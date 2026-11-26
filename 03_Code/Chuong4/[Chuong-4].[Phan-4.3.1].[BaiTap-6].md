# Lời giải Bài tập 4.6

- Chương 4, Mục 4.3.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.3.1].[BaiTap-6].py`
- Lời giải này không in vào giáo trình.

## Lỗi cố ý

Bản sai đẩy mốc thứ ba từ 32,0 A ra 33,0 A: nhánh viết `dong_dien <= 33.0` thay vì `dong_dien <= 32.0`. Đây là một lỗi lệch mốc, đúng loại lỗi mà bài tập muốn kiểm.

## Bốn nhóm ca và kết quả

| Nhóm ca | Số đo | Bản đúng | Bản sai | Bắt được lỗi |
|---|---|---|---|---|
| Thường | 30 · 20 · 50 A | đạt | đạt | **không** |
| Biên tại mốc | 16 · 25 · 32 · 40 · 63 A | đạt | đạt | **không** |
| Biên nhích qua mốc | 16,1 · 25,1 · 32,1 · 40,1 · 63,1 A | đạt | **không đạt** | **có** |
| Ngoại lệ | −1 A | đạt | đạt | không |

## Điểm chính của bài

Kết quả trên là điểm quan trọng nhất của bài, và nó trái với dự đoán thường gặp. Dự đoán là: lỗi nằm ở một mốc, nên ca kiểm thử đặt **đúng tại** các mốc sẽ bắt được. Dự đoán đó sai.

Lý do: mốc bị đẩy ra **ngoài**, từ 32,0 lên 33,0. Số đo 32,0 A vẫn thoả `32.0 <= 32.0` ở bản đúng và `32.0 <= 33.0` ở bản sai, nên cả hai cùng trả 4,0 mm². Năm ca tại mốc đều đạt với cả hai bản.

Khoảng phân biệt hai bản là khoảng từ 32,1 đến 33,0 A: ở đó bản đúng trả 6,0 mm² còn bản sai trả 4,0 mm². Chỉ ca **nhích qua** mốc rơi vào khoảng đó.

Quy tắc rút ra, và nó mở rộng ba loại điểm biên của Mục 3.3.1: với mỗi mốc, một ca tại mốc **và** một ca nhích qua mốc. Một mốc bị kéo vào trong bị ca tại mốc bắt được; một mốc bị đẩy ra ngoài chỉ bị ca nhích qua bắt được. Không biết trước lỗi sẽ kéo vào hay đẩy ra, nên phải có cả hai.

Hệ quả thứ hai: nhóm ca thường không bắt được gì, dù ba số đo của nó trải khắp bảng. Số lượng ca không quyết định, vị trí ca mới quyết định.

Nhóm ngoại lệ cũng không bắt được lỗi này, vì bản sai vẫn chặn dòng điện ngoài miền đúng như bản đúng. Điều đó không làm nhóm ngoại lệ vô dụng: nó bắt một loại lỗi khác, loại quên chặn dữ liệu vào.

Đây cũng là cách trả lời câu TK4.5: sửa cố ý một dòng rồi chạy lại. Bộ ca ban đầu, chỉ có ba nhóm, vẫn đạt với bản sai — nên bộ ca đó không kiểm được lỗi lệch mốc, và phải bổ sung.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 30 A | Khẳng định đạt với cả hai bản |
| Biên | Năm mốc, rồi năm số đo nhích qua mốc | Năm ca tại mốc đạt với cả hai bản; nhóm nhích qua mốc không đạt với bản sai |
| Không hợp lệ | −1 A | `ValueError` ở cả hai bản; nhóm này không bắt được lỗi lệch mốc |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
