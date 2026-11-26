# Lời giải Bài gỡ lỗi GL4

- Chương 4 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-4].[GoLoi-4].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo hoặc biểu hiện | Cách sửa |
|---|---|---|---|---|
| 4 | cú pháp | `def so_du_sau_mot_thang(so_du, lai_suat, tien_tra)` thiếu dấu hai chấm | `SyntaxError: expected ':'` | Thêm dấu hai chấm |
| 18 | thực thi | `so_du_sau_mot_thang(so_du, LAI_SUAT)` thiếu đối số thứ ba | `TypeError: so_du_sau_mot_thang() missing 1 required positional argument: 'tien_tra'` | Truyền đủ ba đối số |
| 11 | logic | `return tien_vay * LAI_SUAT * so_thang` | **không có**; cho 88 000,00 thay vì 47 041,27 nghìn đồng | Cộng dồn lãi thật của từng tháng trong chính vòng lặp |

Sau khi sửa đủ ba lỗi, vay 500 000 nghìn đồng trả hết sau **22 tháng** với tổng lãi **47 041,27 nghìn đồng**.

## Điểm chính của bài

**Lỗi dòng 11 sai gần gấp đôi mà vẫn trông hợp lý.** Công thức `tien_vay × LAI_SUAT × so_thang` tính lãi như thể dư nợ không giảm suốt 22 tháng. Thực tế dư nợ giảm dần, nên lãi thật nhỏ hơn.

| Cách tính | Tổng lãi (nghìn đồng) | Sai lệch |
|---|---|---|
| Bản còn lỗi dòng 11 | 88 000,00 | +87,1 % |
| Bản đúng | 47 041,27 | — |

Con số 88 000 không vô lý: nó nhỏ hơn tiền vay, nó dương, nó cùng bậc độ lớn với lãi thật. Người đọc báo cáo không có cách nào bác nó nếu không tự tính lại.

**Ca biên 24 000 nghìn đồng KHÔNG bộc lộ lỗi dòng 11.** Đây là phát hiện đáng giá nhất của bài. Với `so_thang = 1`, hai công thức cho **đúng cùng một số**: 192,00 nghìn đồng. Tệp kiểm chứng ghi cả hai con số cạnh nhau để thấy rõ điều đó.

Lý do: lãi tháng đầu bao giờ cũng tính trên đúng tiền vay gốc, nên hai cách trùng nhau ở tháng thứ nhất và chỉ tách ra từ tháng thứ hai.

Hệ quả cho việc thiết kế bộ ca kiểm thử: **ca biên nhỏ nhất không phải lúc nào cũng là ca tốt nhất**. Ca `so_thang = 1` bộc lộ rất tốt lỗi lệch một ở biến đếm, nhưng che hoàn toàn lỗi công thức lãi. Cần cả hai loại ca, và cần biết ca nào phủ lỗi nào. Đây là nội dung Mục 6.2.1 về việc bộ ba loại ca vẫn chưa đủ.

**Lỗi dòng 18 là lỗi mà giá trị mặc định có thể che đi.** Hàm khai báo ba tham số không có giá trị mặc định, nên thiếu một đối số thì `TypeError` nổ ngay — may mắn. Nếu `tien_tra` có giá trị mặc định, lời gọi thiếu đối số sẽ **chạy bình thường** với một giá trị không ai định truyền. Đó chính là lỗi `L4.1-9` của Mục 4.1.3.

**Ca không hợp lệ chỉ ra một điều kiện mà đề bài không nói.** Vay 5 000 000 nghìn đồng thì lãi tháng đầu là 40 000, lớn hơn tiền trả 25 000, nên dư nợ **tăng** mỗi tháng và vòng lặp `while so_du > 0` chạy mãi. Bản đã sửa chặn trước vòng lặp bằng một phép so, và thông điệp lỗi nêu cả hai con số để người đọc biết ngay vì sao.

Đây là cách viết thông điệp mà Mục 6.3.1 yêu cầu: nêu giá trị gây lỗi, không chỉ nêu có lỗi.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 500 000 nghìn đồng | 22 tháng; tổng lãi `47041.27`. Bản còn lỗi cho `88000.00` |
| Biên | 24 000 nghìn đồng | 1 tháng; tổng lãi `192.00`. Hai bản cho **cùng** một số, nên ca này không bộc lộ lỗi dòng 11 |
| Không hợp lệ | 5 000 000 nghìn đồng | Lãi tháng đầu 40 000 lớn hơn tiền trả 25 000; phải chặn trước vòng lặp thay vì chạy mãi |
