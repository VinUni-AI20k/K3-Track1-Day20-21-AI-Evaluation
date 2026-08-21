# AI Support Log

> Ghi lại bạn đã dùng AI (ChatGPT/Claude/Kimi...) ở những bước nào khi làm deliverables.
> Trung thực là một phần của bài nộp — không ai làm một mình, quan trọng là bạn giữ
> quyền kiểm soát chất lượng.

| # | Bước | AI dùng để làm gì | Bạn kiểm chứng kết quả thế nào |
|---|------|-------------------|-------------------------------|
| 1 | Grid/dataset | Gợi ý 24 scenario và metadata | Đối chiếu corpus; giữ pending tới team review |
| 2 | Rubric/routing | Formalize blocker và tuyến chấm | Đối chiếu output contract và evaluator |
| 3 | Code checks | Viết check scope enum/follow-up | Chạy test offline và output thật |
| 4 | Judge prompt | Làm rõ deixis, adversarial, false-pass | So confusion matrix trên cùng dev set |

- Bác bỏ việc điền pass rate hoặc verdict giả khi chưa có API output và nhãn người.
- Con người review dataset, chấm độc lập, xử lý bất đồng, xác minh trace và ký verdict.
