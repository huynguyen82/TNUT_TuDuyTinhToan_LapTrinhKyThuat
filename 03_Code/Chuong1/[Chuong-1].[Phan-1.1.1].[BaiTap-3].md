# Lời giải Bài tập 1.3

- Chương 1, Mục 1.1.1 · Mức 2 · 20 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.1.1].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

Lập theo đúng trình tự của Mục 1.1.1: đầu ra trước, đầu vào sau, bước xử lý cuối cùng.

| Phần | Tên | Ý nghĩa, đơn vị, định dạng | Miền giá trị và trường hợp đặc biệt |
|---|---|---|---|
| Đầu ra | `ton_that` | Tổn thất công suất trên đoạn dây, W, hai chữ số thập phân | Luôn không âm; bằng 0,00 khi dòng điện bằng 0 hoặc chiều dài bằng 0 |
| Đầu vào | `dong_dien` | Dòng điện chạy qua đường dây, A | Từ 0 đến 1 000; ngoài miền thì báo dữ liệu không hợp lệ |
| Đầu vào | `dien_tro` | Điện trở của một kilômét dây, Ω/km | Từ 0,01 đến 5,00; ngoài miền thì báo dữ liệu không hợp lệ |
| Đầu vào | `chieu_dai` | Chiều dài đoạn dây, km | Từ 0 đến 100; ngoài miền thì báo dữ liệu không hợp lệ |
| Bước xử lý | Bước 1 | Kiểm ba đầu vào theo miền đã khai báo; gặp giá trị ngoài miền thì báo dữ liệu không hợp lệ và dừng | Không sinh đại lượng mới |
| Bước xử lý | Bước 2 | Tính `ton_that = dong_dien² × dien_tro × chieu_dai` | Sinh ra `ton_that` |

## Ba điểm phải chú ý khi lập bảng

**Thứ tự hai bước xử lý là bắt buộc.** Bước kiểm đứng trước bước tính. Đặt sau thì phép tính đã chạy trên dữ liệu không hợp lệ rồi, và kết quả sai đã sinh ra trước khi có ai báo lỗi. Đây là cùng một nguyên tắc với khối kiểm điều kiện của bài toán điểm hoà vốn ở Mục 1.1.1.

**Cận dưới của điện trở không phải là 0.** Miền ghi từ 0,01 Ω/km, vì một đoạn dây thật luôn có điện trở khác 0. Ghi cận dưới bằng 0 thì bảng đặc tả chấp nhận một đoạn dây siêu dẫn, thứ không có trong phạm vi bài toán.

**Đầu ra phải ghi là luôn không âm.** Thông tin này rút ra được từ miền của ba đầu vào, và nó là một phép kiểm miễn phí: lời giải nào cho ra tổn thất âm thì chắc chắn sai mà không cần biết đáp số đúng.

## Quan hệ giữa đầu vào và đầu ra, đã kiểm bằng máy

| Khẳng định | Kết quả |
|---|---|
| `I` = 50 A, `R` = 0,25 Ω/km, `L` = 1,2 km | 750,00 W |
| Dòng điện tăng gấp đôi lên 100 A | Tổn thất tăng gấp bốn, đúng vì tổn thất tỉ lệ với bình phương dòng điện |
| Chiều dài tăng gấp đôi lên 2,4 km | Tổn thất tăng gấp đôi, đúng vì tổn thất tỉ lệ bậc nhất với chiều dài |
| `L` = 0 km | 0,00 W |
| `I` = 0 A | 0,00 W |
| `I` = −10 A | Báo dữ liệu không hợp lệ, nêu rõ tên đại lượng `dong_dien` |
| `L` = 101 km | Báo dữ liệu không hợp lệ, nêu rõ tên đại lượng `chieu_dai` |

Hai dòng giữa của bảng là hai phép kiểm theo tính chất chứ không theo giá trị. Cách kiểm này dùng được cả khi chưa biết đáp số đúng, và được dạy đầy đủ ở Mục 6.2.2.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Bảng đặc tả có đủ ba phần, đầu ra ghi đúng đơn vị W và hai chữ số thập phân | 5,0 |
| Ba miền giá trị đúng, và bước kiểm đặt trước bước tính | 2,5 |
| Lập bảng đúng trình tự đầu ra trước, đầu vào sau, bước xử lý cuối | 1,5 |
| Tên đại lượng mang nghĩa, viết không dấu theo `snake_case` | 1,0 |
