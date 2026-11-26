# Lời giải Bài tập 1.1

- Chương 1, Mục 1.1.1 · Mức 1 · 10 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Bốn ô đã điền

| Ô | Vị trí trong bảng đặc tả | Nội dung điền |
|---|---|---|
| 1 | Đầu ra `tong_dien_nang`, đơn vị | `kWh` |
| 2 | Đầu ra `tong_dien_nang`, định dạng | Một chữ số thập phân |
| 3 | Đầu vào `t[i]`, miền giá trị | Từ 0 đến 24 h; ngoài miền thì báo dữ liệu không hợp lệ |
| 4 | Đầu ra `tong_dien_nang`, trường hợp đặc biệt | Danh sách rỗng trả về 0,0 |

## Giải thích hậu quả khi thiếu từng ô

**Ô 1 — đơn vị của đầu ra.** Thiếu ô này thì cùng một kết quả đọc được thành 384,0 kWh hoặc 1 382,4 MJ, hai con số lệch nhau đúng 3,6 lần, và không có căn cứ nào nói cách nào sai.

**Ô 2 — số chữ số thập phân.** Thiếu ô này thì `384` và `384,0` cùng được chấm đúng, nên bảng đặc tả không dùng làm căn cứ chấm được; hệ thống tự chấm so chuỗi ký tự nên hai cách trình bày cho hai kết quả chấm khác nhau.

**Ô 3 — miền giá trị của số giờ chạy.** Thiếu ô này thì giá trị 30 giờ được chấp nhận, và một động cơ 7,5 kW cho ra 225,0 kWh trong một ngày, trong khi mức tối đa có thể là 180,0 kWh ứng với 24 giờ. Sai số 45,0 kWh trên một động cơ mà chương trình vẫn chạy bình thường.

**Ô 4 — giá trị trả về khi danh sách rỗng.** Thiếu ô này thì danh sách rỗng không có đáp án xác định: người giải này trả về 0,0, người giải kia để chương trình dừng vì lỗi. Đây đúng là trường hợp mà lỗi `L1.1-2` mô tả.

## Các con số đã kiểm bằng máy

| Khẳng định | Giá trị |
|---|---|
| 384,0 kWh đổi sang MJ | 1 382,4 MJ, tỉ số đúng 3,6 |
| Trình bày 384,0 với 0 chữ số thập phân | `384` |
| Trình bày 384,0 với 1 chữ số thập phân | `384.0` |
| Động cơ 7,5 kW chạy 30 h | 225,0 kWh, số giờ nằm ngoài miền |
| Động cơ 7,5 kW chạy 24 h | 180,0 kWh, số giờ ở đúng cận trên của miền |
| Tổng điện năng của danh sách rỗng | 0,0 kWh |
| Tổng điện năng bộ năm động cơ | 384,0 kWh |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Điền đúng bốn ô | 5,0 |
| Giải thích đúng hậu quả của ô 3 và ô 4, tức hai ô về trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Trình bày đúng khuôn bảng đặc tả ba phần | 1,5 |
| Dùng đúng tên đại lượng của bảng đặc tả | 1,0 |
