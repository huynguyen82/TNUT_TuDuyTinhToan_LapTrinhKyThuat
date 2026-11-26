# Lời giải Bài tập 3.8

- Chương 3, Mục 3.2.2 và 3.2.3 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.2.3].[BaiTap-8].py`
- Lời giải này không in vào giáo trình. Bài mức 3 có nhiều cách lý giải đúng.

## Quy tắc chọn, rút thành hai câu hỏi

1. **Có biết trước số lượt** trước khi vòng lặp bắt đầu không? Không thì dùng `while`; câu hỏi thứ hai không còn ý nghĩa.
2. **Có dừng sớm được** khi đã đủ thông tin không? Có thì `for` có `break`; không thì `for` thuần.

## Bốn tình huống

| Tình huống | Biết trước số lượt | Dừng sớm được | Chọn | Độ phức tạp |
|---|---|---|---|---|
| Tổng của đúng 12 số đo | có | không | `for` | O(n) |
| Đọc tới khi gặp giá trị kết thúc | không | — | `while` | O(số số đo tới giá trị kết thúc) |
| Tìm dòng đầu tiên trong bảng 500 dòng | có | có | `for` có `break` | O(n) xấu nhất, O(1) tốt nhất |
| Kiểm mọi số đo có trong miền hợp lệ | có | có | `for` có `break` | O(n) xấu nhất, O(1) tốt nhất |

## Hai chỗ dễ sai

**Tình huống thứ tư trông giống tình huống thứ nhất.** Cả hai đều duyệt một dãy đã biết độ dài. Khác nhau ở câu hỏi thứ hai: tổng cần **mọi** phần tử nên không dừng sớm được, còn kiểm miền chỉ cần **một** phần tử vi phạm là kết luận xong. Bỏ qua khác biệt đó thì chương trình kiểm miền vẫn đúng nhưng luôn duyệt hết dãy một cách vô ích.

**`break` không đổi độ phức tạp xấu nhất.** Cả ba lựa chọn đều có độ phức tạp xấu nhất O(n). Tệp kiểm chứng khẳng định điều đó cho cả ba. Khi mọi số đo đều hợp lệ, chương trình kiểm miền vẫn phải duyệt hết, đúng bằng chương trình tính tổng.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Tình huống | Kết quả |
|---|---|---|
| Thường | Tổng của đúng 12 số đo | `for`; O(n); biết trước số lượt và phải duyệt hết |
| Biên | Tìm dòng đầu trong bảng 500 dòng | `for` có `break`; O(n) xấu nhất, O(1) tốt nhất |
| Không hợp lệ | Đọc tới khi gặp giá trị kết thúc | `while`; `for` phải đoán số lượt và đoán thiếu thì bỏ sót mà không báo gì |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
