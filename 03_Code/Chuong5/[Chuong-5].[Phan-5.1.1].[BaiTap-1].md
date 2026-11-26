# Lời giải Bài tập 5.1

- Chương 5, Mục 5.1.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Bốn dự đoán và bốn kết quả

| Phép cắt lát | Dự đoán thường gặp | Số phần tử thật | Nội dung thật |
|---|---|---|---|
| `ngay[6:9]` | 4 phần tử | **3** | 48,6 · 62,3 · 71,5 |
| `ngay[20:30]` | `IndexError` | **4** | 46,3 · 40,1 · 36,8 · 33,5 |
| `ngay[5:2]` | `IndexError` hoặc đoạn ngược | **0** | danh sách rỗng |
| `ngay[-3:]` | 3 phần tử | 3 | 40,1 · 36,8 · 33,5 |

Hai phép giữa là hai phép vượt ra ngoài danh sách mà **không** báo lỗi.

## Điểm chính của bài

Cùng một chỉ số vượt cuối, Python xử sự theo hai cách khác nhau tuỳ chỗ dùng. Tệp kiểm chứng đo lại điều đó bằng hai khẳng định cạnh nhau:

| Đoạn mã | Kết quả |
|---|---|
| `ngay[24]` | `IndexError: list index out of range` |
| `ngay[24:30]` | 0 phần tử, không báo lỗi |

Lấy phần tử bắt lỗi, cắt lát thì không. Cắt lát **không bao giờ** báo lỗi vượt cuối: nó cắt bớt tới chỗ còn dữ liệu, hoặc cho đoạn rỗng.

Vì sao điều đó nguy hiểm hơn một thông báo lỗi. Một `IndexError` dừng chương trình ở đúng dòng sai, và người đọc thông báo biết ngay phải sửa chỗ nào. Một đoạn rỗng thì đi tiếp: vòng lặp sau đó chạy 0 lượt, phép `sum` cho 0,0, và phép chia tính trung bình chia cho `len` của đoạn — nếu `len` là 0 thì mới báo lỗi, mà báo ở một dòng khác, cách xa chỗ sai.

Trường hợp tệ nhất là `ngay[20:30]`: nó cho 4 phần tử, một con số trông hợp lý. Một chương trình tính trung bình trên đoạn đó chạy xong, in ra một con số, và con số ấy là trung bình của 4 giờ chứ không phải của 10 giờ như người viết tưởng. Không dòng nào sai về cú pháp, không thông báo nào xuất hiện.

Cách phòng duy nhất là kiểm `len` của đoạn **vừa cắt**, không kiểm hai cận. Hai cận có thể đúng về mặt số học mà vẫn cho đoạn ngắn hơn mong đợi.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `ngay[6:9]` | 3 phần tử; cận trên 9 không thuộc đoạn |
| Biên | `ngay[20:30]` | 4 phần tử, không báo lỗi; `len` bằng `len(ngay) - 20` |
| Không hợp lệ | `ngay[5:2]` | Danh sách rỗng, không báo lỗi |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
