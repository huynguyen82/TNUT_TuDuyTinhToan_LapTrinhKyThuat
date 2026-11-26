# Lời giải Bài tập 6.7

- Chương 6, Mục 6.2.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.2.1].[BaiTap-7].py`
- Lời giải này không in vào giáo trình.

## Bước 1 — bảng đặc tả ba phần, lập trước khi viết mã

| Phần | Nội dung |
|---|---|
| Đầu vào | điểm đầu `x0` kiểu số thực |
| Xử lý | lặp `x = x − f(x)/f'(x)` tới khi bước nhảy nhỏ hơn sai số 10⁻¹⁰; chặn trước khi `f'(x)` bằng 0 |
| Đầu ra | `(nghiệm, số lượt lặp)`, hoặc giá trị quy ước −1,0 và −1 khi không tính được |

## Bước 2 và 3 — miền đầu vào, mốc, và ba ca

| Miền hoặc mốc | Loại ca | Dữ liệu vào | Kết quả mong đợi | Nguồn |
|---|---|---|---|---|
| giữa miền | thường | `x0` = 3,0 | nghiệm 2,0945514815; số lượt trong 1 tới 10 | nghiệm từ **phép chia đôi**; khoảng số lượt từ tính chất hội tụ bình phương |
| mốc: đạo hàm bằng 0 | biên | `x0` = √(2/3) ≈ 0,8165 | giá trị quy ước −1,0 | dòng điều kiện áp dụng của đặc tả |
| mốc: `x0` đúng bằng nghiệm | biên | `x0` = 2,0945514815 | dừng sau đúng **1** lượt | định nghĩa của nghiệm |

Không nguồn nào trong cột cuối là hàm Newton. Đó là bước 4 của [[b-bonbuoc]].

## Ba lỗi cài sẵn và kết quả hai bộ ca

Ba lỗi này khác ba lỗi của Ví dụ 6.4, theo yêu cầu của đề bài.

| Bản | Chỗ sai | Bộ ca viết sau mã | Bộ ca thiết kế trước |
|---|---|---|---|
| Bản đúng | không có | đạt | đạt |
| Lỗi A | `f_dao_ham(x_cu + 1.0)` thay vì `f_dao_ham(x_cu)` | không bắt được | **bắt được** |
| Lỗi B | chặn đạo hàm bằng 0 nhưng trả về `x_cu` thay vì giá trị quy ước | không bắt được | **bắt được** |
| Lỗi C | tiêu chí dừng so `abs(f(x_moi))` với 1,0 thay vì so bước nhảy với sai số | không bắt được | **bắt được** |
| **Tổng** | | **0 trên 3** | **3 trên 3** |

## Điểm chính của bài

**Ba lỗi, ba ca bắt, không ca nào thừa.** Lỗi A sai ở nghiệm nên ca thường bắt được. Lỗi B trả về một con số thay vì giá trị quy ước, nên chỉ ca biên đạo hàm bằng 0 bắt được. Lỗi C dừng quá sớm nên số lượt sai, và ca `x0` đúng bằng nghiệm bắt được nó rõ nhất. Bỏ bất kỳ ca nào thì một lỗi lọt.

**Lỗi B là lỗi đáng chú ý nhất.** Nó **có** nhánh chặn — dòng `if d == 0.0` nằm đúng chỗ — nhưng thân nhánh trả về `x_cu`, tức điểm đầu, như thể đó là nghiệm. Đọc mã thì thấy hàm đã kiểm điều kiện áp dụng, nên nó trông đúng hơn cả bản không kiểm gì. Chỉ một ca ghi rõ **giá trị mong đợi của nhánh chặn** mới phân biệt được. Đó là lỗi `L6.2-3` của [[b-loi621]] ở dạng người viết mã mắc phải thay vì người viết ca.

**Lỗi C cho một nghiệm trông rất đúng.** Tiêu chí `abs(f(x_moi)) <= 1.0` dừng khi giá trị hàm nhỏ, không khi bước nhảy nhỏ. Với `x0` = 3,0 nó dừng sớm hơn vài lượt và cho một số gần nghiệm. Ca thường với khoảng số lượt 1–10 không bắt được, vì số lượt vẫn nằm trong khoảng. Cái bắt được nó là ca `x0` đúng bằng nghiệm: bản đúng dừng sau 1 lượt, bản lỗi C cũng dừng sau 1 lượt nhưng trả về một điểm đã dịch đi.

**Bộ ca viết sau mã bắt 0 trên 3, giống hệt Ví dụ 6.4.** Hai lần đo trên hai bộ lỗi khác nhau cho cùng một kết quả. Lý do không phải là ba lỗi quá tinh vi, mà là bộ ca ấy **không kiểm gì**: khẳng định `nghiem == nghiem` luôn đúng với mọi hàm, kể cả hàm trả về một hằng số.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | điểm đầu 3,0 | nghiệm 2,0945514815 sau 6 lượt; chia đôi cần 34 lượt cho cùng sai số |
| Biên | điểm đầu đúng bằng nghiệm | dừng sau đúng 1 lượt; ca này bắt được lỗi C |
| Không hợp lệ | điểm đầu làm đạo hàm bằng 0 | báo không tính được; ca này bắt được lỗi B |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
