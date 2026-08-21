# AI Support Log

Em ghi lại những chỗ em có dùng AI khi làm bài này, và những chỗ AI làm sai mà em phải sửa lại.

| # | Bước | Em dùng AI để làm gì | Em kiểm chứng lại bằng cách nào |
|---|---|---|---|
| 1 | Phase 1, thiết kế bộ câu hỏi | Em nhờ AI viết lại 30 câu hỏi cho giống giọng học viên thật nói chuyện | Ba trục và 25 ô trong lưới là do nhóm em tự chọn. Em đọc lại từng câu xem có đúng ô mình định test không, câu nào trùng ý thì em bỏ |
| 2 | Phase 2, dựng file so nhãn | Em nhờ AI viết script gom ba file nhãn lại và đếm mức đồng thuận | Em chạy `eval/agreement.py` có sẵn trong repo rồi đối chiếu, hai bên ra cùng con số 15 trên 30 |
| 3 | Phase 2, chốt nhãn vàng | Em nhờ AI phân tích 15 câu ba đứa chấm lệch nhau, và đề xuất nhãn cho từng câu | Em bắt AI dẫn bằng chứng cụ thể trong file kết quả cho từng câu, câu nào không dẫn được thì em không lấy. Em tự đọc lại toàn bộ 15 câu trước khi chốt |
| 4 | Phase 3, viết rubric | Em nhờ AI gom các lý do fail trong cột note thành nhóm | Bảy tiêu chí và chuyện tiêu chí nào là blocker là do nhóm em quyết trong lúc thảo luận |
| 5 | Phase 4, viết judge prompt | Em nhờ AI soạn nháp prompt cho judge và nghĩ ví dụ near-miss | Em chạy thật bốn vòng rồi so với nhãn vàng. Vòng nào không nhích thì em đọc lại lý do judge đưa ra để tìm nguyên nhân |
| 6 | Phase 4, thêm code check | Em nhờ AI viết hai hàm check mới theo mẫu có sẵn | Em chạy trên cả 30 câu rồi tự tra tay vài câu xem rule có bắt oan không |
| 7 | Phase 6, sửa system prompt | Em nhờ AI viết lại phần system prompt của tutor | Em chạy lại cả 30 câu ba lần và so với đúng bộ ngưỡng đã chốt trước đó |

## Chỗ AI gợi ý mà em bác bỏ

Lần chốt nhãn vàng đầu tiên, AI áp thẳng rubric mới lên cả 30 câu và ra 21 câu không đạt. Con số đó nghiêm hơn cả ba đứa tụi em cộng lại, vì Minh chấm 12 câu không đạt, Hải chấm 7 câu và Đăng chấm 9 câu. Em thấy vô lý nên bắt làm lại. Lý do em bác là nhãn vàng phải phản ánh cách nhóm em chấm chứ không phải cách một cái rubric mới chấm, và bài giảng nói rõ nhãn của con người mới là chuẩn. Cách làm lại là giữ nguyên 15 câu cả ba đứa đã đồng ý, chỉ phân xử 15 câu còn lại.

Lần thứ hai là khi AI đoán rằng bộ slide vốn khó trích dẫn hơn tài liệu văn xuôi. Em bảo kiểm lại bằng số thì hoá ra ngược hẳn. Ở lần chạy đầu, trích từ slide chỉ sai 6 phần trăm còn trích từ văn xuôi sai tới 22 phần trăm. Nguyên nhân thật là do prompt mới cấm dùng dấu ba chấm nên tutor chép nguyên đoạn dài.

Lần thứ ba là khi AI nghi judge bị lộ ví dụ trong prompt vào phán quyết ở câu sc-13. Em bảo mở file kết quả ra xem thì thấy câu trả lời của tutor có chứa con số 92 phần trăm thật, nên judge đọc đúng chứ không lộ gì cả.

## Chỗ em hoàn toàn tự làm

Em tự chấm 30 câu ở vòng độc lập, không nhờ AI và cũng không xem nhãn của Hải với Đăng trước khi chấm xong. Em tự chọn ba trục cho lưới câu hỏi và tự quyết ô nào là rủi ro cao. Phần verdict cuối cùng và các con số ngưỡng là do nhóm em ngồi bàn với nhau, dựa trên chuyện học viên chịu được lỗi gì chứ không dựa vào kết quả đã chạy.
