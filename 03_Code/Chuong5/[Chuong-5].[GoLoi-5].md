# Lời giải Bài gỡ lỗi GL5

- Chương 5 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-5].[GoLoi-5].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Đoạn mã sai | Thông báo hoặc biểu hiện | Cách sửa |
|---|---|---|---|---|
| 3 | cú pháp | `def doc_so_do(duong_dan)` thiếu dấu hai chấm | `SyntaxError: expected ':'` | Thêm dấu hai chấm |
| 12 | thực thi | `doc_so_do("pm25_ngay.txt")` dùng đường dẫn tương đối | `FileNotFoundError` khi chạy từ một thư mục khác | Dựng đường dẫn từ vị trí tệp mã nguồn |
| 16 | logic | `for chi_so in range(1, len(ngay))` | **không có**; trung bình ra 42,37 thay vì 43,67 | `range(len(ngay))`, hoặc duyệt trực tiếp `for so_do in ngay` |

Sau khi sửa đủ ba lỗi: trung bình **43,67 µg/m³** và **7 giờ** vượt ngưỡng.

## Điểm chính của bài

**Lỗi dòng 16 chỉ làm sai một trong hai con số.** Đây là điểm đáng nhớ nhất của bài.

| Đại lượng | Bản còn lỗi | Bản đã sửa | Có bộc lộ lỗi |
|---|---|---|---|
| Nồng độ trung bình | 42,37 | 43,67 | **có**, lệch 3,0 % |
| Số giờ vượt ngưỡng | 7 | 7 | **không** |

Số đo bị bỏ là giờ 0 với giá trị 31,2 µg/m³ — dưới ngưỡng 50, nên nó không được đếm trong cả hai bản. Số giờ vượt ngưỡng giống hệt nhau.

Hệ quả thực tế: một báo cáo chỉ in số giờ vượt ngưỡng sẽ **không bao giờ** phát hiện ra lỗi này. Phải in cả hai con số thì lỗi mới có chỗ lộ ra. Đây là lý do Mục 5.3.2 bắt buộc báo cáo ghi đủ các đại lượng, không chọn lọc.

**Lỗi dòng 16 có hai nửa, và nửa thứ hai mới là chỗ sai thật.** Vòng lặp bỏ phần tử đầu, nhưng phép chia cuối vẫn chia cho `len(ngay)` tức 24. Nếu chia cho `len(ngay) - 1` thì kết quả là trung bình đúng của 23 số đo còn lại — vẫn không phải điều bài toán hỏi, nhưng ít sai hơn. Lỗi thật là **tử số và mẫu số không khớp nhau**.

Cách viết tránh được hẳn lỗi này: duyệt trực tiếp `for so_do in ngay` rồi chia cho `len(ngay)`. Khi không có chỉ số thì không có chỗ cho lỗi lệch một. Đó đúng là lý do Mục 5.1.2 dạy cách duyệt trực tiếp.

**Ca biên tệp một dòng bộc lộ lỗi rõ nhất.** `range(1, 1)` là dãy rỗng, nên bản còn lỗi cộng được 0 và chia cho 1, ra **0,0** — một con số không thể nhầm là đúng. Với 24 dòng thì lệch 3 %; với 1 dòng thì lệch 100 %. Đúng quy luật của Mục 3.3.1.

**Lỗi dòng 12 là lỗi của môi trường, không của thuật toán.** Chương trình chạy đúng khi thư mục làm việc trùng thư mục chứa tệp dữ liệu, và hỏng khi không trùng. Loại lỗi này không bộc lộ trên máy người viết, chỉ bộc lộ trên máy người khác hoặc trên hệ thống tự chấm. Cách sửa là dựng đường dẫn từ `__file__` chứ không dựa vào thư mục làm việc.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Tệp 24 dòng | Trung bình `43.67`; 7 giờ vượt. Bản còn lỗi cho `42.37`; số giờ vượt vẫn đúng, nên **chỉ một trong hai** con số bộc lộ lỗi |
| Biên | Tệp chỉ có một dòng | Trung bình bằng chính số đo đó. Bản còn lỗi cho `0.0` — ca bộc lộ lỗi rõ nhất |
| Không hợp lệ | Chạy chương trình từ một thư mục khác | `FileNotFoundError`; đường dẫn tương đối ở dòng 12 phải dựng từ vị trí tệp mã nguồn |
