# Lời giải Bài tập 3.9

- Chương 3, Mục 2.3.1 và cả sáu tiểu mục Chương 3 · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-3].[Phan-3.3.1].[BaiTap-9].py`
- Lời giải này không in vào giáo trình. Bài mức 4 có nhiều cách tổ chức đúng.

## 1. Bảng đặc tả ba phần

| Phần | Tên | Ý nghĩa, đơn vị | Miền giá trị và trường hợp đặc biệt |
|---|---|---|---|
| Đầu ra | bốn số đếm | Số lần của từng trạng thái, số nguyên | Tổng bốn số đếm bằng số số đo hợp lệ đã xử lý |
| Đầu ra | `so_do_loi` | Số số đo lỗi đã bỏ qua, số nguyên | Số đo âm khác −1 |
| Đầu ra | `ly_do_dung` | Lý do dừng đọc, chuỗi | Một trong hai: hết số đo, hoặc gặp trạng thái dừng máy |
| Đầu vào | các số đo | Nhiệt độ vỏ máy, °C | Giá trị −1 là giá trị kết thúc, không phải số đo |
| Bước xử lý | Bước 1 | Đọc một số đo | — |
| Bước xử lý | Bước 2 | Nếu là giá trị kết thúc thì `break` | — |
| Bước xử lý | Bước 3 | Nếu âm thì đếm lỗi rồi `continue` | — |
| Bước xử lý | Bước 4 | Phân loại và đếm | — |
| Bước xử lý | Bước 5 | Nếu là `dung may` thì ghi lý do rồi `break` | — |

## 2. Chọn `while` chứ không `for`

Số lượng số đo mỗi ca khác nhau và chỉ biết khi gặp giá trị kết thúc, nên câu hỏi thứ nhất của Bài tập 3.8 trả lời *không*. Dùng `for` phải đoán số lượt, và đoán thiếu thì bỏ sót mà không báo gì.

## 3. Thứ tự kiểm trong thân quyết định kết quả

Ba bước kiểm phải theo đúng thứ tự: giá trị kết thúc, rồi số đo lỗi, rồi phân loại.

Đảo bước 2 với bước 3 thì giá trị −1 bị đếm nhầm vào số đo lỗi, vì −1 cũng là số âm. Tệp kiểm chứng khẳng định đúng điểm này: dãy chỉ có giá trị kết thúc cho `so_do_loi` bằng 0, không phải 1.

Bước 5 phải nằm **sau** bước 4, vì số đo gây dừng máy vẫn phải được đếm trước khi dừng.

## 4. Ba cấu trúc trong một vòng lặp

Bài này dùng cả `while` cho điều kiện dừng, `continue` cho số đo lỗi, và `break` cho hai lý do dừng khác nhau. Đây là lần đầu ba cấu trúc xuất hiện cùng lúc, và thứ tự của chúng là nội dung chính của bài.

## 5. Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 45 · 72,5 · 85 · −1 | 1 bình thường, 1 cảnh báo, 1 nguy hiểm, 0 dừng máy, 0 lỗi; dừng vì hết số đo |
| Biên | 45 · 120 · 50 · −1 | Dừng ngay ở 120 vì `dung may`; số đo 50 **không** được đọc |
| Không hợp lệ | 45 · −5 · 72,5 · −1 | Số đo −5 bỏ qua và đếm vào lỗi; 72,5 vẫn được xử lý |

Hai ca nữa đã kiểm: dãy rỗng và dãy chỉ có giá trị kết thúc đều cho bốn số đếm bằng 0 và lý do dừng là hết số đo.

## 6. Nối tiếp sang Chương 5

Chương trình này đọc từng số đo từ bàn phím. Chương 5 thay bằng đọc một tệp số liệu đo, và bốn số đếm chuyển thành một từ điển tra theo tên trạng thái. Bảng đặc tả ở phần 1 không đổi; chỉ bước 1 đổi nguồn dữ liệu.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
