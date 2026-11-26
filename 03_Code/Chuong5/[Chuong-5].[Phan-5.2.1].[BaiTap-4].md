# Lời giải Bài tập 5.4

- Chương 5, Mục 5.2.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.2.1].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | Nồng độ kiểu số thực, đơn vị µg/m³, miền từ 0 đến 1 000 |
| Xử lý | Chặn nồng độ ngoài miền; duyệt các khoá của từ điển và giữ khoá cuối cùng mà nồng độ còn lớn hơn hoặc bằng cận dưới |
| Đầu ra | Tên mức kiểu chuỗi, một trong sáu giá trị |

## Kết quả

| Nồng độ | Tên mức | Vì sao |
|---|---|---|
| 43,67 µg/m³ | `kem` | nằm giữa cận dưới 35,5 và 55,5 |
| 35,50 µg/m³ | `kem` | đúng bằng cận dưới của mức đó |
| 35,40 µg/m³ | `trung binh` | nhích xuống dưới cận dưới thì về mức trước |
| 300,0 µg/m³ | `nguy hai` | vượt cận dưới của mức cuối |

## Bảng so số phép so hai cách

| Số dòng bảng | Duyệt danh sách | Tra từ điển |
|---|---|---|
| 6 | 6 | 1 |
| 500 | 500 | 1 |
| 50 000 | 50 000 | 1 |

Cột thứ ba **không đổi**; cột thứ hai bằng đúng số dòng bảng, vì khoá cần tìm là khoá cuối cùng.

## Điểm chính của bài

Bảng trên đếm **phép so**, không đo thời gian, và đó là một lựa chọn có chủ ý. Số phép so là một đại lượng của thuật toán: nó không phụ thuộc máy, không phụ thuộc nhiễu, và lặp lại được tuyệt đối. Tệp kiểm chứng khẳng định nó bằng một vòng lặp qua cả ba quy mô, nên ca kiểm thử này không bao giờ thất bại thất thường.

Thời gian chạy thì khác: [[b-ss521]] của Mục 5.2.1 cho thấy tỉ lệ ở quy mô 50 000 đo được 15 591 ở một lần chạy và 22 577 ở lần khác. Hai bảng nói cùng một điều — O(1) so với O(n) — nhưng bảng đếm phép so nói chắc chắn hơn.

Bài học về cách chứng minh một kết luận về độ phức tạp: đếm phép toán khi đếm được, đo thời gian khi không đếm được. Phép đếm cho một con số chính xác; phép đo cho một con số kèm nhiễu, nên nó cần đo lại nhiều lần và chỉ kết luận về bậc, không kết luận về con số.

Về hàm `ten_muc`: nó duyệt mọi khoá rồi giữ khoá cuối cùng thoả điều kiện, chứ không dừng ở khoá đầu tiên. Lý do: các khoá xếp theo cận dưới tăng dần, nên khoá cuối cùng thoả `nong_do >= can_duoi` là khoá đúng. Cách này phụ thuộc thứ tự khai báo của từ điển, mà Python giữ đúng thứ tự khai báo — tệp kiểm chứng ghi điều đó thành một khẳng định riêng ở Ví dụ 3.

Ba cách tra một khoá không có cho ba hành vi khác nhau, và đó là nội dung ca ngoại lệ:

| Cách tra | Khoá không có cho |
|---|---|
| `can_duoi["cuc xau"]` | `KeyError: 'cuc xau'` |
| `can_duoi.get("cuc xau", -1.0)` | −1,0, một giá trị nói được là không tìm thấy |
| `can_duoi.get("cuc xau")` | `None`, không báo gì |

Cách thứ ba là lỗi `L4.1-3` của Mục 4.1.1 trở lại: một hàm trả `None` và lỗi chỉ nổ ra ở dòng dùng kết quả.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 43,67 µg/m³ | `kem`; trùng kết quả tra bằng duyệt danh sách |
| Biên | 35,5 µg/m³, đúng cận dưới | `kem`; 35,4 thì về `trung binh` |
| Không hợp lệ | Khoá không có | Ba cách tra cho `KeyError`, −1,0 và `None` |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
