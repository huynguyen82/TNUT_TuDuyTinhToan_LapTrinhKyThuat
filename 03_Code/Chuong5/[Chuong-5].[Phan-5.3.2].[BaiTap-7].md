# Lời giải Bài tập 5.7

- Chương 5, Mục 5.3.2 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.3.2].[BaiTap-7].py`
- Lời giải này không in vào giáo trình.

## Số dòng bỏ qua theo loại

| Loại dòng | Số dòng | Vị trí trong tệp |
|---|---|---|
| Thiếu cột | 1 | dòng 100 |
| Ghi chữ thay số | 1 | dòng 301 |
| Ô trống | 3 | dòng 50, 200, 500 |
| **Tổng bỏ qua** | **5** | trên 720 dòng dữ liệu |

## Bảng ba cách xử lý ô trống

| Cách xử lý | Số dòng dùng được | Nồng độ trung bình | Giả định ngầm |
|---|---|---|---|
| Bỏ cả dòng | 715 | 49,4964 µg/m³ | giờ thiếu số đo không tồn tại |
| Điền giá trị giờ liền trước | 720 | 49,4764 µg/m³ | nồng độ không đổi trong một giờ |
| Nội suy hai giá trị kề | 720 | 49,4708 µg/m³ | nồng độ biến đổi đều giữa hai lần đo |
| *Coi là số 0* | *720* | *49,1526 µg/m³* | *giờ thiếu số đo có nồng độ bằng 0* — **không được dùng** |

Chênh lệch giữa ba cách đầu là 0,026 µg/m³, tức 0,05 %.

## Cách nào nên dùng, và vì sao

**Nội suy hai giá trị kề.** Lý do không nằm ở con số.

Ba cách đầu cho ba số chênh nhau 0,05 %, nên nếu chỉ so con số thì không có căn cứ nào để chọn. Căn cứ nằm ở cột thứ tư: giả định ngầm nào đúng với vật lý của phép đo. PM2.5 là một đại lượng liên tục theo thời gian; nó không biến mất ở giờ cảm biến hỏng, và nó cũng không giữ nguyên đúng giá trị của giờ trước. Nội suy là giả định gần với thực tế nhất trong ba.

Cách bỏ dòng có một nhược điểm riêng mà bảng trên không thể hiện: nó làm **số dòng** đổi, từ 720 xuống 715. Mọi đại lượng tính theo số dòng — chẳng hạn "số giờ vượt ngưỡng trong tháng" — từ đó mất mẫu số chung với các tháng khác. Hai tháng, một tháng 720 dòng và một tháng 700 dòng dùng được, không so trực tiếp được bằng số đếm.

Cách điền giá trị trước có một điểm yếu cụ thể, và tệp kiểm chứng đo nó: với ô trống ở **dòng đầu tiên** của tệp, không có giá trị nào để điền, nên cách này bỏ dòng đó và cho 719 dòng thay vì 720. Nội suy thì vẫn cho 720, vì nó lấy giá trị kề phía sau. Nghĩa là cách điền trước không giữ được tính chất "luôn cho đủ số dòng" mà nó hứa.

## Vì sao chênh lệch nhỏ vẫn quan trọng

Cả ba giá trị nằm trong khoảng từ 49,47 tới 49,50 µg/m³, tức **sát dưới** ngưỡng 50. Tệp kiểm chứng ghi điều đó thành một khẳng định cho cả ba.

Với tháng này, ba cách cùng cho kết luận "không vượt ngưỡng", nên chênh lệch 0,05 % không đổi gì. Với một tháng khác, dữ liệu lệch lên chừng 1 %, ba cách có thể rơi vào hai phía ngưỡng và cho **hai kết luận trái nhau**: một cách báo tháng đó vượt ngưỡng, cách khác báo không.

Nói cách khác, chênh lệch nhỏ của phép tính trung gian trở thành chênh lệch lớn của kết luận khi kết quả nằm sát một ngưỡng. Đó là lý do báo cáo phải ghi cách xử lý ô trống cùng số dòng đã bỏ: người đọc cần biết kết luận đứng sát ngưỡng cỡ nào, và nó dựa trên giả định nào.

## Cách không được dùng

Coi ô trống là số 0 cho 49,1526 µg/m³, thấp hơn **cả ba** cách kia, và không báo gì. Lỗi này nặng theo hai nghĩa: nó kéo kết quả theo một chiều cố định, và nó im lặng. Ô trống nghĩa là "không có số đo"; số 0 là một số đo hợp lệ nói rằng không khí sạch tuyệt đối. Hai điều đó không được lẫn vào nhau.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Tệp 720 dòng | `49.4964` với 715 dòng; `49.4764` và `49.4708` với 720 dòng |
| Biên | Ô trống ở dòng đầu | Cách điền trước cho 719 dòng; nội suy cho 720; không cách nào báo lỗi |
| Không hợp lệ | Coi ô trống là 0 | `49.1526`, thấp hơn cả ba cách kia, không báo gì |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
