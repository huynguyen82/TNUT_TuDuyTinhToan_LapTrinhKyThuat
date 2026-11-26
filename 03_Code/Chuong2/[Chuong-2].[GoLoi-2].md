# Lời giải Bài gỡ lỗi GL2

- Chương 2 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-2].[GoLoi-2].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo nguyên văn | Cách sửa |
|---|---|---|---|---|
| 4 | cú pháp | `DUNG_SAI = 0,05` | `SyntaxError: leading zeros in decimal integer literals are not permitted` | `DUNG_SAI = 0.05` |
| 7 | thực thi | `kich_thuoc = int(dong_nhap)` | `ValueError: invalid literal for int() with base 10: '50.03'` | `kich_thuoc = float(dong_nhap)` |
| 13 | logic | `math.isclose(kich_thuoc, DANH_NGHIA)` | **không có**; kết luận `khong dat` cho một chi tiết đạt | `math.isclose(kich_thuoc, DANH_NGHIA, abs_tol=DUNG_SAI)` |

Sau khi sửa đủ ba lỗi, chi tiết 50,03 mm cho độ lệch `0.03` và kết luận `dat`.

## Điểm chính của bài

**Ba lỗi lộ ra theo đúng ba lần chạy.** Lần một không chạy dòng nào. Lần hai chạy tới dòng 7 rồi dừng. Lần ba chạy hết và in ra một phiếu kết quả hoàn chỉnh, đúng định dạng, cột thẳng hàng — và kết luận sai.

**Lỗi dòng 4 là lỗi dấu phẩy thập phân, nhưng không phải lúc nào cũng báo.** Ở đây `0,05` bị chặn vì `05` có số 0 đứng đầu. Nếu viết `0,5` thì Python **không báo gì**: biến nhận một bộ hai số nguyên `(0, 5)`, và lỗi chỉ nổ ra ở dòng 9 khi lấy số thực trừ một bộ. Đây đúng hộp *Cảnh báo lỗi* của Mục 2.4.1, và là lý do lỗi này đáng nhớ hơn vẻ ngoài của nó.

**Lỗi dòng 7 cho thấy vì sao phải chọn đúng hàm ép kiểu.** `int` không nhận chuỗi có phần thập phân — đúng lỗi `L2.2-2`. Thứ tự đúng là ép sang `float` trước; nếu bài toán cần số nguyên thì ép `int(float(x))` sau.

**Lỗi dòng 13 là lỗi nguy hiểm nhất và là lý do bài này tồn tại.** Hàm `math.isclose` gọi thiếu ngưỡng vẫn chạy, vẫn trả `True` hoặc `False`, vẫn in ra một kết luận. Ngưỡng mặc định của nó là ngưỡng **tương đối** cỡ 10⁻⁹. Với hai số quanh 50, ngưỡng đó tương đương khoảng 5 × 10⁻⁸ mm — nhỏ hơn dung sai 0,05 mm **một triệu lần**. Hệ quả: gần như mọi chi tiết đều bị loại.

Tệp kiểm chứng ghi điều đó thành một khẳng định đặt cạnh nhau: cùng dữ liệu `50.03`, bản còn lỗi cho `khong dat`, bản đã sửa cho `dat`.

Bài học, cũng là nội dung Khối 8 của Mục 2.4.2: **ngưỡng là việc của người kỹ sư, không phải của hàm**. Ngưỡng ở đây phải lấy từ dung sai của bản vẽ, tức 0,05 mm, chứ không lấy giá trị mặc định.

**Một chi tiết trình bày đáng chú ý.** Dòng 12 tính `lech` nhưng dòng 13 không dùng `lech` mà gọi lại `math.isclose` trên hai giá trị gốc. Hai dòng ấy làm cùng một việc theo hai cách. Viết `dat = abs(lech) <= DUNG_SAI` thì chỉ còn một cách, ngắn hơn, và không cần `math` nữa. Lời giải giữ `math.isclose` vì đề bài đang dạy hàm đó, nhưng với bài toán dung sai tuyệt đối thì phép so trực tiếp rõ hơn.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `50.03` | Kích thước in `50.03`; độ lệch `0.03`; kết luận đạt. Bản còn lỗi dòng 13 kết luận **ngược** |
| Biên | `50.05` | Kết luận đạt, vì cận trên thuộc miền hợp lệ |
| Không hợp lệ | `50,03` | `ValueError` ở bước ép kiểu; báo dữ liệu không hợp lệ |
