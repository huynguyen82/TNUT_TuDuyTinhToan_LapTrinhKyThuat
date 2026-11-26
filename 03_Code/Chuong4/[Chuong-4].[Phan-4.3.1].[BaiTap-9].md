# Lời giải Bài tập 4.9

- Chương 4, cả năm tiểu mục · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.3.1].[BaiTap-9].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | `tien_vay` số thực, nghìn đồng, miền 1 000 đến 10 000 000; `lai_suat` số thực, miền 0 đến 0,05; `tien_tra` số thực, phải dương, không vượt tiền vay, và phải lớn hơn `tien_vay × lai_suat` |
| Xử lý | Chặn mọi dữ liệu vào; lặp theo tháng, mỗi tháng cộng lãi vào tổng rồi trừ tiền trả khỏi số dư, tới khi số dư không còn dương; tính khoản phải trả ở tháng cuối và quy khoản đó về giá trị hiện tại |
| Đầu ra | `so_thang` số nguyên; `tong_lai`, `tien_tra_thang_cuoi` và giá trị hiện tại, số thực hai chữ số thập phân, nghìn đồng |

## Năm hàm và việc của từng hàm

| Hàm | Việc | Kiểm riêng bằng |
|---|---|---|
| `kiem_du_lieu_vao` | chặn bốn loại dữ liệu vào không hợp lệ | bốn bộ dữ liệu, mỗi bộ vi phạm một điều kiện |
| `so_du_sau_mot_thang` | số dư sau một tháng | 500 000 · 0,008 · 25 000 cho 479 000 |
| `ky_han_va_tong_lai` | số tháng và tổng lãi cộng dồn | lãi suất 0 cho đúng 20 tháng |
| `gia_tri_hien_tai` | quy một dòng tiền về hiện tại | số kỳ 0 cho đúng giá trị tương lai |
| `tien_tra_thang_cuoi` | khoản phải trả ở tháng cuối | lãi suất 0 cho đúng 25 000 |

## Kết quả với bộ dữ liệu thường

| Đại lượng | Giá trị |
|---|---|
| Số tháng trả hết | 22 |
| Tổng lãi cộng dồn | `47041.27` nghìn đồng |
| Tiền trả tháng cuối | `22041.27` nghìn đồng |
| Giá trị hiện tại của khoản tháng cuối | `18497.16` nghìn đồng |

## Điểm chính của bài

Điều kiện chặn quan trọng nhất suy ra từ một câu hỏi duy nhất: tháng đầu, tiền trả có lớn hơn phần lãi phát sinh hay không. Nếu không, số dư tháng sau lớn hơn số dư tháng này, nên điều kiện `so_du > 0.0` không bao giờ sai và vòng lặp chạy mãi. Với tiền vay 500 000 nghìn đồng và lãi suất 0,008, lãi tháng đầu là 4 000 nghìn đồng; tiền trả 1 000 nghìn đồng rơi vào trường hợp này.

Điều kiện đó phải đặt **trước** vòng lặp, không trong vòng lặp. Trong vòng lặp thì nó kiểm lại cùng một thứ mỗi lượt, và với một khoản vay không trả hết được thì không có lượt nào để kiểm — chương trình đã treo.

Tổng lãi là chỗ dễ sai nhất của bài, và Bài gỡ lỗi GL4 cài đúng lỗi này. Lãi phải tính trên **số dư còn lại của từng tháng**, nên phải cộng dồn trong vòng lặp. Tính theo lãi đơn trên tiền vay gốc, tức `tien_vay × lai_suat × so_thang`, cho 88 000 nghìn đồng — gần gấp đôi con số đúng 47 041,27 — và không thông báo nào xuất hiện, vì công thức hợp lệ về cú pháp và cho ra một số có vẻ hợp lý.

Tháng cuối trả 22 041,27 nghìn đồng, ít hơn 25 000 nghìn đồng, vì nợ còn lại nhỏ hơn khoản trả hằng tháng. Tệp kiểm chứng khẳng định `cuoi <= 25000.0`: đây là một tính chất của bài toán, kiểm được mà không cần biết thuật toán bên trong.

Ca biên lãi suất bằng 0 cho ba tính chất kiểm nhẩm được cùng lúc: 20 tháng đúng bằng 500 000 chia 25 000; tổng lãi bằng 0; và tháng cuối trả đúng 25 000. Một ca cho ba khẳng định độc lập là ca có giá trị cao.

Không hàm nào đọc biến toàn cục ngoài hai hằng số miền viết hoa, đúng yêu cầu của đề bài. Nhờ vậy cả năm hàm kiểm riêng được, và tệp kiểm chứng có 13 khẳng định chia đủ ba nhóm.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 500 000 · 0,008 · 25 000 | 22 tháng; tổng lãi `47041.27`; tháng cuối `22041.27` |
| Biên | 500 000 · 0,0 · 25 000 | 20 tháng; tổng lãi `0.00`; tháng cuối `25000.00` |
| Không hợp lệ | 500 000 · 0,008 · 1 000 | `ValueError`; lãi tháng đầu 4 000 lớn hơn tiền trả 1 000 |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
