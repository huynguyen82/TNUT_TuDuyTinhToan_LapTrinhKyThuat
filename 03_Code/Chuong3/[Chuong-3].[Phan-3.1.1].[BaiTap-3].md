# Lời giải Bài tập 3.3

- Chương 3, Mục 3.1.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.1.1].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Lời giải

Một hàm `phan_loai` gồm bước kiểm miền đặt trước chuỗi `elif` bốn nhánh. Bước kiểm trước là nguyên tắc của Mục 1.1.1: không tính trên dữ liệu chưa kiểm.

Điều kiện mỗi nhánh chỉ nêu cận trên, vì tới được nhánh nào nghĩa là mọi nhánh trên đã sai, tức cận dưới đã được bảo đảm.

## Chín ca biên quanh ba ngưỡng

| Ngưỡng | Ngay dưới | Đúng bằng | Ngay trên |
|---|---|---|---|
| 60 | 59,9 → `binh thuong` | 60,0 → `canh bao` | 60,1 → `canh bao` |
| 80 | 79,9 → `canh bao` | 80,0 → `nguy hiem` | 80,1 → `nguy hiem` |
| 100 | 99,9 → `nguy hiem` | 100,0 → `dung may` | 100,1 → `dung may` |

Chỉ ba ca **đúng bằng** ngưỡng phân biệt được điều kiện viết `<` với điều kiện viết `<=`. Sáu ca còn lại cho cùng kết quả với cả hai cách viết, nên bài làm nào chỉ thử 59,9 và 60,1 thì không kiểm được gì về dấu so sánh.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 72,5 °C | `canh bao` |
| Biên | 60,0 °C | `canh bao`; giá trị đúng bằng ngưỡng thuộc miền phía trên |
| Không hợp lệ | 500,0 °C | Báo dữ liệu không hợp lệ, kèm tên đại lượng sai |

Hai cận của miền đo cũng đã kiểm: −40,0 cho `binh thuong` và 300,0 cho `dung may`.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
