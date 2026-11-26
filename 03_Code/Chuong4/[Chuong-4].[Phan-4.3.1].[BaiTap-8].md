# Lời giải Bài tập 4.8

- Chương 4, Mục 4.3.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.3.1].[BaiTap-8].py`
- Lời giải này không in vào giáo trình.

## Hàm sai

Hàm sai là `phan_loai`. Nhánh đầu viết `nhiet_do <= NGUONG[0]` thay vì `nhiet_do < NGUONG[0]`, nên số đo đúng bằng 60,0 °C bị xếp `binh thuong` thay vì `canh bao`.

## Bốn bộ ca kiểm thử

| Hàm | Ca thường | Ca biên | Ca ngoại lệ | Kết quả |
|---|---|---|---|---|
| `la_ket_thuc` | −1,0 cho đúng | −1,1 cho sai | 45,0 cho sai | đạt |
| `la_so_do_loi` | −5,0 cho đúng | −1,0 cho sai | 0,0 cho sai | đạt |
| `phan_loai` | 45,0 cho `binh thuong` | **60,0 cho `canh bao`** | 120,0 cho `dung may` | **không đạt** |
| `dem_trang_thai` | dãy có một số đo lỗi | dãy rỗng | dãy chỉ có giá trị kết thúc | đạt |

Ba bộ ca đạt, một bộ không đạt, nên hàm sai được khoanh vùng còn **một** hàm ngay từ lần chạy đầu.

## Điểm chính của bài

Số đo 60,0 °C là số đo duy nhất phân biệt hai bản của hàm `phan_loai`. Tệp kiểm chứng đo lại điều đó: `phan_loai_sai(59.9) == phan_loai(59.9)` và `phan_loai_sai(60.1) == phan_loai(60.1)`. Nhích một phần mười về bên nào cũng mất khả năng phân biệt.

Phát hiện quan trọng thứ hai là về **dữ liệu vào**, không về ca kiểm thử. Với dãy số đo của Bài tập 3.9 là 45 · 72,5 · 85 · −1, hai bản cho đúng cùng một kết quả cuối `(1, 1, 1, 0, 0)`. Lỗi không lộ ra chút nào, kể cả khi kiểm bằng mắt. Phải đổi dãy thành 45 · **60** · 85 · −1 thì kết quả cuối mới khác nhau: bản sai cho `(2, 0, 1, 0, 0)` còn bản đúng cho `(1, 1, 1, 0, 0)`.

Hai con số so sánh công soát:

| Cách kiểm | Số hàm phải soát bằng mắt |
|---|---|
| Chỉ kiểm kết quả cuối | 4 |
| Kiểm từng hàm bằng bộ ca riêng | 1 |

Tỉ lệ là 4 lần, và nó đúng bằng số hàm. Với một bộ mười hàm thì tỉ lệ là 10 lần. Đó là lý do tiêu chí thứ hai của Mục 1.2.1 — hàm phải kiểm riêng được — là tiêu chí quyết định: tách hàm mà không kiểm riêng được thì tỉ lệ này vẫn là 1.

Chi tiết cài đặt đáng ghi lại: hàm `dem_trang_thai` nhận hàm phân loại qua **tham số** thay vì gọi thẳng. Nhờ vậy cùng một hàm đếm chạy được với cả bản đúng lẫn bản sai, và so sánh hai kết quả cuối trở thành một lệnh `assert` thay vì hai lần sửa mã.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 45 · 60 · 85 · −1 | Bộ ca của `phan_loai` không đạt; ba bộ kia đạt |
| Biên | Số đo đúng bằng 60,0 | Ca duy nhất phát hiện lỗi; 59,9 và 60,1 cho cùng kết quả ở cả hai bản |
| Không hợp lệ | Chỉ kiểm kết quả cuối với dãy 45 · 72,5 · 85 · −1 | Hai bản cho cùng kết quả `(1, 1, 1, 0, 0)`; lỗi không lộ ra |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
