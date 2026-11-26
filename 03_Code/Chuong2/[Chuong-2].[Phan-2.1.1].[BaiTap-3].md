# Lời giải Bài tập 2.3

- Chương 2, Mục 2.1.1 và 2.3.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.1.1].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Cấu trúc lời giải

Chương trình tách làm ba phần, theo đúng ba thành phần của bảng đặc tả ở Mục 1.1.1:

| Phần | Hàm | Việc |
|---|---|---|
| Kiểm đầu vào | `kiem_mien` | Chặn giá trị ngoài miền, kèm tên đại lượng sai |
| Bước xử lý | `dien_nang` | Tính điện năng sau khi đã kiểm |
| Định dạng đầu ra | `dinh_dang` | Một chữ số thập phân theo đặc tả |

Phần nhập từ bàn phím tách riêng ở hàm `chay_tu_ban_phim`. Tách như vậy có một lợi ích cụ thể: phần tính kiểm được bằng khẳng định tự động mà không cần gõ bàn phím, nên tệp lời giải chạy được trong bộ kiểm bảo trì.

## Một phát hiện khi viết lời giải

Khẳng định đầu tiên tôi viết cho phần định dạng là `dinh_dang(60.05) == "60.1"`, theo quy tắc làm tròn trên giấy. Chạy thật cho `60.0`.

Nguyên nhân: 60,05 được lưu thành 60,049999999999997..., nhỏ hơn 60,05 một chút, nên làm tròn một chữ số thập phân cho 60,0. Làm tròn hiển thị theo **giá trị lưu**, không theo chữ số đã gõ trong mã nguồn.

Thêm một trường hợp nữa đáng biết: 60,25 biểu diễn đúng được, và `f"{60.25:.1f}"` cho `60.2` chứ không cho `60.3`, vì Python làm tròn tới số chẵn khi giá trị nằm đúng giữa.

Hai điều này là hệ quả trực tiếp của Mục 2.4.1, và là lý do bài tập này đặt tiền đề ở cả 2.1.1 lẫn 2.3.1.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 7.5 và 8 | `60.0` |
| Biên | 7.5 và 0 | `0.0`; số giờ bằng 0 là cận dưới hợp lệ của miền |
| Không hợp lệ | `bay phay nam` | `ValueError`; chuỗi không ép kiểu được |

Thêm hai bộ biên nữa đã kiểm: hai cận của cả hai miền đều hợp lệ, và 200 kW chạy 24 h cho 4 800,0 kWh.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
