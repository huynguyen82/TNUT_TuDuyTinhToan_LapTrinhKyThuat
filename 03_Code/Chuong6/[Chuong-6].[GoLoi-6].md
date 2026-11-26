# Lời giải Bài gỡ lỗi GL6

- Chương 6 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-6].[GoLoi-6].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo hoặc biểu hiện | Cách sửa |
|---|---|---|---|---|
| 9 | cú pháp | `def f_dao_ham(x)` thiếu dấu hai chấm | `SyntaxError: expected ':'` | Thêm dấu hai chấm |
| 18 | thực thi | Không kiểm `f_dao_ham(x_cu)` khác 0 trước khi chia | `ZeroDivisionError: float division by zero` với `x0` = 0,8165 | Chặn đạo hàm bằng 0 và phát sinh `ValueError` có thông điệp rõ |
| 19 | logic | `if x_moi - x_cu <= SAI_SO`, thiếu `abs` | **không có**; với `x0` = 3,0 hàm dừng ngay lượt đầu và trả về 2,36 | `if abs(x_moi - x_cu) <= SAI_SO` |

Sau khi sửa đủ ba lỗi: `x0` = 3,0 cho nghiệm **2,0945514815** sau **6 lượt**.

## Bảng năm bước cho lỗi logic ở dòng 19

Đây là phần đề bài yêu cầu nộp kèm.

| Bước | Việc làm |
|---|---|
| 1. Tái lập | `x0` = 3,0 là bộ dữ liệu nhỏ nhất tái lập được: đúng một lần gọi hàm |
| 2. Đọc thông báo | Không có thông báo nào. Bước này **không giúp gì**, và ghi rõ như vậy là một phần của bảng |
| 3. Khoanh vùng | In `x_cu` và `x_moi` mỗi lượt; thấy hàm dừng ngay sau lượt 1 trong khi Newton phải cần vài lượt |
| 4. Bảng vết | Lượt 1 cho `x_moi − x_cu` = −0,64. Hiệu **âm**, nên điều kiện `≤ 10⁻¹⁰` đúng ngay, dù bước nhảy còn rất lớn |
| 5. Sửa | Thêm `abs` vào điều kiện dừng, rồi chạy lại cả ba bộ ca |

Bước 4 là bước chỉ ra nguyên nhân: điều kiện dừng đang hỏi *bước nhảy có nhỏ không* nhưng viết thành *bước nhảy có âm không*.

## Điểm chính của bài

**Lỗi dòng 19 phụ thuộc hướng đi của dãy lặp, nên hai ca thường cho hai kết quả khác hẳn nhau.**

| Điểm đầu | Hướng các bước Newton | Bản còn lỗi | Bản đã sửa |
|---|---|---|---|
| 3,0 | đi **xuống**, hiệu luôn âm | 2,3600000000 sau 1 lượt | 2,0945514815 sau 6 lượt |
| 2,0 | đi **lên**, hiệu dương | 2,0945681211 sau 2 lượt | 2,0945514815 sau 5 lượt |

Với `x0` = 3,0 thì sai rõ: 2,36 cho `f(2,36)` = 3,42, cách nghiệm rất xa. Với `x0` = 2,0 thì bản còn lỗi cho 2,0945681211 — **trùng bản đúng tới bốn chữ số thập phân**. Một bộ ca chỉ có điểm đầu 2,0 sẽ kết luận chương trình đạt.

Bài học, và nó khép lại mạch của cả Chương 6: **một bộ ca kiểm thử cần nhiều ca thường ở các phía khác nhau của nghiệm, không chỉ một**. Cùng loại ca, cùng miền hợp lệ, mà một ca phơi lỗi còn một ca gần như che nó.

**Lỗi dòng 18 chỉ lộ ra ở một điểm đầu duy nhất.** Đạo hàm `3x² − 2` bằng 0 tại `x` = √(2/3) ≈ 0,8165. Mọi điểm đầu khác đều chạy bình thường. Ca không hợp lệ phải được chọn **từ đặc tả** — từ dòng điều kiện áp dụng của phương pháp Newton — chứ không thể nghĩ ra bằng cách đọc mã. Đây đúng là lỗi `L6.2-5` nhìn từ phía người viết ca.

**Bản đã sửa chặn bằng `ValueError` chứ không để `ZeroDivisionError` nổ ra.** Hai cách đều dừng chương trình, nhưng thông điệp khác hẳn: `float division by zero` không nói gì về bài toán, còn `dao ham bang 0 tai x = 0.816496580927726` nói đủ để tái lập lại lỗi mà không cần thử lại. Đó là quy tắc thứ hai của Khối 4 Mục 6.3.1.

**Ba lỗi thuộc ba loại khác nhau, và chỉ lỗi thứ ba cần tới quy trình năm bước.** Lỗi cú pháp được trình thông dịch chỉ đúng dòng. Lỗi thực thi được thông báo chỉ đúng dòng. Chỉ lỗi logic là không có gì chỉ, nên nó là lỗi duy nhất đáng lập bảng năm bước — và đề bài chỉ yêu cầu bảng cho nó.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Điểm đầu 3,0 | Nghiệm `2.0945514815` sau 6 lượt. Bản còn lỗi cho `2.36` sau **1** lượt |
| Biên | Điểm đầu 2,0 | Nghiệm `2.0945514815` sau 5 lượt. Bản còn lỗi cho `2.0945681211` — trùng tới bốn chữ số thập phân, nên ca này gần như che được lỗi |
| Không hợp lệ | Điểm đầu 0,8165 | Đạo hàm bằng 0; phải báo rõ không tính được thay vì để `ZeroDivisionError` nổ ra |
