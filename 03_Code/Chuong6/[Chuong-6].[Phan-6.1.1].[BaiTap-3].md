# Lời giải Bài tập 6.3

- Chương 6, Mục 6.1.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.1.1].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo hoặc biểu hiện | Cách sửa |
|---|---|---|---|---|
| 3 | cú pháp | `def f(x)` thiếu dấu hai chấm | `SyntaxError: expected ':'`; không chạy dòng nào | thêm dấu hai chấm |
| 13 | logic | `f(a) * f(giua) > 0.0` thay vì `< 0.0` | không báo gì; `chia_doi(2.0, 3.0)` cho **0,147059** | đổi dấu so sánh thành `<` |
| 18 | thực thi | `return (a + b) / so_luot` thay vì `/ 2.0` | `ZeroDivisionError: float division by zero` khi vòng lặp chạy 0 lượt | chia cho `2.0` |

Sau khi sửa đủ ba lỗi, `chia_doi(2.0, 3.0)` cho **2,094551**.

## Điểm chính của bài

**Ba lỗi lộ ra theo đúng ba lần chạy của Mục 6.1.1.** Lần một không chạy dòng nào; lần hai chạy rồi dừng; lần ba chạy xong và cho số sai. Mỗi lần chạy sửa đúng một lỗi, và thứ tự ấy bắt buộc: không sửa lỗi cú pháp thì không chạy được để thấy hai lỗi kia.

**Lỗi dòng 13 đi xa hơn một chút lệch.** Đổi `<` thành `>` làm thuật toán chọn **nửa đoạn không chứa nghiệm** ở mỗi lượt, nên nó hội tụ về một đầu đoạn chứ không về nghiệm. Kết quả 0,147059 không gần 2,094551 chút nào — lệch hơn 14 lần. Nhưng chương trình vẫn chạy đủ 34 lượt và vẫn trả về một số thực hợp lệ, nên nếu không có giá trị mong đợi thì không có cách nào biết.

**Lỗi dòng 18 chỉ lộ ra ở một ca duy nhất.** Với đoạn [2, 3], `so_luot` bằng 34, nên `(a + b) / 34` cho một số sai nhưng **không** báo lỗi. Ngoại lệ chỉ xảy ra khi vòng lặp chạy 0 lượt, tức khi hai cận đã sát nhau hơn sai số — ca `chia_doi(2.0, 2.0)`.

Nghĩa là bộ ca chỉ có ca thường sẽ xếp lỗi dòng 18 vào loại **logic** chứ không phải thực thi, và xếp như vậy không sai từ góc nhìn của bộ ca ấy. Loại của một lỗi phụ thuộc dữ liệu đưa vào, không chỉ phụ thuộc dòng mã. Tệp kiểm chứng ghi cả hai biểu hiện bằng hai khẳng định riêng.

**Còn một lỗi thứ tư mà đề bài không nêu.** Cả bản sai lẫn bản đã sửa đều không kiểm `f(a) * f(b) < 0`. Gọi `chia_doi(0.0, 1.0)` trên đoạn không đổi dấu thì cả hai bản đều trả về một số mà không báo gì. Đó là nhóm lỗi thứ nhất của Mục 6.4.1, và nó là lý do hàm `chia_doi` của Mục 6.2.1 có thêm nhánh chặn ở đầu.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `chia_doi(2.0, 3.0)` | 2,094551 sau khi sửa đủ ba lỗi. Bản mới sửa lỗi cú pháp cho `0.147059` mà không báo gì |
| Biên | `chia_doi(2.0, 2.0)` | `ZeroDivisionError: float division by zero` ở dòng 18; ca **duy nhất** bộc lộ lỗi thực thi |
| Không hợp lệ | `chia_doi(0.0, 1.0)` | hàm không đổi dấu; cả hai bản đều trả về một số mà không báo gì — lỗi thứ tư, ngoài ba lỗi đề bài nêu |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
