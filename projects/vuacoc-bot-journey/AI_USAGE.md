# AI Usage — VuaCóc Bot Journey 🐸

## 1. Tôi đã dùng AI cho việc gì?

- **Hỗ trợ phân tích trường hợp biên (Edge Cases):** Dùng AI để thảo luận về các tình huống đối đầu giữa Student Bot và các baseline bots (khoảng cách $\le 1$, lượt cuối cùng `turn == max_turns`, trường hợp `opponent_position` không được cung cấp).
- **Gợi ý thiết kế ca kiểm thử (Test Design):** Sử dụng AI để rà soát danh sách kiểm thử theo cấu trúc **Arrange → Act → Assert (AAA)**, bảo đảm đủ 5 loại: Normal case, Boundary/Edge case, Defensive/Invalid input, Regression case, và Legality contract.
- **Rà soát chất lượng mã nguồn (Code Review & Linting):** Kiểm tra mã nguồn có vi phạm ranh giới giáo trình hay không (đảm bảo 100% Standard Library, không thêm dependency ngoài, tuân thủ `ruff check`).

## 2. Tôi đã tự viết hoặc thay đổi phần nào?

- **Thiết kế giải thuật của Bot ([`student_bot/bot.py`](student_bot/bot.py)):** Trực tiếp thiết kế quy tắc ưu tiên 3 bước:
  1. *Phòng vệ an toàn:* Thẩm định `validate_state`, fallback an toàn nếu dữ liệu thiếu hoặc sai kiểu.
  2. *Bảo toàn chiến thắng:* Nếu đã ở đích (`position == goal`), chủ động đứng chờ (`wait`).
  3. *Tối ưu hóa nước đi:* Tính toán hướng di chuyển ngắn nhất (`get_direction_to_goal`) để tiến về đích trong 4 lượt, vượt qua cơ chế dừng chờ của `cautious_bot`.
- **Phân rã hàm (Decomposition):** Tách logic phức tạp thành các hàm nhỏ độc lập: `validate_state`, `is_at_goal`, `get_direction_to_goal`, `assess_tactical_situation`, `choose_action`, `explain_decision`.
- **Viết bộ kiểm thử chuyên sâu ([`tests/test_student_bot.py`](tests/test_student_bot.py)):** Xây dựng 20 test case độc lập kiểm tra mọi khía cạnh hoạt động của bot.
- **Thực thi và kiểm chứng giải đấu:** Chạy giải đấu vòng tròn hai lượt A/B đối đầu với toàn bộ 3 baseline bots (`WaitBot`, `ForwardBot`, `CautiousBot`), ghi nhận kết quả thực tế.

## 3. Tôi đã kiểm chứng câu trả lời của AI như thế nào?

- **Kiểm thử tự động bằng pytest:** Chạy toàn bộ 54 unit test trong repository và 20 test riêng cho `student_bot`:
  ```bash
  pytest projects/vuacoc-bot-journey/tests/test_student_bot.py -v
  pytest projects/vuacoc-bot-journey/tests -q
  ```
- **Kiểm tra cú pháp và phong cách mã nguồn:** Dùng Ruff để xác nhận chuẩn PEP 8 và sạch lỗi import:
  ```bash
  ruff check projects/vuacoc-bot-journey
  ```
- **Thử nghiệm input bất thường (Fuzzing / Defensive testing):** Truyền các giá trị sai kiểu (`None`, chuỗi `"zero"`, dictionary rỗng `{}`) vào hàm `choose_action()` để đảm bảo bot không bao giờ bị sập (crash).
- **Xác thực giải đấu thực tế (Tournament Proof):** Chạy `evaluate_bot` xác nhận tỷ lệ hoàn thành trận đấu đạt 100%, tỷ lệ nước đi hợp lệ đạt 100%, thắng 4 trận, hòa 2 trận, không thua trận nào.

## 4. Một điều tôi hiểu rõ hơn

Tôi hiểu rằng một con Bot thi đấu tốt trong môi trường phần mềm không chỉ là một thuật toán tính điểm phức tạp, mà trước hết phải là một **mô-đun phần mềm đáng tin cậy**: biết phòng vệ trước dữ liệu bẩn, không bao giờ vi phạm luật chơi, có thể giải thích được lý do cho từng quyết định (`explain_decision`), và được chứng minh bằng một bộ kiểm thử hồi quy tự động.
