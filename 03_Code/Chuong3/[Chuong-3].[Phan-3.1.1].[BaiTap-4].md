# Lời giải Bài tập 3.4

- Chương 3, Mục 3.1.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.1.1].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Lời giải

Chuỗi `elif` năm nhánh theo đúng năm mốc của bảng, cộng một `else` báo vượt bảng tra, và một bước kiểm miền đặt trước.

**Thứ tự nhánh là một phần của lời giải**, không phải chuyện trình bày. Các mốc phải xếp từ nhỏ tới lớn. Đảo ngược thì dòng 10 A rơi vào nhánh `<= 63` đầu tiên và nhận dây 10 mm², tức thừa gần bảy lần tiết diện cần thiết. Chương trình vẫn chạy, vẫn in ra một con số hợp lệ, và lỗi chỉ lộ ra khi có người đối chiếu với bảng gốc.

## Năm mốc và sáu nhánh

| Dòng điện | Tiết diện |
|---|---|
| tới 16 A | 1,5 mm² |
| tới 25 A | 2,5 mm² |
| tới 32 A | 4,0 mm² |
| tới 40 A | 6,0 mm² |
| tới 63 A | 10,0 mm² |
| trên 63 A | vượt bảng tra |

## Một phép kiểm theo tính chất

Tiết diện phải tăng đơn điệu theo dòng điện: dòng lớn hơn thì không bao giờ nhận dây nhỏ hơn. Tệp kiểm chứng duyệt một dãy dòng điện tăng dần và khẳng định tính chất đó ở mọi bước.

Phép kiểm này mạnh hơn kiểm từng đáp số vì nó bắt được lỗi đảo thứ tự nhánh mà không cần biết trước đáp án của từng dòng điện cụ thể.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 30 A | `4.0` mm² |
| Biên | 16 A | `1.5` mm²; dòng đúng bằng mốc nhận tiết diện của mốc đó |
| Không hợp lệ | 100 A | Báo vượt bảng tra |

Hai ca biên nữa đã kiểm: 16,1 A nhảy sang 2,5 mm², và 63,1 A sang vượt bảng.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
