# Lời giải Bài tập 4.3

- Chương 4, Mục 4.1.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.1.1].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | `so_du` số thực, nghìn đồng, miền 0 đến 10 000 000; `lai_suat` số thực, miền 0 đến 0,05; `tien_tra` số thực, phải lớn hơn `so_du × lai_suat` |
| Xử lý | Chặn dữ liệu ngoài miền, rồi tính `so_du × (1 + lai_suat) − tien_tra`; gọi lại hàm ba lần, mỗi lần truyền kết quả lần trước |
| Đầu ra | Ba số thực, hai chữ số thập phân, nghìn đồng |

## Kết quả ba tháng đầu

| Tháng | Lãi suất 0,008 | Lãi suất 0,0 |
|---|---|---|
| 1 | `479000.00` | `475000.00` |
| 2 | `457832.00` | `450000.00` |
| 3 | `436494.66` | `425000.00` |

## Điểm chính của bài

Hàm được gọi ba lần với ba đối số khác nhau, trong khi tham số chỉ có một bộ tên. Đó chính là chỗ phân biệt tham số với đối số: ba lần gọi, ba đối số `so_du` khác nhau là 500 000, 479 000 và 457 832 nghìn đồng.

Phép chặn đáng chú ý nhất là điều kiện `tien_tra <= so_du * lai_suat`. Nó không bắt một kiểu dữ liệu sai hay một miền sai, mà bắt một tổ hợp dữ liệu **hợp lệ từng cái** nhưng vô nghĩa khi đi cùng nhau: tiền trả 1 000 nghìn đồng là hợp lệ, lãi suất 0,008 là hợp lệ, số dư 500 000 là hợp lệ, nhưng ba cái cùng nhau cho một khoản nợ tăng mãi.

Không có phép chặn đó, hàm vẫn chạy và vẫn trả về một con số lớn hơn số dư ban đầu — không báo gì. Lỗi loại này chỉ lộ ra khi ai đó đọc bảng và thấy nợ tăng.

Ca biên lãi suất bằng 0 là ca kiểm được bằng tính toán nhẩm: số dư phải giảm đúng 25 000 nghìn đồng mỗi tháng. Loại ca như vậy có giá trị hơn ca lấy số từ chính chương trình, vì nó dựa trên một tính chất của bài toán chứ không dựa trên cách cài đặt.

Danh sách chưa được dạy tới Chương 5, nên hàm `ba_thang_dau` trả về ba giá trị. Cách này cũng hợp với §7: không dùng cấu trúc chưa dạy.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 500 000 · 0,008 · 25 000 | `479000.00`, `457832.00`, `436494.66` |
| Biên | 500 000 · 0,0 · 25 000 | `475000.00`, `450000.00`, `425000.00` |
| Không hợp lệ | 500 000 · 0,008 · 0 | `ValueError`; tiền trả 0 làm số dư tăng mãi |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
