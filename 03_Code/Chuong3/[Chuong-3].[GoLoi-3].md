# Lời giải Bài gỡ lỗi GL3

- Chương 3 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-3].[GoLoi-3].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo hoặc biểu hiện | Cách sửa |
|---|---|---|---|---|
| 21 | cú pháp | `if so_do < NGUONG_CANH_BAO` thiếu dấu hai chấm | `SyntaxError: expected ':'` | Thêm dấu hai chấm |
| 28 | thực thi | `tong / (so_luong - dem_loi)` không kiểm mẫu số | `ZeroDivisionError: float division by zero` khi mọi số đo đều lỗi | Kiểm số đo hợp lệ lớn hơn 0 trước phép chia |
| 12 | logic | `for chi_so in range(1, so_luong)` | **không có**; đọc thiếu đúng một số đo | `range(so_luong)` |

Sau khi sửa đủ ba lỗi, bộ 45 · 72,5 · 85 °C cho 1 bình thường, 1 cảnh báo, 1 nguy hiểm, trung bình 67,5 °C.

## Điểm chính của bài

**Lỗi dòng 12 là lỗi lệch một ở dạng khó thấy nhất.** `range(1, so_luong)` sinh `so_luong − 1` giá trị, nên vòng lặp đọc thiếu đúng một số đo — và nó bỏ **số đo đầu tiên**, không phải số cuối.

Với bộ thường ba số đo, bản còn lỗi cho 0 bình thường, 1 cảnh báo, 1 nguy hiểm, trung bình 78,75 °C. Ba con số đều hợp lý, đều nằm trong miền nhiệt độ thực tế của một động cơ. Không có gì trong chính kết quả nói rằng nó sai.

**Ca biên một số đo là ca bộc lộ lỗi rõ nhất.** Với `so_luong = 1`, `range(1, 1)` là dãy **rỗng**: vòng lặp không chạy lượt nào, chương trình đọc 0 số đo. Lúc đó phép chia tính trung bình cũng không thực hiện được, nên lỗi logic dòng 12 **kéo theo** lỗi thực thi dòng 28.

Đây là một quan sát đáng giữ: hai lỗi ở hai dòng cách nhau 16 dòng, mà ca biên nhỏ nhất làm cả hai cùng lộ ra. Đúng như Mục 3.3.1 kết luận — ca biên nhỏ nhất phân biệt rõ nhất.

**Lỗi dòng 28 có hai nguyên nhân khác nhau cùng dẫn tới một thông báo.** Mẫu số `so_luong - dem_loi` bằng 0 khi: mọi số đo đều âm (ca không hợp lệ của đề bài), hoặc vòng lặp không chạy lượt nào (hệ quả của lỗi dòng 12). Cùng một `ZeroDivisionError`, hai nguyên nhân. Thông báo lỗi chỉ nói *ở đâu*, không nói *vì sao* — đúng Khối 8 của Mục 6.1.1.

**Lệnh `continue` ở dòng 17 là lệnh đúng, không phải lỗi.** Số đo âm là lỗi cảm biến và phải bỏ qua chứ không được dừng việc đếm. Dùng `break` ở đó mới là lỗi, và đó là lỗi `L3.2-9`. Bài này cố ý đặt một lệnh **đúng** ở chỗ dễ nghi ngờ, để người giải phải phân biệt chỗ sai thật với chỗ trông lạ.

## Quy trình năm bước cho lỗi dòng 12

| Bước | Việc làm |
|---|---|
| 1. Tái lập | Một số đo duy nhất 45,0 °C — bộ nhỏ nhất còn gây ra lỗi |
| 2. Đọc thông báo | Không có thông báo nào ở bộ ba số đo; ở bộ một số đo thì có `ZeroDivisionError`, nhưng nó trỏ dòng 28 chứ không trỏ dòng 12 |
| 3. Khoanh vùng | In `chi_so` ở đầu thân vòng lặp; thấy nó bắt đầu từ 1 chứ không từ 0 |
| 4. Bảng vết | Bảng vết cho thấy lượt đầu tiên xử lý số đo thứ hai |
| 5. Sửa | Đổi `range(1, so_luong)` thành `range(so_luong)`, chạy lại cả ba bộ ca |

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 3 số đo 45 · 72,5 · 85 °C | 1 bình thường, 1 cảnh báo, 1 nguy hiểm; trung bình 67,5 °C. Bản còn lỗi cho 0 · 1 · 1 và 78,75 °C |
| Biên | 1 số đo 45 °C | 1 bình thường; trung bình 45,0 °C. Bản còn lỗi đọc **0** số đo và không tính được trung bình |
| Không hợp lệ | 2 số đo đều âm | 2 số đo lỗi; phép chia tính trung bình không thực hiện được, phải kiểm trước |
