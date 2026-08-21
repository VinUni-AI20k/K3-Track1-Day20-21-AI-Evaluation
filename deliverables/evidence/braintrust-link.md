# Braintrust — trace của mọi run tutor & judge

- **Project:** `ai-evaluation`
- **Org:** `haidang2425`
- **Dashboard:** https://www.braintrust.dev/app/haidang2425/p/ai-evaluation/trace?object_type=project_logs&object_id=18e6525d-b83f-4ca6-be78-282e49beaae9&r=33c037384566d4b4b1745df27e453440&s=889dcbc642639384

## Những gì được log

| Loại trace | Sinh ra từ | Nội dung |
|---|---|---|
| `tutor-run` | `eval/run_eval.py` | câu hỏi + slide context, output JSON, tool calls `kb_search`, tokens, cost, latency |
| `judge-run` | `eval/judge.py` | scenario_id, model judge, verdict, rationale, tokens, latency |

Số trace: 30 `tutor-run` (dataset v1) + 4×30 `judge-run` (calibration v1→v4).

## Cấu hình

```env
BRAINTRUST_API_KEY=<key của nhóm — KHÔNG commit>
BRAINTRUST_PROJECT=ai-evaluation
```

## Lưu ý khi đặt key

`tutor/tutor.py::load_dotenv()` **không cắt comment cuối dòng**. Viết
`BRAINTRUST_API_KEY=sk-xxx   # ghi chú` sẽ khiến cả phần ghi chú trở thành một phần
của key; nếu ghi chú có dấu tiếng Việt thì thư viện HTTP báo
`UnicodeEncodeError: 'latin-1' codec can't encode character` và **toàn bộ trace bị
drop**. Đặt key trần, không ghi chú cùng dòng.

## Bug đã sửa trong repo (nếu không sửa thì mất trace)

`bool` là subclass của `int` trong Python, nên filter `isinstance(x, (int, float))` ở
`eval/judge.py` và `eval/run_eval.py` không lọc được nó. OpenRouter trả
`usage.is_byok` khi thì `0` khi thì `false`; gặp `false` thì Braintrust trả HTTP 400
(`metrics.is_byok: Expected number, received boolean`) và **drop cả batch**. Đã loại
`bool` ở cả hai chỗ.
