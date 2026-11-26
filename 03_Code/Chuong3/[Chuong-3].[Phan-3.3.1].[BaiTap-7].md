# Lời giải Bài tập 3.7

- Chương 3, Mục 3.3.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.3.1].[BaiTap-7].py`
- Lời giải này không in vào giáo trình. Bài mức 3 có nhiều cách lý giải đúng.

## Ca kiểm thử đã chọn: `n` = 1

| `n` | `range(1, n)` | `range(1, n + 1)` | Kết quả đúng | Tỉ lệ chênh |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 % |
| **1** | **0** | **1** | **1** | **100 %** |
| 3 | 3 | 6 | 6 | 50 % |
| 10 | 45 | 55 | 55 | 18,2 % |
| 100 | 4 950 | 5 050 | 5 050 | 1,98 % |

Kết luận: đoạn dùng `range(1, n)` **sai**, vì nó bỏ sót phần tử cuối.

## Cách lập kết quả đúng

Kết quả đúng tính bằng công thức `n(n + 1)/2`, **không** tính bằng cách chạy một trong hai đoạn mã. Đây là bước 1 của quy trình truy vết đối chiếu ở Mục 1.5.1: bảng giá trị mong đợi lập từ đặc tả, không lập từ chương trình cần kiểm. Lập từ chương trình thì hai bảng luôn trùng nhau và quy trình không bao giờ tìm ra lỗi.

## Hai bảng vết ở ca `n` = 1

| Lượt | `range(1, 1)` | `range(1, 2)` |
|---|---|---|
| trước vòng lặp | `tong` = 0 | `tong` = 0 |
| 1 | không chạy lượt nào | `chi_so` = 1, `tong` = 1 |
| kết quả | 0 | 1 |

Vòng lặp thứ nhất chạy **0 lượt**, vì `range(1, 1)` là dãy rỗng. Đó là lý do ca này phân biệt rõ nhất: một đoạn làm việc, đoạn kia không làm gì cả.

## Vì sao `n` = 100 không phân biệt được

Chênh lệch giữa hai đoạn luôn đúng bằng `n`, tức bằng phần tử bị bỏ sót. Nhưng kết quả đúng tăng theo `n²`, nên tỉ lệ chênh giảm như `2/(n+1)`. Ở `n` = 100 tỉ lệ đó còn 1,98 %, và 4 950 với 5 050 đều là những con số trông hợp lý cho bài toán.

Nguyên tắc rút ra, ngược với trực giác: **dữ liệu lớn hơn kiểm kém hơn** với loại lỗi này. Tệp kiểm chứng khẳng định tỉ lệ chênh giảm đơn điệu khi `n` tăng.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `n` = 1 | 0 và 1; chênh lệch chiếm 100 % |
| Biên | `n` = 0 | Cả hai cho 0; ca này **không** phân biệt được, nên không dùng làm ca duy nhất |
| Không hợp lệ | `n` = 100 | 4 950 và 5 050; chênh dưới 2 %, không phân biệt được bằng mắt |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
