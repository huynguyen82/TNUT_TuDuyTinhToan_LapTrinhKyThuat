# Lời giải Bài tập 2.7

- Chương 2, Mục 2.4.1 và 2.4.2 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.4.2].[BaiTap-7].py`
- Lời giải này không in vào giáo trình. Bài mức 3 có nhiều cách trình bày đúng.

## Bảng năm ví dụ

| Mã | Kết quả bất thường | Nguồn sai số | Sai số tuyệt đối | Cách xử lý |
|---|---|---|---|---|
| S1 | `0.1 + 0.2` cho `0.30000000000000004` | Làm tròn | 5,55 × 10⁻¹⁷ | So bằng `math.isclose` |
| S2 | Cộng 0,1 mười lần cho `0.9999999999999999` | Làm tròn tích luỹ | 1,11 × 10⁻¹⁶ | Dùng `sum` hoặc `math.fsum` thay vòng lặp cộng tay |
| S3 | `1e308 ** 2` báo `OverflowError: (34, 'Result too large')` | Tràn số | không đo được | Đổi đơn vị để đại lượng nằm trong miền |
| S4 | `-7 // 2` cho −4, kỳ vọng −3 | Chọn sai toán tử | lệch đúng 1 đơn vị | Dùng `//` khi cần làm tròn xuống, `int` khi cần cắt về phía 0 |
| S5 | Cộng 0,01 mười lần vào 50,00 cho `50.09999999999998` | So sánh số thực | 2,13 × 10⁻¹⁴ | `math.isclose` với ngưỡng lấy từ dung sai |

## Ba điểm phải nói rõ

**S3 có hai hành vi khác nhau.** Phép `1e308 ** 2` báo `OverflowError`, nhưng phép `1e308 * 10` **không** báo gì và trả về `inf`. Trường hợp thứ hai nguy hiểm hơn: chương trình chạy tiếp với một giá trị vô nghĩa, và mọi phép tính sau đó cũng cho `inf` mà không có dấu hiệu nào. Đây là câu hỏi mà đề bài yêu cầu trả lời.

**S4 không phải sai số biểu diễn.** Bốn ví dụ còn lại đều bắt nguồn từ cách máy lưu số; S4 thì không. Giá trị −4 là kết quả **đúng** của phép chia nguyên, chỉ là người viết chọn sai toán tử cho ý định của mình. Vì vậy ở S4 không đo sai số tuyệt đối theo nghĩa thông thường mà ghi độ lệch đúng 1 đơn vị. Bài làm nào xếp S4 vào cùng nhóm với S1 và S2 là chưa phân biệt được hai thứ khác nhau.

**S5 là S2 ở quy mô bài toán thật.** Cùng cơ chế làm tròn tích luỹ, nhưng S2 hỏi về con số còn S5 hỏi về **kết luận**: phép `==` cho `False` nên chi tiết bị loại oan. Sai số 2,13 × 10⁻¹⁴ mm nhỏ hơn dung sai 0,05 mm khoảng 12 bậc, tức hoàn toàn không đáng kể về mặt cơ khí, mà vẫn đủ để lật câu kết luận. Đó là lý do phải thay `==` bằng `math.isclose`.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Ví dụ | Kết quả |
|---|---|---|
| Thường | S1 | Nguồn làm tròn; sai số tuyệt đối 5,55 × 10⁻¹⁷ |
| Biên | S4 | Nguồn chia nguyên; lệch đúng 1 đơn vị; không phải sai số biểu diễn |
| Không hợp lệ | S3 | Nguồn tràn số; `OverflowError`; còn `1e308 * 10` trả `inf` mà không báo lỗi |

## Một giới hạn của phép đo

Sai số tương đối không định nghĩa khi giá trị đúng bằng 0. Tệp kiểm chứng khẳng định hàm `sai_so_tuong_doi` ném `ValueError` trong trường hợp đó, thay vì trả về một con số vô nghĩa. Đây cũng là lý do `math.isclose` cần `abs_tol` cho các đại lượng có thể bằng 0, nội dung của Bài tập 2.8.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
