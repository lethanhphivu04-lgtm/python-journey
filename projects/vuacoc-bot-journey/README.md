# VuaCóc Bot Journey

VuaCóc Bot Journey là project xuyên khóa để người học nâng cấp cùng một hệ
thống ra quyết định từ Week 07 đến Week 15. Game gốc có thể tham khảo tại
[vuacoc.com](https://vuacoc.com/), nhưng track này chỉ dùng mô hình học tập
local, không tuyên bố API/runtime compatibility. Người học không gặp `functions`,
`dict`, JSON, exceptions, `pytest`, modules và OOP như những chương rời rạc:
mỗi chủ đề làm bot **more capable, more reliable, more explainable**.

Đây là một spiral project, không phải project chỉ bắt đầu ở tuần cuối:

```text
Observe state
   ↓
Choose action
   ↓
Run match
   ↓
Inspect result
   ↓
Test/debug
   ↓
Improve
```

Learning loop xuyên suốt:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Course-local Line Arena

Implementation local biến hành trình thành evidence chạy được:

```text
Student Bot → Local Arena → Baseline Bots → Match → Replay → Evaluation
```

- [Local Arena](local_arena/README.md) sở hữu match loop và teaching contract.
- [Baseline bots](baselines/README.md) cung cấp đúng ba policy minh bạch.
- [Student Bot](student_bot/README.md) là starter xuyên khóa.

```text
COURSE_LOCAL_ARENA = YES
VUACOC_PRODUCTION_COMPATIBILITY = NOT_CLAIMED
NETWORK_CALLS = 0
SECRETS = 0
```

## Hành trình W07–W15

| Week | Milestone | Điều bot học thêm |
|---|---|---|
| W07 | [Function Bot](milestones/w07-function-bot.md) | quyết định xác định bằng function |
| W08 | [State + Heuristic](milestones/w08-state-and-heuristic.md) | state có cấu trúc và rule dễ giải thích |
| W09 | [Midterm Bot V1](milestones/w09-midterm-bot-v1.md) | ghép các phần thành bot chạy local |
| W10 | [Replay + Data](milestones/w10-replay-and-data.md) | lưu evidence bằng file, JSON và CSV |
| W11 | [Robust Bot](milestones/w11-robustness-and-debugging.md) | phân biệt lỗi phần mềm với thua chiến thuật |
| W12 | [Tested Bot](milestones/w12-testing-with-pytest.md) | khóa hành vi bằng regression tests |
| W13 | [Adapter Boundary](milestones/w13-modules-cli-arena-adapter.md) | tách bot core khỏi runtime adapter |
| W14 | [Strategy Composition](milestones/w14-strategy-composition.md) | thay strategy mà không viết lại core |
| W15 | [Capstone Tournament](milestones/w15-capstone-tournament.md) | tích hợp, đánh giá, giải thích và demo |

Tournament W15 chạy hai lượt A/B trước mỗi baseline để evidence không phụ thuộc
một phía xuất phát. Các metric được báo riêng, không gộp thành rating.

Xem [bảng milestone](MILESTONES.md), [kiến trúc](ARCHITECTURE.md),
[evaluation](EVALUATION.md) và [trạng thái integration contract](INTEGRATION_CONTRACT.md).

## Phạm vi của track

VuaCóc Bot Journey là **flagship capstone track**: một lộ trình nổi bật giúp
kết nối các tuần thành một câu chuyện phát triển liên tục. Đây không phải lựa
chọn capstone bắt buộc duy nhất. Mọi capstone vẫn dùng yêu cầu và rubric
canonical trong [`FINAL_PROJECT.md`](../../FINAL_PROJECT.md).

Python Journey chỉ đi đến nhiều bot độc lập cùng tham gia môi trường chung,
match, tournament và evaluation. Reinforcement learning, self-play training,
MCTS chuyên sâu, opponent modeling nâng cao, LLM agent orchestration và hệ
thống agent phân tán nằm ngoài phạm vi khóa học.

## Trạng thái integration

```text
VUACOC_RUNTIME_CONTRACT = UNVERIFIED
ARENA_ADAPTER = DESIGN_ONLY
PRODUCTION_INTEGRATION = NO
```

Các milestone hiện dùng teaching models và local evidence. Không nội dung nào
trong thư mục này được xem là contract runtime chính thức của VuaCóc.

---

## Setup and Installation

Dự án được xây dựng 100% bằng thư viện tiêu chuẩn của Python (>= 3.12). Không yêu cầu cài đặt package bên ngoài nào để chạy match hay tournament.

1. Đảm bảo bạn đã cài đặt Python 3.12+:
   ```bash
   python --version
   ```

2. (Tùy chọn) Cài đặt maintainer dependencies để chạy kiểm thử bằng `pytest`:
   ```bash
   python -m pip install --upgrade "pip>=25.1"
   python -m pip install --group dev
   ```

## Usage and Execution

### 1. Chạy thử nghiệm một trận đấu đơn (Single Match):
Từ thư mục gốc repository:
```bash
# Đấu giữa Student Bot (A) và WaitBot (B) có ghi log Replay
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a student --bot-b wait --replay

# Đấu giữa Student Bot (A) và CautiousBot (B)
python projects/vuacoc-bot-journey/local_arena/cli.py --bot-a student --bot-b cautious --replay
```

### 2. Chạy Giải đấu Vòng tròn 2 Lượt A/B (Tournament):
Chạy đánh giá Student Bot toàn diện với 3 baseline bots:
```bash
python -c "from local_arena.tournament import evaluate_bot, summarize_results; from student_bot.bot import choose_action; from baselines.wait_bot import choose_action as wb; from baselines.forward_bot import choose_action as fb; from baselines.cautious_bot import choose_action as cb; res = evaluate_bot(choose_action, {'wait': wb, 'forward': fb, 'cautious': cb}); print(summarize_results(res))"
```

## Test and Verification

Chạy toàn bộ bộ kiểm thử tự động với `pytest`:
```bash
# Chạy bộ test riêng cho Student Bot
pytest projects/vuacoc-bot-journey/tests/test_student_bot.py -v

# Chạy toàn bộ các test của VuaCóc Bot Journey
pytest projects/vuacoc-bot-journey/tests -q
```

Kiểm tra độ sẵn sàng Capstone:
```bash
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py projects/vuacoc-bot-journey
```

## Cấu trúc mã nguồn (Project Architecture)

```text
projects/vuacoc-bot-journey/
├── README.md                 # Tài liệu tổng quan (setup, usage, test)
├── AI_USAGE.md               # Bản kê khai và giải trình sử dụng AI
├── MILESTONES.md             # Lộ trình phát triển từ Tuần 07 đến Tuần 15
├── student_bot/              # Bộ não Bot của học viên
│   ├── bot.py                # Thuật toán ra quyết định, phân rã hàm và giải trình
│   └── README.md             # Ghi chú riêng cho student_bot
├── baselines/                # Các bot đối thủ mẫu
│   ├── wait_bot.py           # Luôn đứng chờ
│   ├── forward_bot.py        # Luôn tiến về phía trước
│   └── cautious_bot.py       # Dừng lại khi gặp đối thủ ở cự ly gần (<= 1)
├── local_arena/              # Đấu trường bàn cờ 1D Line Arena
│   ├── arena.py              # Động cơ mô phỏng trận đấu, xử lý lượt và phân định thắng thua
│   ├── tournament.py         # Tổ chức giải đấu vòng tròn 2 lượt A/B
│   ├── models.py             # Cấu trúc dữ liệu MatchResult, TurnRecord
│   └── replay.py             # Xuất và đọc lịch sử trận đấu (JSON)
└── tests/                    # Bộ kiểm thử tự động (> 40 tests)
    ├── test_student_bot.py   # Unit test, boundary test, invalid input, regression
    ├── test_baseline_bots.py # Kiểm thử hành vi 3 bot mẫu
    ├── test_local_arena.py   # Kiểm thử động cơ đấu trường và clamp biên
    ├── test_tournament.py    # Kiểm thử tính xác định của giải đấu
    └── test_replay.py        # Kiểm thử tính toàn vẹn của file Replay
```

## Kết quả Tournament thực tế (Evidence)

Kết quả khi đưa Student Bot vào giải đấu 2 lượt A/B với 3 baseline bots:
- **Số trận đấu:** 6 trận (gặp `WaitBot`, `ForwardBot`, `CautiousBot` ở cả ghế A và B).
- **Thắng:** 4 trận (thắng tuyệt đối `WaitBot` và `CautiousBot` ở cả 2 ghế).
- **Hòa:** 2 trận (hòa `ForwardBot` do cả hai cùng chạm đích ở lượt thứ 4).
- **Thua:** 0 trận.
- **Tỷ lệ hoàn thành trận đấu (Completion Rate):** 100% (6/6).
- **Tỷ lệ nước đi hợp lệ (Legal Action Rate):** 100% (luôn nằm trong `{"left", "right", "wait"}`).
- **Số lỗi hệ thống (Known Failures):** 0.

## Quyết định thiết kế (Design Decisions)

1. **Phân rã hàm độc lập (Decomposition):** Hàm `choose_action` không chứa code lồng nhau phức tạp mà ủy thác cho các hàm con: `validate_state`, `is_at_goal`, `get_direction_to_goal`, `assess_tactical_situation`.
2. **Lập trình phòng thủ (Defensive Programming):** Sử dụng `state.get()` và kiểm tra kiểu chặt chẽ trong `validate_state`. Nếu nhận dictionary rỗng hoặc dữ liệu thiếu/sai kiểu, bot tự động chọn hành động an toàn `"wait"` thay vì làm sập chương trình.
3. **Tính giải trình (Explainability):** Hàm `explain_decision` giúp người học và giám khảo hiểu rõ ràng trạng thái bàn cờ nào đã dẫn đến nước đi cụ thể của Bot.

## AI Usage

Chi tiết giải trình việc sử dụng AI theo đúng quy định của khóa học được ghi nhận tại file [`AI_USAGE.md`](AI_USAGE.md).
