# Lời giải Bài tập 4.4

- Chương 4, Mục 4.1.3 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.1.3].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | `gia_tri_tuong_lai` số thực, nghìn đồng; `so_ky` số nguyên, miền 0 đến 600; `lai_suat` số thực tuỳ chọn, miền 0 đến 0,05, mặc định 0,008 |
| Xử lý | Chặn `so_ky` và `lai_suat` ngoài miền, rồi tính `gia_tri_tuong_lai / (1 + lai_suat) ** so_ky` |
| Đầu ra | Số thực, hai chữ số thập phân, nghìn đồng |

## Ba cách gọi và kết quả

| Cách gọi | Dòng mã | Kết quả |
|---|---|---|
| Bỏ qua tham số có mặc định | `gia_tri_hien_tai(100000.0, 12)` | `90881.11` |
| Truyền theo thứ tự | `gia_tri_hien_tai(100000.0, 12, 0.008)` | `90881.11` |
| Truyền theo tên | `gia_tri_hien_tai(100000.0, 12, lai_suat=0.008)` | `90881.11` |

Ba cách cho đúng cùng một giá trị, và tệp kiểm chứng khẳng định điều đó bằng một lệnh `assert` so cả ba.

## Điểm chính của bài

Thứ tự tham số là bắt buộc, không phải lựa chọn: `lai_suat` có giá trị mặc định nên phải đứng **sau** `so_ky`. Đặt ngược lại thì Python báo `SyntaxError: parameter without a default follows parameter with a default` ngay khi đọc tệp.

Ba cách gọi khác nhau về chỗ khác: cách thứ ba đọc rõ nhất ở những chỗ giá trị lãi suất thật sự quan trọng, chẳng hạn khi so hai phương án đầu tư. Cách thứ nhất ngắn nhất, nhưng nó **che** mất việc thiếu đối số. Nếu so hai phương án mà quên truyền lãi suất cho một phương án, cả hai cùng dùng 0,008, hai kết quả bằng nhau, và người đọc kết luận hai phương án như nhau — không thông báo nào xuất hiện.

Ca ngoại lệ đáng chú ý nhất là số kỳ âm. Không chặn thì công thức vẫn chạy: `100000 / (1 + 0.008) ** -3` cho một số **lớn hơn** 100 000 nghìn đồng. Về toán thì đúng — đó là giá trị tương lai, không phải giá trị hiện tại — nhưng về nghĩa của bài toán thì vô lý, vì giá trị hiện tại của một dòng tiền tương lai không thể lớn hơn chính nó khi lãi suất dương. Tệp kiểm chứng đo lại điều này bằng một khẳng định riêng.

Ca biên lãi suất bằng 0 cho một tính chất kiểm nhẩm được: không chiết khấu thì mọi số kỳ đều cho đúng giá trị tương lai, kể cả 600 kỳ.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 100 000 sau 12 kỳ, lãi suất mặc định | `90881.11` |
| Biên | 100 000 sau 0 kỳ | `100000.00` |
| Không hợp lệ | 100 000 sau −3 kỳ | `ValueError`; không chặn thì ra số lớn hơn 100 000 |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
