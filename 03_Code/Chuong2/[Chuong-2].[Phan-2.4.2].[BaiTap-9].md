# Lời giải Bài tập 2.9

- Chương 2, Mục 1.1.1 và cả sáu tiểu mục Chương 2 · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.4.2].[BaiTap-9].py`
- Lời giải này không in vào giáo trình. Bài mức 4 có nhiều cách tổ chức đúng.

## 1. Bảng đặc tả ba phần

Lập trước khi viết dòng mã đầu tiên, theo trình tự đầu ra trước của Mục 1.1.1.

| Phần | Tên | Ý nghĩa, đơn vị, định dạng | Miền giá trị và trường hợp đặc biệt |
|---|---|---|---|
| Đầu ra | `so_dat` | Số chi tiết đạt, số nguyên | Từ 0 đến số chi tiết |
| Đầu ra | `trung_binh` | Kích thước trung bình, mm, hai chữ số thập phân | Luôn tính được khi số chi tiết lớn hơn 0 |
| Đầu ra | `tuong_doi` | Sai số tương đối của trung bình so với danh nghĩa, ký hiệu khoa học hai chữ số | Bằng 0 khi trung bình đúng bằng danh nghĩa |
| Đầu vào | `danh_nghia` | Kích thước danh nghĩa, mm | Phải khác 0, vì là mẫu số của sai số tương đối |
| Đầu vào | `dung_sai` | Dung sai, mm | Không âm |
| Đầu vào | `cac_chuoi_do` | Kích thước đo được, chuỗi | Số phần tử từ 1 đến 100; chuỗi không ép kiểu được thì báo dữ liệu không hợp lệ kèm số thứ tự |
| Bước xử lý | Bước 1 | Kiểm số chi tiết theo miền | Không sinh đại lượng mới |
| Bước xử lý | Bước 2 | Với từng chi tiết: ép kiểu, cộng dồn vào tổng, đếm nếu đạt | Sinh `tong` và `so_dat` |
| Bước xử lý | Bước 3 | Tính trung bình và sai số tương đối | Sinh `trung_binh` và `tuong_doi` |

## 2. Chọn phép so sánh ở bước kết luận

Dùng `math.isclose` với `rel_tol=0.0` và `abs_tol=dung_sai`. Lý do theo quy tắc hai câu hỏi của Bài tập 2.8: hai giá trị là số thực, và bài toán đã cho sẵn một dung sai tuyệt đối. Đặt `rel_tol=0.0` để ngưỡng tương đối mặc định không can thiệp.

Viết `can_duoi <= x <= can_tren` cũng cho kết quả đúng với dữ liệu của đề bài. Chọn `math.isclose` vì nó nói thẳng ý định là *so với dung sai*, và vì hai cận tính bằng phép cộng trừ số thực nên bản thân chúng đã mang sai số biểu diễn.

## 3. Chỗ dễ sai nhất: cộng dồn trên giá trị nào

Phải cộng dồn trên **giá trị gốc**, không trên giá trị đã làm tròn để in. Cộng dồn trên giá trị đã làm tròn là lỗi `L2.3-3` của Mục 2.3.1.

Tệp kiểm chứng khẳng định hai cách cho kết quả khác nhau trên chính bộ dữ liệu của đề bài: cộng dồn trên giá trị gốc cho trung bình 50,00333333333333, còn cộng dồn sau khi làm tròn một chữ số thập phân cho một con số khác.

## 4. Đáp số

Với danh nghĩa 50,00 mm, dung sai 0,05 mm và ba chi tiết 50,03 · 49,97 · 50,01:

| Đầu ra | Giá trị thật | In ra |
|---|---|---|
| Số chi tiết đạt | 3 | `3` |
| Kích thước trung bình | 50,00333333333333 mm | `50.00` |
| Sai số tương đối | 6,666666666 × 10⁻⁵ | `6.67e-05` |

Điểm đáng chú ý: trung bình in ra `50.00` trông như đúng bằng danh nghĩa, nhưng sai số tương đối 6,67 × 10⁻⁵ cho thấy nó không bằng. Đây là lý do phiếu in cả hai: con số đã làm tròn để đọc, và sai số để biết con số đó đã bị làm tròn bao nhiêu.

## 5. Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 50.00, 0.05, ba chi tiết 50.03 · 49.97 · 50.01 | 3 đạt; `50.00`; 6,67 × 10⁻⁵ |
| Biên | Một chi tiết duy nhất 50.05 | 1 đạt; `50.05`; cận trên thuộc miền |
| Không hợp lệ | Số chi tiết bằng 0 | Báo dữ liệu không hợp lệ ở bước 1, trước khi chia |

Ba bộ biên nữa đã kiểm: chi tiết 50,06 không đạt nhưng vẫn vào trung bình; hai chi tiết 49,95 và 50,05 cho trung bình đúng bằng danh nghĩa nên sai số tương đối bằng 0; và 100 chi tiết vẫn nằm trong miền.

## 6. Nối tiếp sang Chương 3

Chương trình này nhận từng chi tiết một. Chương 3 thay phần nhập lặp lại bằng một vòng lặp, và Chương 5 thay bằng đọc tệp số liệu. Bảng đặc tả ở phần 1 không đổi qua cả ba chương; chỉ phần bước xử lý thứ hai đổi cách thực hiện.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
