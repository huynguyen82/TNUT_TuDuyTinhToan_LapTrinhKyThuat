# Lời giải Bài tập 3.2

- Chương 3, Mục 3.2.2 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.2.2].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Ba đoạn mã, ba lỗi

| Đoạn | Lỗi | Dòng thiếu hoặc viết sai | Bản sửa | Số lượt sau khi sửa |
|---|---|---|---|---|
| a | Thân thiếu dòng tăng biến đếm | không có dòng nào làm đổi `chi_so` | thêm `chi_so = chi_so + 1` vào cuối thân | 3 |
| b | Điều kiện dùng phép bằng | `while chi_so != 10` với bước nhảy 3 | đổi thành `while chi_so < 10` | 4 |
| c | `continue` đặt trước dòng tăng | dòng tăng bị bỏ qua ở lượt có `continue` | chuyển sang `for` với `range` | 5 |

Cả ba đoạn đều chạy mãi. Tệp kiểm chứng chạy chúng với một giới hạn số lượt để không treo, rồi khẳng định cả ba chạm giới hạn còn ba bản sửa thì dừng đúng số lượt ghi ở cột cuối.

## Vì sao đoạn b chạy mãi

Biến đếm nhận lần lượt 0, 3, 6, 9, 12, 15… và **nhảy qua** mốc 10 mà không bao giờ bằng nó. Đây đúng là lỗi `L1.3-2` đã gặp ở lưu đồ Chương 1, nay xuất hiện lại trong mã Python.

Nguyên tắc rút ra: điều kiện dừng của một vòng lặp nên dùng phép so sánh thứ tự, không dùng phép bằng, trừ khi chắc chắn biến đếm đi qua đúng giá trị mốc.

## Vì sao đoạn c chạy mãi

Lệnh `continue` bỏ qua **toàn bộ** phần còn lại của thân, kể cả dòng tăng biến đếm nếu dòng đó nằm sau. Tới lượt `chi_so` bằng 2 thì `continue` chạy, dòng tăng bị bỏ qua, nên lượt sau `chi_so` vẫn bằng 2.

Bản sửa chuyển sang `for` với `range`: ở đó dòng tăng biến đếm nằm ngầm trong `range` và `continue` không chạm tới được. Đây là lý do `for` an toàn hơn `while` khi đã biết trước số lượt.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Đoạn | Kết quả |
|---|---|---|
| Thường | a | Chạy mãi; thêm dòng tăng biến đếm; sau khi sửa chạy 3 lượt |
| Biên | b | Chạy mãi vì biến đếm nhảy qua mốc; đổi sang `<`; sau khi sửa chạy 4 lượt |
| Không hợp lệ | c | Chạy mãi từ lượt gặp `continue`; chuyển sang `for`; sau khi sửa chạy 5 lượt |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
