# Lời giải Bài tập 3.1

- Chương 3, Mục 3.1.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Đoạn mã của đề bài

Bốn lệnh `if` độc lập, trong đó nhánh ba viết `nhiet_do >= 80.0` mà thiếu cận trên, nên miền của nó chồng lấn miền của nhánh bốn.

## Ba dự đoán và ba kết quả

| Nhiệt độ | Số nhánh cùng khớp | Đoạn mã sai cho | Đáp án đúng | Lỗi có lộ ra |
|---|---|---|---|---|
| 45 °C | 1 | `binh thuong` | `binh thuong` | không |
| 85 °C | 1 | `nguy hiem` | `nguy hiem` | không |
| 120 °C | **2** | `dung may` | `dung may` | không, nhưng vì lý do sai |

## Điểm chính của bài

Không số đo nào trong ba số làm lỗi lộ ra, và đó là nội dung bài tập này muốn dạy. Với 120 °C, hai nhánh cùng khớp; kết quả vẫn đúng chỉ vì nhánh bốn viết **sau** nhánh ba nên nó gán đè. Tính đúng đắn ở đây phụ thuộc thứ tự viết, một thứ không ai ghi vào đặc tả và không ai kiểm.

Tệp kiểm chứng chứng minh điều đó bằng cách đảo thứ tự hai lệnh `if` cuối: kết quả lật từ `dung may` sang `nguy hiem`, tức sai, mà không dòng nào bị sửa nội dung.

Chuỗi `elif` không có vấn đề này: nó dừng ở điều kiện đúng đầu tiên, nên không bao giờ có hai nhánh cùng chạy, kể cả khi người viết để miền chồng lấn.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 45 °C | `binh thuong`; một nhánh khớp |
| Biên | 85 °C | `nguy hiem`; đúng, nên lỗi vẫn không lộ ra |
| Không hợp lệ | 120 °C | Hai nhánh cùng khớp; kết quả đúng vì lý do sai |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
