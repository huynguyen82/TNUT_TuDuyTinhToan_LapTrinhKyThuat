# Lời giải Bài tập 4.1

- Chương 4, Mục 4.1.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Đoạn mã của đề bài

Hàm `so_du_thieu_return` tính đúng công thức và gán kết quả vào biến cục bộ `moi`, nhưng không có lệnh `return`. Biến `moi` mất khi hàm kết thúc, nên hàm trả về `None`.

## Dự đoán và ba kết quả

| Cách dùng kết quả | Dự đoán thường gặp | Kết quả thật | Lỗi có lộ ra |
|---|---|---|---|
| In ngay kết quả | `479000.0` | `None` | không, chương trình chạy xong bình thường |
| Đem vào phép trừ | `454000.0` | `TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'` | có |
| Đem vào điều kiện `while` | vòng lặp chạy 22 lượt | `TypeError: '>' not supported between instances of 'NoneType' and 'int'` | có |

## Điểm chính của bài

Dòng sai thật là dòng 23, dòng gán `moi` mà không trả về. Dòng báo lỗi là dòng 37, dòng làm phép trừ. Khoảng cách là **14 dòng**, và hai dòng đó nằm trong hai hàm khác nhau.

Đó là lý do lỗi thiếu `return` khó tìm hơn lỗi cú pháp: thông báo lỗi chỉ vào chỗ **dùng** kết quả, không chỉ vào chỗ **tạo ra** kết quả sai. Người đọc thông báo bắt đầu soát từ dòng 37 và có thể soát rất lâu trước khi nghĩ tới hàm.

Dấu hiệu nhận ra loại lỗi này gọn hơn nhiều: mọi thông báo đều có chữ `NoneType`. Thấy `NoneType` thì việc đầu tiên là tìm hàm nào thiếu `return`, không phải đọc lại dòng báo lỗi.

Trường hợp nguy hiểm nhất là trường hợp thứ nhất: in ngay kết quả. Không thông báo lỗi nào, chương trình chạy xong, và `None` được in ra như một giá trị bình thường. Nếu kết quả đó đi vào một bảng báo cáo thì bảng có một ô trống mà không ai biết vì sao.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Gọi hàm rồi in ngay | `None`; không có lỗi, nên lỗi không lộ ra |
| Biên | Gọi hàm rồi trừ | `TypeError` nhắc `NoneType` và `float`, báo ở dòng phép trừ |
| Không hợp lệ | Gọi hàm rồi so với 0 | `TypeError` nhắc `NoneType` và `int`; vòng lặp không chạy lượt nào |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
