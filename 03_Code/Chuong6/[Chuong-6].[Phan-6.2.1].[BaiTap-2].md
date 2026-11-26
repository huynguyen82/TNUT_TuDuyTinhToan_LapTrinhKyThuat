# Lời giải Bài tập 6.2

- Chương 6, Mục 6.2.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.2.1].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Xếp loại bốn ca

| Ca | Dữ liệu vào | Loại | Lý do |
|---|---|---|---|
| `ca_a` | 100 000, 10 năm | thường | giá trị giữa miền, không gần mốc nào |
| `ca_b` | 100 000, 5 năm | thường | cũng là giá trị giữa miền; **không** phải loại khác |
| `ca_c` | 100 000, 1 năm | biên | 1 là mốc dưới của miền số năm |
| `ca_d` | 0, 10 năm | biên | 0 là mốc dưới của miền nguyên giá |

**Loại ca còn thiếu: dữ liệu không hợp lệ.** Không ca nào trong bốn ca truyền một giá trị ngoài miền đặc tả cho phép.

## Nhánh chưa ca nào đi qua

Số đo của tệp kiểm chứng, đếm bằng `sys.settrace`:

| Bộ ca | Số dòng đi qua | Dòng chưa chạy |
|---|---|---|
| Một ca thường | 5 trên 7 | dòng 21 và 23 |
| Bốn ca của đề bài | 5 trên 7 | dòng 21 và 23 |
| Thêm hai ca không hợp lệ | 7 trên 7 | không |

Hai dòng chưa chạy là hai dòng `return []`: một cho `so_nam <= 0`, một cho `nguyen_gia < 0.0`. Cả hai là nhánh chặn dữ liệu không hợp lệ.

## Điểm chính của bài

**Bốn ca của đề bài phủ đúng bằng một ca.** Tệp kiểm chứng ghi điều đó thành một khẳng định trực tiếp: tập dòng mà `[(100000.0, 10)]` đi qua **bằng** tập dòng mà `[(100000.0, 10), (100000.0, 5)]` đi qua. Hai ca thường khác giá trị không phủ thêm dòng nào.

Đây là lỗi `L6.2-1` của [[b-loi621]] ở dạng cụ thể: ba hay bốn giá trị khác nhau không có nghĩa là ba hay bốn loại ca. Cách duy nhất biết chắc là phân loại từng ca theo [[b-baloaica]] trước khi tính là đủ.

**Hai ca biên của đề bài có ích, nhưng không chạm vào nhánh chặn.** `ca_c` với 1 năm và `ca_d` với nguyên giá 0 đều nằm **trong** miền hợp lệ — 1 là số năm hợp lệ, 0 là nguyên giá hợp lệ. Chúng là ca biên thật, nhưng chúng đi qua đúng đường mà ca thường đã đi.

Hai ca thiếu là hai ca **nhích qua mốc**: số năm 0 (nhích qua mốc dưới của miền số năm) và nguyên giá −5 000 (nhích qua mốc dưới của miền nguyên giá). Đúng quy tắc hai ca cho một mốc của Bài tập 4.6: ca tại mốc đã có, ca nhích qua mốc thì chưa.

**Hai dòng không chạy là hai dòng duy nhất không ai kiểm.** Nếu nhánh chặn viết sai — chẳng hạn `if so_nam < 0` thay vì `<= 0` — thì bốn ca của đề bài vẫn đạt hết, và hàm gọi với số năm bằng 0 sẽ cho `ZeroDivisionError` chứ không trả về danh sách rỗng. Bốn ca không nói gì về chuyện đó.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `ca_a` và `ca_b` | cả hai là ca thường; hai ca khác giá trị không thành hai loại ca, và không phủ thêm dòng nào |
| Biên | `ca_c`, số năm bằng 1 | ca biên tại mốc dưới của miền số năm; vẫn đi đúng đường của ca thường |
| Không hợp lệ | bốn ca cộng lại | thiếu hẳn loại ca dữ liệu không hợp lệ; hai dòng `return []` chưa ca nào chạy |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
