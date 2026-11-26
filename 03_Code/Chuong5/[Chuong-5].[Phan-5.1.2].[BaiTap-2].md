# Lời giải Bài tập 5.2

- Chương 5, Mục 5.1.2 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.1.2].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Bộ dữ liệu phải chọn

Chuỗi **toàn số âm**, chẳng hạn −5,0 · −12,0 · −3,0.

| Bộ dữ liệu | Bản sai cho | Bản đúng cho | Lỗi có lộ ra |
|---|---|---|---|
| Có cả số dương lẫn số âm | 72,5 | 72,5 | **không** |
| Toàn số âm | **0,0** | −3,0 | **có** |
| Danh sách rỗng | 0,0 | `ValueError` | có |

## Điểm chính của bài

Kết quả 0,0 là vô lý theo một cách kiểm được ngay: **không phần tử nào** của chuỗi bằng 0. Tệp kiểm chứng ghi điều đó thành một vòng lặp khẳng định, nên lỗi phát hiện được mà không cần biết đáp án đúng là bao nhiêu.

Nguyên nhân: giá trị khởi tạo 0,0 không thuộc dữ liệu. Nó đóng vai một phần tử ngầm mà đề bài không cho, và nó thắng mọi so sánh với số âm. Quy tắc chung: **giá trị khởi tạo của biến cực trị phải lấy từ chính dữ liệu**, tức `day[0]`.

Đây đúng là lỗi của Bài tập 1.8 ở dạng mã nguồn. Ở Chương 1, bảng vết tính tải lớn nhất trên dầm khởi tạo từ phần tử **cuối** thay vì phần tử đầu, cho 56,0 kN thay vì 49,0 kN. Hai lỗi khác nhau ở chi tiết nhưng cùng một gốc: phép khởi tạo không khớp đặc tả.

Một phát hiện đáng ghi về trường hợp danh sách rỗng. Bản sai cho 0,0 và **không báo gì**; bản đúng phát sinh `ValueError`. Nghĩa là bản đúng không chỉ cho kết quả đúng hơn mà còn **an toàn hơn**: nó từ chối trả lời khi câu hỏi không có câu trả lời. Danh sách rỗng không có cực đại, nên mọi con số trả về đều là bịa. Hàm `max` có sẵn của Python cũng xử sự như vậy.

Bài học về cách chọn ca kiểm thử: bộ dữ liệu "có cả số dương lẫn số âm" trông đa dạng hơn bộ "toàn số âm", nhưng nó không bắt được lỗi. Số lượng và vẻ đa dạng của dữ liệu không quyết định; cái quyết định là dữ liệu có đi qua **chỗ sai** hay không. Ở đây chỗ sai là phép so với 0, nên ca phải là ca mà mọi phần tử đều nhỏ hơn 0.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 45 · −5 · 72,5 · −12 · 38 | Hai bản cùng cho 72,5; lỗi không lộ ra |
| Biên | −5 · −12 · −3 | Bản sai 0,0; bản đúng −3,0; không phần tử nào bằng 0 |
| Không hợp lệ | Danh sách rỗng | Bản sai 0,0 không báo gì; bản đúng `ValueError`, an toàn hơn |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
