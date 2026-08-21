"""Chấm results.jsonl bằng LLM judge -> verdicts.jsonl, rồi đối chiếu labels.csv.

Cách dùng (chạy từ root repo):
  python3 eval/judge.py                # chấm tất cả các row mặc định
  python3 eval/judge.py sc-01 sc-03    # chỉ chấm các scenario_id được chọn
  python3 eval/judge.py --prompt eval/judge_prompt.md --labels deliverables/evidence/labels-groundedness-gold.csv --output deliverables/evidence/verdicts-groundedness-v1.jsonl

Model judge mặc định khác model tutor (EVAL_JUDGE_MODEL, mặc định openai/gpt-4o-mini)
để tránh tự chấm chéo cùng một model.
"""
import argparse
import csv
import json
import os
import sys
from pathlib import Path

# tutor.py nằm ở tutor/ (khu vực sản phẩm) — thêm vào sys.path để import được
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))

import tutor
import tracing

# --- Tracing (tuỳ chọn): Braintrust hoặc LangSmith, log mỗi verdict thành 1 trace
_tracer = tracing.init_tracer()

JUDGE_MODEL = os.environ.get("EVAL_JUDGE_MODEL", "openai/gpt-4o-mini")

# judge_prompt.md nằm cạnh file này trong eval/ — resolve theo __file__, không theo cwd
DEFAULT_PROMPT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "judge_prompt.md")

def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def read_labels(path="labels.csv"):
    """labels.csv: scenario_id,label,note — chỉ lấy dòng có label."""
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return {r["scenario_id"]: r["label"].strip().lower()
                for r in csv.DictReader(f) if r.get("scenario_id") and r.get("label", "").strip()}

def build_judge_prompt(rec, template):
    """Nhồi input/answer/sources của 1 row vào template.
    Nếu row có slide context thì gắn vào input — judge phải chấm theo đúng
    bối cảnh học viên đang đứng ở slide nào."""
    input_text = rec.get("input", "")
    if rec.get("slide"):
        input_text = tutor.format_slide_context(rec["slide"]).strip() + "\n" + input_text
    answer = json.dumps(rec.get("output"), ensure_ascii=False, indent=2)
    sources = json.dumps(rec.get("output", {}).get("sources", []),
                         ensure_ascii=False, indent=2)
    return (template.replace("{{input}}", input_text)
                    .replace("{{answer}}", answer)
                    .replace("{{sources}}", sources))

def judge_row(rec, template, judge_model=None):
    model = judge_model or JUDGE_MODEL
    prompt = build_judge_prompt(rec, template)
    data, latency = tutor.chat([{"role": "user", "content": prompt}],
                               model=model, max_tokens=1500)
    content = data["choices"][0]["message"]["content"]
    out = tutor.parse_json_content(content)
    return {"scenario_id": rec["scenario_id"], "verdict": out.get("verdict", "uncertain"),
            "score": out.get("score"), "rationale": out.get("rationale", ""),
            "issues": out.get("issues", []), "raw_content": content,
            "usage": data.get("usage", {}), "latency_s": round(latency, 2)}

def print_confusion(verdicts, labels, criterion_name="overall"):
    """Ma trận nhầm lẫn judge (hàng) vs nhãn người (cột) + tỉ lệ đồng thuận & chỉ số calibration."""
    classes = ["pass", "fail", "uncertain"]
    pairs = [(v["scenario_id"], v["verdict"], labels[v["scenario_id"]])
             for v in verdicts if v["scenario_id"] in labels]
    if not pairs:
        print(f"\nLabels file chưa có nhãn nào trùng scenario_id -> chưa tính được agreement cho {criterion_name}.")
        return
    print(f"\nConfusion matrix [{criterion_name}] (hàng = judge, cột = nhãn người):")
    print("%10s | %s" % ("", " ".join("%9s" % c for c in classes)))
    for cj in classes:
        row = [sum(1 for _, v, h in pairs if v == cj and h == ch) for ch in classes]
        print("%10s | %s" % (cj, " ".join("%9d" % x for x in row)))

    total = len(pairs)
    agree = sum(1 for _, v, h in pairs if v == h)

    # Detailed metrics
    human_pass = sum(1 for _, _, h in pairs if h == "pass")
    human_fail = sum(1 for _, _, h in pairs if h == "fail")

    judge_pass_on_human_pass = sum(1 for _, v, h in pairs if v == "pass" and h == "pass")
    judge_fail_on_human_fail = sum(1 for _, v, h in pairs if v == "fail" and h == "fail")
    false_block = sum(1 for _, v, h in pairs if v == "fail" and h == "pass")
    missed_bad = sum(1 for _, v, h in pairs if v == "pass" and h == "fail")

    good_recall = (judge_pass_on_human_pass / human_pass * 100.0) if human_pass > 0 else 0.0
    bad_catch = (judge_fail_on_human_fail / human_fail * 100.0) if human_fail > 0 else 0.0

    print("\n--- Calibration Metrics ---")
    print(f"Total Paired Cases: {total}")
    print(f"Agreement: {agree}/{total} = {100.0 * agree / total:.1f}%")
    print(f"Good-Output Recall (Judge Pass | Human Pass): {judge_pass_on_human_pass}/{human_pass} = {good_recall:.1f}%")
    print(f"Bad-Output Catch Rate (Judge Fail | Human Fail): {judge_fail_on_human_fail}/{human_fail} = {bad_catch:.1f}%")
    print(f"False-Block Count (Judge Fail on Good): {false_block}")
    print(f"Missed-Bad Count (Judge Pass on Bad): {missed_bad}")

    discrepant = [sid for sid, v, h in pairs if v != h]
    if discrepant:
        print(f"Discrepant Scenario IDs ({len(discrepant)}): {', '.join(discrepant)}")

def parse_args():
    parser = argparse.ArgumentParser(description="Judge tutor responses with LLM")
    parser.add_argument("scenarios", nargs="*", help="Specific scenario IDs to evaluate")
    parser.add_argument("--results", default="results.jsonl", help="Path to results.jsonl")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT_PATH, help="Path to judge prompt markdown")
    parser.add_argument("--labels", default="labels.csv", help="Path to human gold labels CSV")
    parser.add_argument("--output", default="verdicts.jsonl", help="Path to output verdicts JSONL")
    parser.add_argument("--criterion", default="groundedness", help="Name of criterion being judged")
    parser.add_argument("--model", default=JUDGE_MODEL, help="Judge model identifier")
    return parser.parse_args()

def main():
    args = parse_args()
    results = read_jsonl(args.results)
    if not results:
        sys.exit(f"Không thấy {args.results} — chạy python3 eval/run_eval.py trước.")
    if not tutor.get_api_key(args.model):
        sys.exit("Chưa có API key cho judge model %s — xem .env.example." % args.model)

    chosen = set(args.scenarios)
    rows = [r for r in results if not chosen or r["scenario_id"] in chosen]
    rows = [r for r in rows if "output" in r]  # bỏ row lỗi, không có gì để chấm

    if not os.path.exists(args.prompt):
        sys.exit(f"Không thấy judge prompt tại {args.prompt}")
    template = open(args.prompt, encoding="utf-8").read()
    print(f"Chấm {len(rows)} row [{args.criterion}] bằng judge {args.model} ...")

    verdicts = []
    for i, rec in enumerate(rows, 1):
        print("[%d/%d] %s ... " % (i, len(rows), rec["scenario_id"]), end="", flush=True)
        try:
            v = judge_row(rec, template, judge_model=args.model)
            v["criterion"] = args.criterion
            _tracer.log_run(
                name="judge-run",
                inputs={"scenario_id": rec["scenario_id"], "judge_model": args.model, "criterion": args.criterion},
                outputs={"verdict": v["verdict"], "rationale": v.get("rationale", "")},
                metrics={**{k: x for k, x in v.get("usage", {}).items()
                            if isinstance(x, (int, float))},
                         "latency_s": v.get("latency_s", 0)},
            )
            print(v["verdict"])
        except Exception as e:
            v = {"scenario_id": rec["scenario_id"], "criterion": args.criterion, "verdict": "uncertain",
                 "error": str(e)}
            print("LỖI: %s" % e)
        verdicts.append(v)

    with open(args.output, "w", encoding="utf-8") as f:
        for v in verdicts:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"Ghi {len(verdicts)} verdict vào {args.output}")
    if _tracer.backend:
        _tracer.flush()
        print("Đã log %d trace judge lên %s." % (len(verdicts), _tracer.backend))

    labels_dict = read_labels(args.labels)
    print_confusion(verdicts, labels_dict, criterion_name=args.criterion)

if __name__ == "__main__":
    main()
