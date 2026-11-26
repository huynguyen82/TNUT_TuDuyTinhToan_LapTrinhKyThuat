# Lời giải Bài tập 5.6

- Chương 5, Mục 5.4.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.4.1].[BaiTap-6].py`
- Lời giải này không in vào giáo trình. Hai hình bài này sinh ra nằm ở `04_DuLieu`, không phải hình in trong sách.

## Hai bản đồ thị

| Bản | Năm phép bắt buộc | Kích thước tệp |
|---|---|---|
| Đủ năm phép | `plot` · `set_xlabel` · `set_ylabel` · `legend` · `savefig` | 91 kB |
| Thiếu tên trục và chú giải | chỉ `plot` và `savefig` | 59 kB |

Bản thiếu nhỏ hơn 32 kB, vì nó không phải vẽ chữ nào.

## Điểm chính của bài

Bản thiếu tên trục **vẽ ra bình thường** và không có thông báo nào. Đó là điều cần nắm: Matplotlib không bắt buộc tên trục, nên thiếu tên trục là một lỗi im lặng hoàn toàn — không `ValueError`, không cảnh báo, chỉ một tệp hình đẹp mà vô dụng.

Đồ thị thiếu gì khi đưa vào báo cáo. Trục dọc của bài này chạy từ 25 tới 72, và người đọc không biết đó là µg/m³ hay mg/m³. Hai đơn vị ấy cách nhau **một nghìn lần**, nên cùng một hình đọc được thành "nồng độ dưới ngưỡng" hoặc "nồng độ gấp hai mươi lần ngưỡng". Trục ngang chạy từ 0 tới 23 và không rõ là giờ, ngày hay số thứ tự số đo. Đường nét đứt ở mức 50 không có chú giải nên không rõ nó là ngưỡng cảnh báo, giá trị trung bình, hay một mốc nào khác.

Nói gọn: bản thiếu tên trục cho người đọc biết **hình dạng** của chuỗi số đo và không cho biết gì khác. Hình dạng một mình không trả lời được câu hỏi của báo cáo, vốn là "nồng độ có vượt ngưỡng hay không".

Vì vậy tên trục, đơn vị và chú giải không phải phần trang trí mà là phần **dữ liệu** của hình. Một hình thiếu chúng tương đương một bảng số không có tiêu đề cột.

Hai ca biên đáng ghi lại. Thứ nhất, đường ngưỡng chỉ nhìn thấy được khi nó nằm giữa cực tiểu và cực đại của chuỗi; tệp kiểm chứng khẳng định `min(day) < 50.0 < max(day)`. Với một chuỗi toàn dưới ngưỡng, đường ngưỡng nằm ngoài vùng vẽ và Matplotlib **mở rộng** trục để chứa nó. Đo trên một chuỗi năm số đo từ 9 tới 13: trước khi gọi `axhline`, trục dọc chạy từ 8,80 tới 13,20; sau khi gọi, nó chạy từ 6,95 tới 52,05, tức rộng gấp hơn mười lần. Chuỗi số đo bị ép xuống đáy hình. Thứ hai, một số đo duy nhất vẫn vẽ ra một hình hợp lệ trên 10 kB, nhưng một bảng một dòng đọc chính xác hơn — đó là nội dung Khối 8 Mục 5.4.1.

Ca ngoại lệ cuối cùng: danh sách **rỗng** cũng vẽ ra một tệp hình, chỉ là hình trống, và không báo lỗi gì. Thêm một lỗi im lặng của Matplotlib, nên chương trình phải tự kiểm `len` trước khi vẽ.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 24 số đo | Tệp 91 kB; bề ngang dưới 6,3 inch nên vừa khổ A4 |
| Biên | Một số đo duy nhất | Hình vẽ ra được, trên 10 kB, nhưng chỉ có một điểm |
| Không hợp lệ | Bỏ `set_xlabel`, `set_ylabel`, `legend` | Không báo lỗi; ba phép bắt buộc còn thiếu; hình không đọc được |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
