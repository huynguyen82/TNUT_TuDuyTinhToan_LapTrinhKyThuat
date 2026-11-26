# Lời giải Bài tập 4.5

- Chương 4, Mục 4.1.1 · Mức 2 · 30 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.1.1].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | `dong_dien` số thực, đơn vị A, miền 0 đến 1 000 |
| Xử lý | Chặn dòng điện ngoài miền, rồi tra chuỗi `elif` năm mốc; vượt mốc cuối thì trả hằng số `VUOT_BANG_TRA` |
| Đầu ra | Số thực, đơn vị mm², một chữ số thập phân, hoặc câu báo vượt bảng tra |

## Kết quả ba dòng điện

| Dòng điện | Tiết diện | Đối chiếu Bài tập 3.4 |
|---|---|---|
| 30,0 A | `4.0` mm² | trùng |
| 16,0 A | `1.5` mm² | trùng |
| 100,0 A | vượt bảng tra | trùng |

## Điểm chính của bài

Bài tập 3.4 làm được một dòng điện trong một lần chạy, vì bảng tra viết thẳng trong luồng chương trình. Sau khi tách thành hàm, ba dòng điện là ba lời gọi, và bảng tra chỉ có **một** bản. Thêm dòng điện thứ tư là thêm một lời gọi, không phải chép lại sáu nhánh `elif`.

Chi tiết quan trọng nhất của bài nằm ở trường hợp vượt bảng tra. Nếu hàm chỉ có năm nhánh `elif` mà không có dòng `return` cuối, nó trả `None` khi dòng điện vượt 63 A — đúng lỗi `L4.1-3` của Mục 4.1.1. Không báo lỗi, và `None` đi tiếp vào chương trình như một tiết diện.

Lời giải chọn trả về hằng số `VUOT_BANG_TRA` bằng −1,0. Giá trị này **nói được** điều nó muốn nói: một tiết diện âm không bao giờ là một tiết diện thật, nên chỗ nhận nó phân biệt được ngay. Tệp kiểm chứng có một khẳng định riêng cho điều này: `tiet_dien(100.0) is not None`.

Ca biên phải phủ cả năm mốc, vì lỗi hay gặp nhất của bảng tra là lệch một mốc, và chỉ số đo đúng bằng mốc mới phân biệt được `<=` với `<`. Lời giải thêm một ca nữa là 16,1 A, để xác nhận nhích qua mốc thì sang mốc tiếp theo. Bài tập 4.6 cho thấy ca nhích này không chỉ bổ sung mà còn là ca duy nhất bắt được một loại lỗi mà năm ca tại mốc bỏ qua.

Thứ tự năm nhánh phải từ mốc nhỏ tới mốc lớn, như Mục 3.1.1 đã nêu. Tách thành hàm không làm điều kiện này mất đi; nó chỉ gom chỗ có thể sai lại thành một chỗ.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 30 A | `4.0` mm²; trùng Bài tập 3.4 |
| Biên | 16 A | `1.5` mm²; dòng đúng bằng mốc nhận tiết diện của mốc đó |
| Không hợp lệ | 100 A | Báo vượt bảng tra qua hằng số `VUOT_BANG_TRA`, không trả `None` |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
