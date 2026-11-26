# Lời giải Bài tập 6.1

- Chương 6, Mục 6.1.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Bảng sáu thông báo

| STT | Thông báo | Loại | Nói được dòng sai | Mã lỗi gốc |
|---|---|---|---|---|
| 1 | `SyntaxError: expected ':'` | cú pháp | có | `L3.1-1` |
| 2 | `IndexError: list index out of range` | thực thi | có | `L5.1-1` |
| 3 | Chạy xong, in 75,0 kWh thay vì 60,0 kWh | **logic** | **không** | `L2.1-3` |
| 4 | `ValueError: could not convert string to float` | thực thi | có | `L2.3-2` |
| 5 | Không báo lỗi; chuỗi toàn số âm cho kết quả 0 | **logic** | **không** | `L5.1-5` |
| 6 | `UnboundLocalError: cannot access local variable` | thực thi | có | `L4.1-5` |

Một thông báo cú pháp, ba thông báo thực thi, hai thông báo logic.

## Điểm chính của bài

**Hai câu hỏi của đề bài hoá ra là một câu.** Tệp kiểm chứng ghi điều đó thành một khẳng định chạy trên cả sáu dòng: `(loai == "logic") == (not noi_duoc)`. Không dòng nào vi phạm.

Nghĩa là không cần phân loại rồi mới trả lời câu hỏi thứ hai, mà ngược lại: hỏi "thông báo này có chỉ được dòng sai không" trước, rồi loại lỗi suy ra ngay. Câu hỏi thứ hai dễ trả lời hơn hẳn, vì chỉ cần nhìn xem có chữ `line` hoặc một số dòng trong thông báo hay không.

**Thông báo 6 là chỗ dễ sai nhất.** `UnboundLocalError: cannot access local variable 'LAI_SUAT' where it is not associated with a value` nhắc tới một *khai báo*, nên nó trông giống lỗi cú pháp. Nhưng Python chỉ phát hiện ra nó **khi chạy tới dòng đọc biến**, nên nó là lỗi thực thi. Dấu hiệu phân biệt chắc chắn: lỗi cú pháp làm chương trình **không chạy dòng nào**, còn lỗi này xảy ra sau khi hàm đã bắt đầu chạy.

**Hai thông báo loại logic không phải là thông báo.** Dòng 3 và dòng 5 của bảng không phải là thứ Python in ra; chúng là **mô tả biểu hiện** mà người đọc phải tự viết sau khi so kết quả với giá trị mong đợi. Đó chính là nội dung của [[b-baloai]]: loại thứ ba không có thông báo nào, nên nó chỉ tồn tại khi có một kết quả mong đợi để so.

**Tỉ lệ ba loại trong sáu thông báo này không đại diện cho cả sách.** Sáu thông báo cho 1 · 3 · 2, tức lỗi thực thi chiếm nửa. Số đếm thật trên 69 mã lỗi Python của năm chương cho 14 · 22 · 33, tức lỗi logic chiếm 47,8 %. Sáu mẫu quá ít để kết luận về tỉ lệ; đó cũng là một bài học của chính bài tập này.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | thông báo 1 | cú pháp; có nói dòng, nhưng dòng nêu có thể là dòng kế sau dòng sai thật |
| Biên | thông báo 3 | logic; không nói dòng nào, vì không có thông báo nào |
| Không hợp lệ | thông báo 6 | thực thi; có nói dòng. Dễ nhầm thành cú pháp vì nó nhắc tới một khai báo |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
