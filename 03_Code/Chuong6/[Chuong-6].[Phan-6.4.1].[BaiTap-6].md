# Lời giải Bài tập 6.6

- Chương 6, Mục 6.4.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.4.1].[BaiTap-6].py`
- Lời giải này không in vào giáo trình.

## Bốn đoạn và nhóm lỗi của từng đoạn

| Đoạn | Nội dung | Nhóm | Chạy một lần có phát hiện được |
|---|---|---|---|
| A | `numpy.trapz(day, dx=1.0)` | **2** — tên hàm thư viện đã thôi dùng | **không** |
| D | `nguyen_gia // so_nam` | **3** — trộn kiểu im lặng | **không** |
| G | `return 1.15   # theo tieu chuan` | **4** — hằng số không có nguồn | **không** |
| J | đệ quy chia đôi không có điều kiện dừng | **1** — thiếu điều kiện áp dụng | **có** |

Chạy một lần trên bộ dữ liệu thường phát hiện được **1 trên 4** đoạn.

## Điểm chính của bài

**Đoạn J là đoạn duy nhất bị một lần chạy bắt được, và nó bị bắt vì lý do không liên quan tới lỗi thật.** Lỗi thật của nó là thiếu điều kiện áp dụng: nó không kiểm `f(a)·f(b) < 0` và không kiểm bề rộng đoạn. Cái làm nó nổ là `RecursionError` — một hệ quả, không phải nguyên nhân. Nếu đoạn J có điều kiện dừng theo bề rộng đoạn mà vẫn thiếu kiểm đổi dấu, nó sẽ chạy xong và trả về một số sai, hệt như bản AI sinh của Ví dụ 6.6.

**Đoạn A cho kết quả đúng.** Tệp kiểm chứng khẳng định `doan_a([0,1,2]) == doan_a_dung([0,1,2])` — hai tên hàm cho đúng cùng một số thực. Không ca kiểm thử nào trên kết quả bắt được nó, vì kết quả không sai. Và khi lời gọi nằm trong một module nhập vào, cảnh báo thôi dùng cũng không hiện ra. Đoạn A chỉ hỏng ở bản NumPy sau.

**Đoạn D im lặng đúng trên bộ dữ liệu của đề bài.** Với 100 000 và 10 năm, `//` và `/` cho cùng 10 000,0. Tệp kiểm chứng ghi cả hai mặt thành hai khẳng định cạnh nhau: bằng nhau với 10 năm, khác nhau với 7 năm (14 285,0 so với 14 285,714285714290). Một bộ dữ liệu chia hết che được lỗi hoàn toàn.

**Đoạn G không có gì để so.** Hệ số 1,15 là một hệ số an toàn; không có công thức toán nào cho ra 1,15, nên không có nguồn độc lập nào để tính kết quả mong đợi. Tệp kiểm chứng ghi điều đó thành một dòng trả về `False` kèm chú thích, chứ không giả vờ kiểm. Đó là cách trung thực duy nhất: nhóm 4 chỉ kiểm được bằng cách tra số hiệu tiêu chuẩn, tức cách C4 của Mục 6.4.1.

**Ba đoạn im lặng thuộc ba lý do khác nhau.** A im lặng vì **đúng**; D im lặng vì bộ dữ liệu **che** được; G im lặng vì **không có chuẩn để so**. Ba lý do ấy cần ba cách kiểm khác nhau, và đó là nội dung của [[b-boncach]].

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | đoạn D với 100 000 và 10 năm | nhóm 3; chạy một lần **không** phát hiện được, vì 100 000 chia hết cho 10 |
| Biên | đoạn A với dãy ba phần tử | nhóm 2; kết quả đúng, không cảnh báo khi gọi từ module khác |
| Không hợp lệ | đoạn J với đoạn không đổi dấu | nhóm 1; đệ quy không có điều kiện dừng nên nó báo `RecursionError` — đoạn duy nhất mà một lần chạy phát hiện được |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
