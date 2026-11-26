# Lời giải Bài tập 2.2

- Chương 2, Mục 2.2.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.2.1].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Ba đoạn mã, ba lỗi

| Đoạn | Mã sai | Loại lỗi | Thông báo nguyên văn | Bản sửa |
|---|---|---|---|---|
| a | `ten_ca = ngay` | Lỗi thực thi | `NameError: name 'ngay' is not defined` | `ten_ca = "ngay"` |
| b | `kich_thuoc = int("50.03")` | Lỗi thực thi | `ValueError: invalid literal for int() with base 10: '50.03'` | `kich_thuoc = float("50.03")` |
| c | `50 = kich_thuoc` | Lỗi cú pháp | `SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?` | `kich_thuoc = 50` |

Mọi thông báo trong bảng do tệp kiểm chứng chạy lấy, không chép tay.

## Phân biệt tên lỗi với loại lỗi

Đoạn a và đoạn b cùng là **lỗi thực thi** nhưng tên lỗi khác nhau: `NameError` và `ValueError`. Bài làm nào trả lời "lỗi `NameError`" là trả lời tên lỗi chứ chưa trả lời loại lỗi theo ba loại của Mục 1.5.1.

Cách phân biệt: lỗi cú pháp xảy ra **trước khi** chương trình chạy dòng nào, nên không dòng nào trong tệp được thực hiện, kể cả dòng đúng đứng trước dòng sai. Lỗi thực thi xảy ra **trong khi** chạy, nên các dòng trước đó đã chạy xong và đã sinh ra tác dụng.

## Vì sao ba đoạn không có lỗi logic

Đề bài cho ba đoạn mà không đoạn nào là lỗi logic, và đó là chủ ý. Lỗi logic **không sinh thông báo nào**, nên không thể hỏi "chép lại thông báo lỗi nguyên văn". Chính sự vắng mặt đó là điều cần nhận ra: hai loại lỗi đầu máy chỉ ra giúp, loại thứ ba thì không. Bài tập 2.1 là bài về lỗi logic, và ở đó không có thông báo nào để chép.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Đoạn | Kết quả mong đợi |
|---|---|---|
| Thường | a | Lỗi thực thi; `NameError`; thêm dấu nháy |
| Biên | b | Lỗi thực thi; `ValueError`; ép sang `float` trước |
| Không hợp lệ | c | Lỗi cú pháp; không dòng nào chạy; đảo hai vế phép gán |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
