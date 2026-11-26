# Lời giải Bài tập 3.5

- Chương 3, Mục 3.2.1 · Mức 2 · 30 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.2.1].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Thay đổi so với Bài tập 2.9

Bài tập 2.9 nhận từng chi tiết bằng một khối lệnh chép lại. Bài này thay bằng một vòng lặp `for` chạy `range(so_chi_tiet)`.

| Tiêu chí | Bài tập 2.9 | Bài tập 3.5 |
|---|---|---|
| Số dòng mã với 3 chi tiết | khoảng 12 | khoảng 12 |
| Số dòng mã với 300 chi tiết | khoảng 1 200 | khoảng 12 |
| Đáp số trên cùng bộ dữ liệu | 3 đạt, trung bình 50,00333333333333 | **trùng khớp** |

Dòng cuối là yêu cầu của đề bài và cũng là phép kiểm tốt nhất của bài này: hai chương trình viết bằng hai cấu trúc khác nhau phải cho cùng một đáp số trên cùng dữ liệu. Tệp kiểm chứng khẳng định đúng giá trị 50,00333333333333 đã chốt ở Chương 2.

## Hai điểm giữ nguyên từ Chương 2

**Cộng dồn trên giá trị gốc.** Vẫn phải cộng kích thước gốc, không cộng giá trị đã làm tròn để in; đây là lỗi `L2.3-3`.

**Chọn phép so sánh.** Vẫn dùng `math.isclose` với `rel_tol=0.0` và `abs_tol` lấy đúng bằng dung sai, theo quy tắc hai câu hỏi của Bài tập 2.8.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 3 chi tiết 50.03 · 49.97 · 50.01 | 3 đạt; trung bình `50.00`; trùng Bài tập 2.9 |
| Biên | 1 chi tiết 50.05 | 1 đạt; trung bình `50.05` |
| Không hợp lệ | 0 chi tiết | Báo dữ liệu không hợp lệ trước khi chia |

Hai ca nữa đã kiểm: 50.06 không đạt nhưng vẫn vào trung bình, và 100 chi tiết vẫn trong miền. Tệp kiểm chứng còn khẳng định vòng lặp chạy đúng số chi tiết lượt, không thừa không thiếu.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
