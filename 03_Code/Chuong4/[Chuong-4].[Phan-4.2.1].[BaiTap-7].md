# Lời giải Bài tập 4.7

- Chương 4, Mục 4.2.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.2.1].[BaiTap-7].py`
- Lời giải này không in vào giáo trình.

## Bảng áp ba tiêu chí cho bốn hàm

| Hàm | Tiêu chí 1: đầu vào và đầu ra một câu | Tiêu chí 2: kiểm riêng bằng | Tiêu chí 3: động từ và danh từ |
|---|---|---|---|
| `doc_kich_thuoc` | nhận một chuỗi, trả một số thực | chuỗi `"50.03"` và chuỗi `"50,03"` | đọc · kích thước |
| `dat_dung_sai` | nhận một kích thước, trả đúng hoặc sai | 50,03 · 50,05 · 50,06 | đạt · dung sai |
| `kich_thuoc_trung_binh` | nhận tổng và số chi tiết, trả một số thực | tổng 50,05 với 1 chi tiết; 0 chi tiết | tính · kích thước trung bình |
| `gom_ket_qua` | nhận số chi tiết và nguồn dữ liệu, trả số đạt và trung bình | ba kích thước của Bài tập 3.5 | gom · kết quả |

Cột thứ hai là cột quyết định. Mỗi hàm điền được cột đó bằng một bộ dữ liệu nhỏ, và không bộ nào cần chạy ba hàm kia.

## Kết quả

| Bộ dữ liệu | Số chi tiết đạt | Trung bình | Đối chiếu Bài tập 3.5 |
|---|---|---|---|
| 3 kích thước 50.03 · 49.97 · 50.01 | 3 | `50.00` mm | trùng |
| 1 kích thước 50.05 | 1 | `50.05` mm | trùng |

## Điểm chính của bài

Chỗ khó nhất của bài không phải việc viết bốn hàm, mà việc làm cho hàm thứ tư kiểm được. Hàm `gom_ket_qua` phải đọc dữ liệu vào, mà dữ liệu vào trong Bài tập 3.5 đến từ bàn phím. Hàm nào đọc bàn phím thì không kiểm được bằng `assert`: mỗi lần chạy ca kiểm thử lại phải có người gõ.

Lời giải giải chỗ này bằng cách cho `gom_ket_qua` nhận **một hàm** làm tham số: tham số `doc_mot_dong` cấp một kích thước cho mỗi lượt. Khi chạy thật, truyền vào một hàm gọi `input`; khi kiểm, truyền vào một hàm đọc từ một bộ dữ liệu cố định. Thân hàm `gom_ket_qua` không đổi một dòng nào giữa hai trường hợp.

Đây là trừu tượng hoá của Mục 1.2.2 áp vào mã nguồn: phần chung là vòng lặp và phép đếm, phần khác nhau là nguồn dữ liệu, nên phần khác nhau trở thành một tham số.

Phép chặn đặt ở hàm `kich_thuoc_trung_binh`, không ở hàm `gom_ket_qua`. Lý do: phép chia là chỗ **có thể** gặp số 0, nên phép chặn thuộc về hàm chứa phép chia. Đặt ở hàm gom thì mỗi chỗ gọi hàm tính trung bình lại phải tự chặn một lần.

Hai ca ngoại lệ của bài thuộc **hai hàm khác nhau**: chuỗi dùng dấu phẩy bị hàm `doc_kich_thuoc` chặn, còn 0 chi tiết bị hàm `kich_thuoc_trung_binh` chặn. Đó chính là cái mà việc tách hàm mua được: hai lỗi khác nhau hiện ra ở hai chỗ khác nhau, nên khoanh vùng được ngay.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 3 và 50.03 · 49.97 · 50.01 | 3 đạt; `50.00`; trùng Bài tập 3.5 |
| Biên | 1 và 50.05 | 1 đạt; `50.05`; hàm trung bình chạy đúng với một phần tử |
| Không hợp lệ | 0 chi tiết | `ValueError` từ `kich_thuoc_trung_binh`, trước khi chia |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
