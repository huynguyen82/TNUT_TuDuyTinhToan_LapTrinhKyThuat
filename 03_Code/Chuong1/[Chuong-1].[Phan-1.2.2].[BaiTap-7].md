# Lời giải Bài tập 1.7

- Chương 1, Mục 1.2.2 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.2.2].[BaiTap-7].py`
- Lời giải này không in vào giáo trình. Bài mức 3 có nhiều cách trình bày đúng; bảng dưới là một cách.

## Ba đặc tả riêng, viết theo khuôn sáu dòng

| Dòng | Đề 1: điện năng | Đề 2: lượng mưa | Đề 3: chi phí |
|---|---|---|---|
| Tên phần | Tổng điện năng nhóm thiết bị | Tổng lượng mưa một đợt | Tổng chi phí một đơn hàng |
| Đầu vào | Dãy điện năng từng thiết bị | Dãy lượng mưa từng ngày | Dãy chi phí từng khoản |
| Đơn vị đầu vào | kWh | mm | nghìn đồng |
| Đầu ra | Tổng và kết luận so hạn mức | Tổng và kết luận so ngưỡng | Tổng và kết luận so hạn mức |
| Đơn vị đầu ra | kWh | mm | nghìn đồng |
| Bước xử lý | Cộng dồn rồi so với ngưỡng | Cộng dồn rồi so với ngưỡng | Cộng dồn rồi so với ngưỡng |

Số dòng trùng nhau: 4 trên 6, chỉ dòng tên phần và hai dòng đơn vị là khác. Theo gợi ý của đề bài, số dòng trùng từ bốn trở lên thì gộp được.

## Đặc tả chung

| Dòng | Nội dung |
|---|---|
| Tên phần | Cộng dồn một dãy số đo rồi so tổng với một ngưỡng |
| Đầu vào | `day_so_do` là dãy số đo cùng một đại lượng; `nguong` là giá trị ngưỡng |
| Đơn vị đầu vào | `don_vi` là một tên đơn vị, dùng chung cho cả dãy và ngưỡng |
| Đầu ra | `tong` và một câu kết luận vượt hay không vượt ngưỡng |
| Đơn vị đầu ra | `don_vi`, cùng đơn vị với đầu vào |
| Bước xử lý | Bước 1 cộng dồn `day_so_do` thành `tong`; bước 2 so `tong` với `nguong` |

Ba tên đại lượng mới đặt: `day_so_do`, `don_vi`, `nguong`. Dòng đơn vị đầu vào bắt buộc phải có, nếu không thì mắc lỗi `L1.2-4`.

## Đề không khớp và lý do

Đề bài thứ tư, đếm số ngày mưa vượt ngưỡng, **không** khớp đặc tả chung ở trên. Lý do nằm ở bước xử lý: đặc tả chung cộng dồn rồi so tổng với ngưỡng một lần, còn đề thứ tư so từng phần tử với ngưỡng rồi đếm số lần vượt.

Hai đề này dùng cùng một dãy số đo 18,0 · 42,0 · 31,0 · 25,0 mm, nên khác biệt không lộ ra ở đầu vào mà chỉ lộ ra ở đầu ra. Gán bừa đề thứ tư vào đặc tả chung cho ra tổng 116,0 mm và kết luận *vượt ngưỡng*, trong khi đáp án đúng là *2 ngày vượt ngưỡng 30 mm*. Cả hai câu đều nghe hợp lý; câu thứ nhất trả lời sai câu hỏi. Đây đúng là lỗi `L1.2-6`.

Dạng thứ hai cần một đặc tả chung riêng: đếm số phần tử của một dãy số đo vượt một ngưỡng.

## Lựa chọn và lý giải

Chọn **giữ đặc tả chung** cho ba đề đầu, vì bốn điều kiện đều thoả: đã có từ hai bài toán cùng dạng trở lên; đã viết xong đặc tả riêng của từng bài trước khi gộp; số dòng trùng là 4 trên 6; và ba đề đều cùng một bước xử lý.

Con số biện minh cho lựa chọn: ba đặc tả riêng tốn 18 dòng, đặc tả chung tốn 6 dòng. Khi số đề cùng dạng tăng lên 300, ba đặc tả riêng thành 1 800 dòng còn đặc tả chung vẫn 6 dòng. Và khi phát hiện một sai sót trong cách cộng dồn, đặc tả chung chỉ phải sửa 1 chỗ thay vì 3 chỗ, nên không mắc lỗi bỏ sót như `L1.2-3`.

Nếu chỉ có hai đề đầu thì nên giữ hai đặc tả riêng, theo đúng Khối 8 của Mục 1.2.2: chỉ gộp khi bài toán thứ ba xuất hiện.

## Các giá trị đã kiểm bằng máy

| Đề bài | Tổng | Ngưỡng | Vượt ngưỡng |
|---|---|---|---|
| Điện năng | 186,0 kWh | 200,0 kWh | không |
| Lượng mưa | 116,0 mm | 100,0 mm | có |
| Chi phí | 2 450,0 nghìn đồng | 2 000,0 nghìn đồng | có |
| Số ngày mưa vượt ngưỡng 30 mm | — | — | 2 ngày |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Đặc tả chung đúng sáu dòng, ba tên đại lượng kèm đơn vị | 5,0 |
| Chỉ đúng đề không khớp và nêu đúng lý do ở bước xử lý | 2,5 |
| Lý giải lựa chọn có kèm số dòng đo được, không chỉ nói chung chung | 1,5 |
| Tên đại lượng mang nghĩa | 1,0 |
