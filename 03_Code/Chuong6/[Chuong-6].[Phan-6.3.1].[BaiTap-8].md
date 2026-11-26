# Lời giải Bài tập 6.8

- Chương 6, Mục 6.3.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.3.1].[BaiTap-8].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Chỗ sai | Cách sửa |
|---|---|---|---|
| 9 | cú pháp | `for _ in range(so_diem)` thiếu dấu hai chấm | thêm dấu hai chấm |
| 14 | logic | `return 4.0 * trong / trong` — mẫu số là `trong` thay vì `so_diem` | đổi mẫu số thành `so_diem` |
| 14 | thực thi | không chặn `so_diem` bằng 0 trước vòng lặp | `raise ValueError` khi `so_diem <= 0` |

## Bảng năm bước cho từng lỗi

### Lỗi cú pháp, dòng 9

| Bước | Việc làm |
|---|---|
| 1. Tái lập | chạy bất kỳ, kể cả với 1 điểm |
| 2. Đọc thông báo | `SyntaxError: expected ':'` tại dòng 9 |
| 3. Khoanh vùng | không cần; thông báo đã chỉ đúng dòng |
| 4. Bảng vết | không cần |
| 5. Sửa | thêm dấu hai chấm, chạy lại cả bộ ca |

### Lỗi logic, dòng 14

| Bước | Việc làm |
|---|---|
| 1. Tái lập | **1 điểm** là bộ dữ liệu nhỏ nhất còn gây ra lỗi |
| 2. Đọc thông báo | không có thông báo nào; bước này không giúp gì |
| 3. Khoanh vùng | chia đôi: in `trong` và `so_diem` ngay trước dòng `return` |
| 4. Bảng vết | bảng vết cho thấy với `n` = 1 thì `trong` bằng `so_diem`, nên `4.0 * trong / trong` luôn ra 4,0 |
| 5. Sửa | đổi mẫu số thành `so_diem`, chạy lại cả bộ ca |

### Lỗi thực thi, dòng 14

| Bước | Việc làm |
|---|---|
| 1. Tái lập | **0 điểm** |
| 2. Đọc thông báo | `ZeroDivisionError: float division by zero`, chỉ đúng dòng chia |
| 3. Khoanh vùng | không cần |
| 4. Bảng vết | không cần |
| 5. Sửa | chặn `so_diem <= 0` trước vòng lặp bằng `raise ValueError` có thông điệp nêu giá trị nhận được |

## Điểm chính của bài

**Lỗi logic cho đúng 4,0 với mọi số điểm, và đó là dấu hiệu nhận ra nó.** Tệp kiểm chứng ghi điều đó thành hai khẳng định: `uoc_luong_pi_con_loi(100_000) == 4.0` và `uoc_luong_pi_con_loi(1) == 4.0`. Tử số và mẫu số là cùng một biến, nên tỉ số luôn bằng 1 và kết quả luôn bằng hệ số 4,0.

Một kết quả **không đổi theo dữ liệu vào** là dấu hiệu mạnh nhất của lỗi logic kiểu này. Nó không cần bảng vết để phát hiện: chỉ cần chạy hai lần với hai số điểm khác nhau và so hai kết quả.

**Bộ dữ liệu nhỏ nhất của bước 1 là 1 điểm, không phải 100 000.** Với 1 điểm, bảng vết có đúng một dòng, và một dòng ấy đủ cho thấy `trong` bằng `so_diem`. Với 100 000 điểm, bảng vết có 100 000 dòng và không đọc nổi. Đó là toàn bộ lý do bước 1 đứng trước bước 4.

**Bước 2 không giúp gì cho lỗi logic, và phải ghi rõ như vậy.** Bảng năm bước của lỗi dòng 14 ghi "không có thông báo nào; bước này không giúp gì". Ghi như thế đúng hơn là bỏ trống, vì nó xác nhận bước 2 đã được làm và đã cho kết quả rỗng — chứ không phải bị quên.

**Hai lỗi cùng nằm ở dòng 14 nhưng là hai lỗi khác loại.** Mẫu số sai là lỗi logic; không chặn số điểm bằng 0 là lỗi thực thi. Sửa lỗi logic trước thì lỗi thực thi vẫn còn: `4.0 * trong / so_diem` với `so_diem` bằng 0 vẫn cho `ZeroDivisionError`. Hai lỗi phải sửa riêng, và bước 5 của quy trình đòi đúng điều đó.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 100 000 điểm | `3.143640` sau khi sửa đủ ba lỗi; bản còn lỗi cho `4.000000` |
| Biên | 1 điểm | bộ dữ liệu nhỏ nhất tái lập được lỗi ở dòng 14; chương trình cho `4.0` thay vì một ước lượng |
| Không hợp lệ | 0 điểm | `ZeroDivisionError`; bản đã sửa chặn trước bằng `ValueError` có thông điệp nêu giá trị nhận được |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
