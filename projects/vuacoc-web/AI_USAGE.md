# AI Usage — Vua Cóc Battle Arena Web 🐸

## 1. Tôi đã dùng AI cho việc gì?

- **Hỗ trợ thiết kế kiến trúc thuần chuẩn (Zero-dependency):** Dùng AI tư vấn cách sử dụng `http.server` và `urllib.parse` của Python Standard Library để làm Web Server & REST API thay vì phải cài Flask/FastAPI nặng nề.
- **Tư vấn cấu trúc giao diện HTML5/CSS3:** Gợi ý bảng màu Forest Green & Warm Terracotta nhã nhặn, cơ chế kéo thanh trượt Timeline để xem lại Replay JSON.
- **Gợi ý thuật toán AI 2D trên đầm sen:** Thiết kế hàm tìm đường `smart_2d_ai` ưu tiên săn ruồi vàng trong bán kính gần và né tránh đá ngầm.

## 2. Tôi đã tự viết hoặc thay đổi phần nào?

- **Backend API Server ([`app.py`](app.py)):** Trực tiếp tổ chức các endpoint REST: `/api/bots`, `/api/rules`, `/api/match/run`, `/api/tournament/run`, `/api/2d/new`, `/api/2d/step`.
- **Frontend Controller ([`static/game.js`](static/game.js)):** Viết logic điều khiển animation trên bàn đấu, liên kết phím bấm mũi tên (`←`, `→`, `Space`/`↓`) và trình biên tập code Bot trực tiếp trên web.
- **Bộ kiểm thử tự động ([`tests/test_web_app.py`](tests/test_web_app.py)):** Viết 6 test case kiểm tra tạo bàn cờ 2D, thuật toán né đá, cơ chế ghi điểm và tích hợp Student Bot.

## 3. Tôi đã kiểm chứng câu trả lời của AI như thế nào?

- **Chạy kiểm thử pytest:**
  ```bash
  pytest projects/vuacoc-web/tests -v
  ```
- **Kiểm thử trực tiếp trên trình duyệt:** Khởi chạy `python projects/vuacoc-web/app.py`, mở trình duyệt tại `http://localhost:8080`, thử nghiệm toàn bộ 4 chế độ: Chơi trực tiếp, Đấu bot, Giải đấu vòng tròn, Đầm sen 2D.
- **Thẩm định độ sẵn sàng Capstone:** Chạy script `check_capstone_readiness.py` đạt kết quả PASS.

## 4. Một điều tôi hiểu rõ hơn

Tôi hiểu rằng việc kết hợp giữa backend logic bằng Python và frontend trực quan bằng JavaScript giúp việc học thuật toán trở nên sống động, dễ debug và dễ giải thích (explainable) hơn rất nhiều so với chỉ in kết quả ra màn hình terminal.
