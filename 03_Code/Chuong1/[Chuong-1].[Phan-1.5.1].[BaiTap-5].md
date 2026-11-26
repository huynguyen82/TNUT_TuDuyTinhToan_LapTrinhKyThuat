# Lời giải Bài tập 1.5

- Chương 1, Mục 1.5.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.5.1].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Bảng vết trên dãy bốn số đo

Dãy 12,0 · 18,0 · 15,0 · 21,0 µg/m³.

| Lượt | `i` | Số đo (µg/m³) | `tong` (µg/m³) | `i < n` |
|---|---|---|---|---|
| trước vòng lặp | 0 | – | 0,0 | Đúng |
| 1 | 1 | 12,0 | 12,0 | Đúng |
| 2 | 2 | 18,0 | 30,0 | Đúng |
| 3 | 3 | 15,0 | 45,0 | Đúng |
| 4 | 4 | 21,0 | 66,0 | Sai, dừng |

Sau vòng lặp: `trung_binh = 66,0 / 4 = 16,5` µg/m³.

## Bảng vết trên dãy rỗng

| Lượt | `i` | Số đo (µg/m³) | `tong` (µg/m³) | `i < n` |
|---|---|---|---|---|
| trước vòng lặp | 0 | – | 0,0 | Sai, dừng |

Bảng chỉ có một dòng. Cột điều kiện dừng đã nhận giá trị sai ngay ở dòng trước vòng lặp, nên thân vòng lặp không chạy lượt nào và `tong` giữ nguyên 0,0.

## Bước không thực hiện được trên dãy rỗng

Bước sau vòng lặp, `gán trung_binh = tong / so_phan_tu`, không thực hiện được vì `so_phan_tu` bằng 0. Đây đúng là lỗi `L1.1-2` của Mục 1.1.1: một bước vi phạm điều kiện *thực hiện được* của thuật toán, và chỉ lộ ra ở một bộ dữ liệu cụ thể.

Điều đáng nói là vòng lặp **không** có lỗi: nó chạy đúng 0 lượt và để lại `tong` bằng 0,0, hoàn toàn hợp lý. Lỗi nằm ở bước sau nó. Bảng vết tách bạch được hai chỗ này, còn đọc nhẩm thì dễ quy cả hai về một.

Cách sửa: thêm một bước kiểm `nếu so_phan_tu > 0 thì` bao quanh phép chia, và khai báo trong phần đầu ra của bảng đặc tả rằng dãy rỗng không có trung bình cộng.

## Các giá trị đã kiểm bằng máy

| Bộ dữ liệu | Số dòng bảng vết | `tong` | Trung bình |
|---|---|---|---|
| 12,0 · 18,0 · 15,0 · 21,0 | 5 | 66,0 µg/m³ | 16,5 µg/m³ |
| Một số đo 12,0 | 2 | 12,0 µg/m³ | 12,0 µg/m³ |
| Dãy rỗng | 1 | 0,0 µg/m³ | bước chia không thực hiện được |

Miền số đo từ 0 đến 500 µg/m³ cũng đã kiểm: hai đầu miền đều hợp lệ, 500,1 thì không.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Bảng vết trên dãy bốn số đo đúng từng ô, và trung bình 16,5 µg/m³ | 5,0 |
| Bảng vết trên dãy rỗng có đúng một dòng, và chỉ đúng bước không thực hiện được | 2,5 |
| Hai bảng có đủ dòng trước vòng lặp và cột điều kiện dừng | 1,5 |
| Tên đại lượng trong bảng khớp tên trong mã giả | 1,0 |
