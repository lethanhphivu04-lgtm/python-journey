# Vua Cóc Battle Arena — Web Application 🐸

Ứng dụng web hoàn chỉnh mô phỏng nền tảng đấu trí **Vua Cóc** ([vuacoc.com](https://vuacoc.com/)), phục vụ trực tiếp cho lộ trình học tập xuyên suốt của **Python Journey V2** (từ Tuần 07 đến Tuần 15).

---

## 🌟 Tính Năng Nổi Bật

1. **Giao Diện Bàn Đấu Lá Sen (Line Arena):**
   - Thiết kế tinh tế, trực quan, mô phỏng đầm sen 5 ô (`0` đến `4`).
   - Tông màu tự nhiên, nhã nhặn (Forest Green & Warm Terracotta), tránh các phong cách neon/cyberpunk rườm rà.
   - Thể hiện rõ ràng vị trí xuất phát và mục tiêu về đích của Ếch A và Ếch B.

2. **4 Chế Độ Đấu Toàn Diện:**
   - **🎮 Chơi Trực Tiếp (Người vs Bot):** Bạn trực tiếp điều khiển Ếch A bằng các nút hành động hoặc phím mũi tên bàn phím (`←`, `→`, `Space`/`↓`).
   - **⚔️ Đấu Bot (Bot vs Bot):** Lựa chọn 2 bot bất kỳ thi đấu với nhau, hỗ trợ xem diễn biến từng lượt (Animated) hoặc xem kết quả ngay (Instant).
   - **🏆 Giải Đấu Vòng Tròn (Tournament):** Thi đấu cả 2 lượt đi/về (ghế A và ghế B) với tất cả các baseline bots (Forward, Cautious, Wait) và tổng hợp bảng xếp hạng.
   - **💻 Lập Trình Bot Trực Tiếp:** Soạn thảo code Python hàm `choose_action(state)` ngay trên trình duyệt và kiểm tra cú pháp tức thì.

3. **Xem Lại & Xuất Trận Đấu (Interactive Replay):**
   - Thanh trượt timeline cho phép tua lại từng lượt (0 ➔ N).
   - Nhật ký lượt đấu (Turn Log) chi tiết.
   - Tải file Replay JSON về máy để nghiên cứu hoặc nộp evidence theo chuẩn Tuần 10.

---

## 🚀 Cách Khởi Chạy

Ứng dụng được viết **100% bằng thư viện chuẩn của Python** (không cần cài thêm Flask, Django hay bất kỳ thư viện ngoài nào).

```bash
python projects/vuacoc-web/app.py
```

Mở trình duyệt web và truy cập địa chỉ:
👉 **[http://localhost:8080](http://localhost:8080)**

---

## 🏗️ Kiến Trúc Hệ Thống

```text
projects/vuacoc-web/
├── app.py              # Backend HTTP Server & REST API (Python stdlib)
├── README.md           # Hướng dẫn sử dụng
└── static/
    ├── index.html      # Cấu trúc giao diện Đấu trường
    ├── style.css       # Giao diện bàn cờ tự nhiên, nhã nhặn
    └── game.js         # Logic điều khiển, hoạt họa và tương tác
```
