# Tracing Project & Verification Evidence

- **Tracing Backend**: LangSmith
- **Project Name**: i-evaluation
- **Project URL**: https://smith.langchain.com/o/default/projects/p/ai-evaluation
- **Tutor Model**: gemini/models/gemini-flash-lite-latest
- **Judge Model**: gemini/models/gemma-4-31b-it
- **Verification Status**: VERIFIED (Cloud tracing connection established and validated via LangSmith API)
- **Execution Date**: 2026-08-21T11:03:27+07:00 (Asia/Saigon)

---

## 1. Tracing Architecture

- **Instrumentation**: eval/tracing.py (LangSmithTracer)
- **Captured Metrics**:
  - scenario_id & question inputs
  - Multi-step tool calls (kb_search queries, retrieved corpus doc/sections)
  - Raw JSON outputs & parsed fields
  - Latency (latency_s), token counts (prompt_tokens, completion_tokens, 	otal_tokens), cost estimation (cost_usd)
- **Run Tracking**:
  - Homogeneous 22-scenario candidate evaluation trace batch
  - Multi-round LLM Judge calibration traces
