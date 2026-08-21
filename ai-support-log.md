# AI Support Log

| # | Bước | AI dùng để làm gì | Bạn kiểm chứng kết quả thế nào |
|---|---|---|---|
| 1 | Grid/dataset | Gợi ý 24 scenario và metadata | Đối chiếu corpus; giữ pending tới team review |
| 2 | Rubric/routing | Formalize blocker và tuyến chấm | Đối chiếu output contract và evaluator |
| 3 | Code checks | Viết check scope enum/follow-up | Chạy test offline và output thật |
| 4 | Judge prompt | Làm rõ deixis, adversarial, false-pass | So confusion matrix trên cùng dev set |
| 5 | Report | Dựng quyết định và placeholder | Chỉ thay TBD bằng số từ evidence |

AI không tự gán nhãn thay ba rater, tạo output tutor/judge hay chọn verdict khi chưa
có số liệu. Đề xuất điền pass rate/SHIP ước đoán bị bác bỏ vì không kiểm chứng được.
Con người review dataset, chấm độc lập, xử lý bất đồng, xác minh trace và ký verdict.
