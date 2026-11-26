# Lời giải Bài tập 2.8

- Chương 2, Mục 2.4.2 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.4.2].[BaiTap-8].py`
- Lời giải này không in vào giáo trình. Bài mức 3 có nhiều cách lý giải đúng.

## Quy tắc chọn, rút thành hai câu hỏi

Gợi ý của đề bài là hai câu hỏi, và chúng đủ để quyết định cả bốn tình huống:

1. Hai giá trị là **số nguyên** hay số thực? Số nguyên thì dùng phép `==`; không có sai số biểu diễn nào để lo.
2. Một trong hai giá trị **có thể bằng 0**, hoặc bài toán đã cho sẵn một **dung sai tuyệt đối**? Có thì dùng `abs_tol`; không thì dùng `rel_tol`.

Hàm `chon_phep_so_sanh` trong tệp kiểm chứng cài đặt đúng hai câu hỏi này.

## Bốn tình huống

| Tình huống | Phép chọn | Ngưỡng | Lý giải |
|---|---|---|---|
| Hai kích thước, dung sai 0,05 mm | `math.isclose` với `abs_tol` | 0,05 | Bài toán đã cho sẵn dung sai tuyệt đối; ngưỡng phải đúng bằng dung sai đó |
| Hai tổng điện năng cỡ 500 kWh | `math.isclose` với `rel_tol` | 10⁻⁹ | Không có dung sai cho sẵn, giá trị lớn và không thể bằng 0, nên sai số tỉ lệ với độ lớn |
| Một sai lệch cỡ 10⁻¹² so với 0 | `math.isclose` với `abs_tol` | 10⁻⁹ | Một giá trị bằng 0 nên ngưỡng tương đối vô dụng |
| Hai mã động cơ, số nguyên | `==` | không cần | Số nguyên biểu diễn đúng tuyệt đối |

## Hai sai lầm hay gặp

**Lấy ngưỡng mặc định.** Gọi `math.isclose(50.02, 50.00)` không nêu ngưỡng thì hàm dùng ngưỡng tương đối mặc định rất nhỏ, và cho `False` — chi tiết bị loại dù nằm trong dung sai. Ngưỡng là thông tin của **bài toán**, lấy từ dung sai, từ cấp chính xác thiết bị đo hoặc từ bản vẽ; không phải thông tin của hàm.

**Dùng ngưỡng tương đối cho đại lượng gần 0.** Tệp kiểm chứng khẳng định `math.isclose(1e-12, 0.0)` cho `False` còn thêm `abs_tol=1e-9` cho `True`. Lý do: sai số tương đối chia cho giá trị đúng, mà giá trị đúng bằng 0 thì phép chia không có nghĩa, nên mọi sai lệch đều bị coi là lớn.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 50,02 mm và 50,00 mm, dung sai 0,05 mm | `abs_tol=0.05`; kết luận đạt |
| Biên | 1 × 10⁻¹² và 0 | `abs_tol`; ngưỡng tương đối cho `False` vì một số bằng 0 |
| Không hợp lệ | Hai mã động cơ 2 và 2 | Phép `==`; số nguyên không cần ngưỡng |

Một bộ biên nữa đã kiểm: ngưỡng bằng đúng dung sai thì giá trị ở biên vẫn được nhận, tức `math.isclose(50.05, 50.00, abs_tol=0.05)` cho `True`.

## Trường hợp bị chặn

Ngưỡng âm không có nghĩa: `math.isclose(1.0, 1.0, rel_tol=-0.1)` cho `ValueError: tolerances must be non-negative`.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
