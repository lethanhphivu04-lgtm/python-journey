# Tuần 11 — Exceptions · Tracebacks · Debugging · Defensive coding

Tuần này bạn đọc lỗi trước khi sửa, bắt đúng lỗi dự kiến và để programming bug
tiếp tục hiện rõ.

## Outcomes

- đọc exception type, message và vị trí cuối traceback;
- phân biệt expected bad input với programming bug;
- dùng `try/except/else/finally` đúng vai trò và `raise` khi contract bị vi phạm;
- áp dụng `Reproduce → Read traceback → Isolate → Fix → Re-test`;
- phân biệt strategy loss với software defect trong bot local.

Đi theo [notes](notes.md), [examples](examples/), [exercises](exercises/),
[hints](hints.md), [machine check](checks/README.md) và
[mini-project](mini-project/README.md).

Không dùng `except Exception: pass` để tạo cảm giác “robust”.

Tài liệu [README.md](README.md) được viết bằng giọng văn cô đọng của kỹ sư phần mềm nên có nhiều thuật ngữ chuyên môn.

Dưới đây là phần **"dịch nghĩa" sang ngôn ngữ đời thường, kèm ví dụ thực tế** để bạn hiểu trọn vẹn từng câu chữ:

---

### 1. Câu mở đầu:
> *"Tuần này bạn đọc lỗi trước khi sửa, bắt đúng lỗi dự kiến và để programming bug tiếp tục hiện rõ."*

* **Nghĩa thực tế**:
  * Khi mới học lập trình, thấy màn hình hiện chữ đỏ báo lỗi thì phản xạ tự nhiên là hoảng loạn, đoán mò rồi sửa bừa.
  * Tuần này rèn cho bạn **thói quen của lập trình viên chuyên nghiệp**: Bình tĩnh đọc thông báo lỗi trước.
  * Cái gì là dữ liệu người dùng nhập sai (ví dụ: gõ chữ vào ô nhập số) thì ta bắt lại để nhắc nhở họ. Còn cái gì là lỗi do chính mình viết code sai (ví dụ: gõ nhầm tên biến) thì **phải để nó hiện ra màn hình** để mình biết đường mà sửa, tuyệt đối không được giấu nó đi.

---

### 2. Giải nghĩa 5 mục tiêu (Outcomes):

#### ① *"Đọc exception type, message và vị trí cuối traceback"*
* **Nghĩa là**: Khi code bị lỗi, đừng vội nhìn vào dòng đầu tiên. Hãy nhìn vào **dòng cuối cùng** để trả lời 3 câu hỏi:
  1. Nó là loại lỗi gì? (`ValueError`, `ZeroDivisionError`, `KeyError`...)
  2. Nó giải thích lỗi ra sao? (Ví dụ: `division by zero` - chia cho số 0)
  3. Dòng nào trong file của bạn đã gây ra việc đó?

---

#### ② *"Phân biệt expected bad input với programming bug"*
* **Expected bad input (Dữ liệu xấu dự kiến được)**:
  * Người dùng nhập vào ô tuổi là `"hai mươi"` thay vì số `20`.
  * $\rightarrow$ Đây là chuyện bình thường ngoài đời. Bạn dùng `try...except ValueError` để bắt lại và in ra: *"Vui lòng nhập số"*.
* **Programming bug (Lỗi do người lập trình)**:
  * Bạn gõ nhầm tên biến: `print(toiu)` thay vì `print(tuoi)`.
  * $\rightarrow$ Đây là lỗi của bạn. Không được dùng `try/except` để che nó lại. Phải để nó báo lỗi `NameError` để bạn biết mà sửa tên biến.

---

#### ③ *"Dùng `try/except/else/finally` đúng vai trò và `raise` khi contract bị vi phạm"*
* **Chia đúng việc cho 4 khối**:
  * `try`: Chỉ bọc đúng dòng có nguy cơ lỗi (như ép kiểu số, mở file).
  * `except`: Bắt đúng lỗi đó để xử lý.
  * `else`: Chỉ chạy khi mọi thứ **thành công** (không có lỗi).
  * `finally`: Việc **bắt buộc phải làm** dù thành công hay thất bại (như ghi nhật ký, đóng kết nối).
* **`raise` khi vi phạm hợp đồng (contract)**:
  * Giả sử bạn viết hàm rút tiền `rut_tien(so_tien)`. "Hợp đồng" của hàm là `so_tien` phải $> 0$.
  * Nếu ai đó truyền vào `-50000`, hàm của bạn phải chủ động "bấm chuông báo động":
    ```python
    if so_tien <= 0:
        raise ValueError("Số tiền rút phải lớn hơn 0!")
    ```

---

#### ④ *"Áp dụng Reproduce → Read traceback → Isolate → Fix → Re-test"*
* Đây là **quy trình 5 bước gỡ lỗi (Debugging loop)**:
  1. **Reproduce (Tái hiện lỗi)**: Tìm ra đúng thao tác hoặc dữ liệu làm cho chương trình bị lỗi lại được lần nữa (để chắc chắn lỗi có thật).
  2. **Read traceback (Đọc vết lỗi)**: Đọc thông báo lỗi từ dòng cuối lên.
  3. **Isolate (Cô lập)**: Thu hẹp phạm vi, tìm ra chính xác dòng code nào làm hỏng việc.
  4. **Fix (Sửa)**: Sửa đúng nguyên nhân gốc rễ.
  5. **Re-test (Kiểm tra lại)**: Chạy lại thử nghiệm xem lỗi đã hết chưa và việc sửa đó có làm hỏng chỗ khác không.

---

#### ⑤ *"Phân biệt strategy loss với software defect trong bot local"*
* Trong dự án lập trình Bot chơi game (Vua Cóc):
  * **Strategy loss (Thua do chiến thuật)**: Bot chạy mượt mà, không lỗi dòng nào, nhưng thuật toán tính toán nước đi dở nên bị đối phương đánh bại. $\rightarrow$ *Đây không phải lỗi phần mềm, muốn thắng thì cần cải thiện chiến thuật.*
  * **Software defect (Lỗi phần mềm)**: Bot đang chạy thì bị crash văng ra ngoài, hoặc Bot đòi đi một nước đi trái luật bàn cờ. $\rightarrow$ *Đây là lỗi lập trình (bug), bắt buộc phải sửa.*

---

### 3. Câu cảnh báo cuối bài:
> *"Không dùng `except Exception: pass` để tạo cảm giác “robust”."*

* **"Robust"** có nghĩa là "mạnh mẽ, kiên cường, không bao giờ sập".
* Nhiều người học lầm tưởng rằng bọc toàn bộ code trong `except Exception: pass` thì chương trình sẽ không bao giờ văng màn hình đỏ $\rightarrow$ tưởng thế là code xịn, "bền bỉ".
* Thực chất đó là **sự bền bỉ giả tạo**. Nó giống như việc ngôi nhà đang cháy nhưng bạn tháo pin chuông báo cháy ra để nhà được yên tĩnh. Chương trình bên trong đã hỏng nát dữ liệu mà bạn hoàn toàn không hề hay biết.

---

💡 **Tóm gọn lại bằng 1 câu**:
> *Tuần 11 dạy bạn cách **đối diện thẳng thắn với lỗi**: biết cách đọc lỗi để sửa đúng chỗ, bắt lỗi người dùng một cách lịch sự, và không bao giờ được viết code che giấu lỗi của chính mình.*