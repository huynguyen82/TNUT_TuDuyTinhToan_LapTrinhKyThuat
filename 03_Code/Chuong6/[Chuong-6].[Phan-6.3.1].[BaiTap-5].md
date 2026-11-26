# Lời giải Bài tập 6.5

- Chương 6, Mục 6.3.1 · Mức 2 · 30 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.3.1].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Hai cách đọc trên cùng một tệp

| Tiêu chí | Không bắt ngoại lệ | Bắt ngoại lệ theo loại |
|---|---|---|
| Số dòng dùng được | **49** | **715** |
| Kết cục | dừng ở dòng 50 với `ValueError: could not convert string to float: ''` | chạy hết 720 dòng |
| Dòng thiếu cột | không đếm được | 1 |
| Dòng ghi chữ thay số | không đếm được | 1 |
| Ô trống | không đếm được | 3 |

Tỉ lệ **14,6 lần**. Tổng 715 + 1 + 1 + 3 = 720, đúng số dòng dữ liệu của tệp.

## Ba loại dòng hỏng bắt ở ba chỗ khác nhau

| Loại dòng hỏng | Hỏng ở đâu | Bắt bằng gì |
|---|---|---|
| Thiếu cột | `cac_o[2]` khi `split` chỉ cho hai cột | `except IndexError` |
| Ô trống | `float("")` | phép so `o == ""` trước khi gọi `float` |
| Ghi chữ thay số | `float("ghi chu")` | `except ValueError` |

## Điểm chính của bài

**Ba loại dòng hỏng cần ba chỗ bắt, không phải một.** Dòng thiếu cột hỏng ngay ở phép lấy cột thứ ba; hai loại còn lại hỏng ở phép `float`. Gộp cả ba vào một khối `try` duy nhất thì bắt được cả ba, nhưng **không phân biệt được** loại nào — và số dòng bỏ qua theo từng loại là một phần của báo cáo, theo Mục 5.3.2.

Ô trống không bắt bằng `except` mà kiểm bằng `o == ""`. Lý do: `float("")` đúng là cho `ValueError`, nên bắt được, nhưng nó cho **cùng loại ngoại lệ** với dòng ghi chữ. Kiểm trước bằng một phép so chuỗi là cách duy nhất tách hai loại ấy mà không phải đọc nội dung thông điệp lỗi.

**Dòng hỏng đầu tiên nằm ở dòng 50, không phải dòng 100.** Tệp do `sinh_du_lieu_chuong5.py` sinh ra có ô trống ở các dòng 50, 200, 500 và dòng thiếu cột ở dòng 100. Ô trống đứng trước, nên bản không bắt ngoại lệ dừng ở dòng 50 và chỉ xử lý được 49 dòng. Con số phải đo chứ không suy từ vị trí của dòng thiếu cột.

**`FileNotFoundError` bắt ngoài vòng lặp, không bắt trong.** Tên tệp không có là lỗi xảy ra ở câu lệnh `open`, tức **trước** khi đọc dòng nào. Đặt nó vào khối `try` trong vòng lặp là sai chỗ theo hai nghĩa: vòng lặp chưa bao giờ chạy, và khối `try` ấy chạy 720 lần cho một chuyện chỉ xảy ra được một lần.

Hàm `doc_an_toan` của tệp kiểm chứng đặt nó đúng chỗ: bọc cả lời gọi `doc_co_bat`, bên ngoài mọi vòng lặp.

**Không dùng `except Exception`.** Đó là lỗi `L6.3-1` của [[b-loi631]]. Nếu dòng `float(cac_o[2])` bị gõ nhầm thành `float(cac_o[3])`, bản bắt theo loại sẽ báo `IndexError` cho **mọi** dòng và số dòng dùng được tụt về 0 — một dấu hiệu rõ ràng. Bản dùng `except Exception` rồi `continue` cũng cho 0 dòng, nhưng nó báo con số ấy như thể tệp hỏng, chứ không như thể chương trình hỏng.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | tệp 720 dòng | 715 dòng dùng được khi có bắt; 49 khi không bắt; tỉ lệ 14,6 lần |
| Biên | tệp chỉ có dòng tiêu đề | 0 dòng dùng được, cả hai cách, và không cách nào báo lỗi |
| Không hợp lệ | tên tệp không có | `FileNotFoundError`; lỗi **không** nên bắt trong vòng lặp, vì nó xảy ra trước khi đọc dòng nào |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
