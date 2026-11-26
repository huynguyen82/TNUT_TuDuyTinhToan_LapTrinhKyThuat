# Lời giải Bài tập 1.8

- Chương 1, Mục 1.5.1 · Mức 3 · 45 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.5.1].[BaiTap-8].py`
- Lời giải này không in vào giáo trình.

## Quy trình năm bước

**Bước 1, lập bảng giá trị mong đợi từ bảng đặc tả, không nhìn mã giả.** Phép cộng dồn trên dãy 8,0 · 12,0 · 6,0 · 15,0 kN cho dãy tổng từng phần 8,0 rồi 20,0 rồi 26,0 rồi 41,0.

**Bước 2, lập bảng vết từ mã giả.**

**Bước 3 và 4, so hai bảng từ trên xuống, dừng ở dòng đầu tiên lệch.**

| Lượt | `tong` mong đợi (kN) | `tong` của mã giả (kN) | Khớp |
|---|---|---|---|
| trước vòng lặp | 0,0 | 8,0 | không |
| 1 | 8,0 | 16,0 | không |
| 2 | 20,0 | 28,0 | không |
| 3 | 26,0 | 34,0 | không |
| 4 | 41,0 | 49,0 | không |

Dòng đầu tiên lệch là dòng trước vòng lặp. Dòng mã giả chạy trước vòng lặp và liên quan tới `tong` chỉ có một dòng: **dòng 3**, dòng khởi tạo.

**Bước 5, sửa và kiểm lại.** Dòng 3 viết `gán tong = tai[1]` thay vì `gán tong = 0`. Sau khi sửa, bảng vết trùng khít bảng mong đợi ở cả năm dòng, tổng về 41,0 kN và kết luận về dầm đạt với tải cho phép 45 kN.

Độ lệch không đổi suốt cả bảng, luôn đúng bằng 8,0 kN tức giá trị của phần tử đầu tiên. Đó là dấu hiệu của lỗi khởi tạo, khác với lỗi lệch một vốn chỉ sai ở lượt cuối.

## Bộ dữ liệu chọn để truy vết, và lý do

Chọn chính dãy 8,0 · 12,0 · 6,0 · 15,0 kN của đề bài. Lý do: lỗi khởi tạo bộc lộ ngay ở dòng trước vòng lặp với **mọi** bộ dữ liệu không rỗng, nên không cần bộ đặc biệt nào. Tệp kiểm chứng khẳng định điều đó trên ba bộ khác nhau là một tải, hai tải và bốn tải.

Đây là điểm khác với lỗi dấu so sánh ở Mục 1.5.1, loại chỉ bộc lộ khi bộ dữ liệu có giá trị đúng bằng ngưỡng. Hai loại lỗi đòi hai cách chọn bộ dữ liệu khác nhau, và bài làm nên nói rõ sự khác nhau đó.

Vẫn nên thêm hai bộ nữa khi kiểm lại sau khi sửa:

| Trường hợp | Dữ liệu | Mã giả sai | Mong đợi | Kết luận có lật không |
|---|---|---|---|---|
| Thường | 8,0 · 12,0 · 6,0 · 15,0 kN | 49,0 kN | 41,0 kN | có, từ đạt thành không đạt |
| Biên | một tải 8,0 kN | 16,0 kN | 8,0 kN | không, cả hai đều dưới 45 kN |
| Không hợp lệ | dãy rỗng | không thực hiện được | 0,0 kN | — |

Dòng giữa đáng chú ý: ở bộ một tải, lỗi vẫn còn nguyên nhưng câu kết luận không đổi, nên bài làm nào chỉ so câu kết luận mà không so giá trị tổng thì bỏ sót lỗi. Dòng cuối cho thấy mã giả sai còn hỏng thêm một kiểu nữa trên dãy rỗng: nó truy cập phần tử đầu tiên của một dãy không có phần tử nào.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Chỉ đúng dòng 3 và nêu đúng nội dung sửa thành `gán tong = 0` | 5,0 |
| Có bộ biên và bộ dãy rỗng, kèm nhận xét kết luận không lật ở bộ biên | 2,5 |
| Hai bảng vết trình bày đặt cạnh nhau, có đủ dòng trước vòng lặp | 1,5 |
| Nêu được quy trình theo đúng năm bước, trong đó bước 1 không nhìn mã giả | 1,0 |
