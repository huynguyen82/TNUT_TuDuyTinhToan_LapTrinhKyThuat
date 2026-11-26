# Lời giải Bài tập 1.4

- Chương 1, Mục 1.3.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.3.1].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Lưu đồ lời giải

Bảy khối, theo đúng bảng đặc tả của Bài tập 1.3.

| Thứ tự | Khối | Hình dạng | Nội dung |
|---|---|---|---|
| 1 | `bat_dau` | Bầu dục | Bắt đầu |
| 2 | `nhap` | Bình hành | Nhập `I` (A), `R` (Ω/km), `L` (km) |
| 3 | `kiem_dau_vao` | Thoi | Ba đầu vào đều trong miền? |
| 4 | `tinh_ton_that` | Chữ nhật | `ton_that = I² × R × L` |
| 5 | `xuat_ket_qua` | Bình hành | Xuất `ton_that` (W, hai chữ số thập phân) |
| 6 | `xuat_loi` | Bình hành | Xuất: dữ liệu không hợp lệ |
| 7 | `ket_thuc` | Bầu dục | Kết thúc |

Các mũi tên: 1→2, 2→3, 3→4 nhãn `Đúng`, 3→6 nhãn `Sai`, 4→5, 5→7, 6→7.

## Hai chỗ dễ sai

**Nhánh `Sai` cũng phải dẫn tới khối kết thúc.** Bài làm nào để nhánh `Sai` kết thúc ở khối `xuat_loi` mà không nối tiếp tới khối kết thúc thì vi phạm quy tắc 2, dù hình vẽ trông đã đủ ý.

**Khối kiểm đặt trước khối tính.** Đây là yêu cầu của đề bài và là điểm chính của bài tập. Đáng chú ý: lưu đồ đặt khối kiểm **sau** khối tính vẫn thoả cả năm quy tắc nối, nên bộ kiểm quy tắc không bắt được lỗi này. Chỉ việc truy vết đường đi mới cho thấy phép tính đã chạy trên dữ liệu chưa kiểm. Tệp kiểm chứng khẳng định đúng điều đó, và đây là một ví dụ sớm cho ý của Mục 1.5.1: hợp lệ về hình thức không có nghĩa là đúng.

## Ba đường đi đã kiểm bằng máy

| Dữ liệu vào | Đường đi qua các khối | Đầu ra |
|---|---|---|
| `I` = 50 A, `R` = 0,25 Ω/km, `L` = 1,2 km | `bat_dau` → `nhap` → `kiem_dau_vao` → `tinh_ton_that` → `xuat_ket_qua` → `ket_thuc` | `750.00` |
| `L` = 0 km | như trên, vẫn đi nhánh `Đúng` | `0.00` |
| `I` = −10 A | `bat_dau` → `nhap` → `kiem_dau_vao` → `xuat_loi` → `ket_thuc` | dữ liệu không hợp lệ |

Dòng thứ hai là chỗ hay bị làm sai: chiều dài bằng 0 là giá trị **hợp lệ** ở cận dưới của miền, nên phải đi nhánh `Đúng` và cho ra 0,00 W, chứ không phải đi nhánh `Sai`.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Lưu đồ cho đúng ba đầu ra ứng với ba bộ dữ liệu kiểm thử | 5,0 |
| Khối kiểm đặt trước khối tính, và nhánh `Sai` dẫn tới khối kết thúc | 2,5 |
| Dùng đúng hình dạng khối và thoả cả năm quy tắc nối | 1,5 |
| Đặt tên khối mang nghĩa | 1,0 |
