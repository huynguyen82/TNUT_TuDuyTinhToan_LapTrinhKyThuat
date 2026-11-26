# Lời giải Bài tập 3.6

- Chương 3, Mục 3.2.3 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.2.3].[BaiTap-6].py`
- Lời giải này không in vào giáo trình.

## Lời giải

Một vòng lặp `for`, trong thân có hai lệnh rẽ nhánh theo thứ tự bắt buộc: kiểm số đo lỗi **trước**, rồi mới kiểm vượt ngưỡng. Đảo thứ tự thì một số đo âm sẽ được so với ngưỡng trước khi bị loại, tuy không ảnh hưởng kết quả ở đây nhưng làm mạch đọc sai ý.

Gặp số đo âm thì tăng số đếm lỗi rồi `continue`, tức bỏ qua lượt này và sang giờ kế tiếp.

## Vì sao `continue` chứ không `break`

Đây là điểm chính của bài. Tệp kiểm chứng so hai cách trên cùng dãy 42 · −5 · 61 · 73:

| Cách | Số giờ vượt ngưỡng | Số số đo lỗi |
|---|---|---|
| `continue` | 2 | 1 |
| `break` | **0** | 1 |

Dùng `break` làm mất hai giờ vượt ngưỡng nằm sau số đo lỗi. Với một ca 8 giờ mà cảm biến chập ở giờ thứ hai, báo cáo quan trắc mất sáu giờ còn lại và kết luận ca đó không có giờ nào vượt ngưỡng.

Phân biệt hai lệnh bằng một câu: `break` nghĩa là *đã xong*; `continue` nghĩa là *lượt này bỏ qua*. Một số đo hỏng không có nghĩa là ca trực đã xong.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 42 · 55 · 61 · 48 · 50 · 73 | 3 giờ vượt ngưỡng, 0 số đo lỗi |
| Biên | Một số đo 50,0 | Không đếm là vượt, vì điều kiện dùng dấu lớn hơn |
| Không hợp lệ | Một số đo −5 ở giữa dãy | Bỏ qua và đếm vào số đo lỗi; các giờ sau vẫn được xử lý |

Hai ca nữa đã kiểm: dãy rỗng cho 0 và 0, và dãy toàn số đo lỗi cho 0 giờ vượt với 3 số đo lỗi — ở ca cuối này `break` chỉ đếm được 1 lỗi thay vì 3.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
