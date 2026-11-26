# Lời giải Bài tập 6.9

- Chương 6, cả bốn tiểu mục · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.4.1].[BaiTap-9].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần, lập trước khi đọc mã

| Phần | Nội dung |
|---|---|
| Đầu vào | hai cận `a < b` của đoạn, đọc từ tệp văn bản `04_DuLieu/doan_a6.txt` |
| Xử lý | kiểm đoạn hợp lệ và kiểm `f(a)·f(b) < 0`, rồi chia đôi tới khi bề rộng đoạn nhỏ hơn sai số 10⁻¹⁰ |
| Đầu ra | `(nghiệm, số lượt lặp)`; phát sinh `ValueError` khi đoạn không hợp lệ hoặc hàm không đổi dấu |

## Bộ bốn ca, thiết kế trước khi đọc mã

| Loại ca | Dữ liệu vào | Kết quả mong đợi | Nguồn |
|---|---|---|---|
| Thường | `f`, đoạn [2, 3] | nghiệm 2,0945514815 | **phương pháp Newton**, một phương pháp khác hẳn phép chia đôi |
| Biên | `x − 2`, đoạn [2, 3] | 2,0 sau 0 lượt | nghiệm nằm đúng tại cận dưới |
| Không hợp lệ | `f`, đoạn [0, 1] | `ValueError` | dòng điều kiện áp dụng của đặc tả |
| Không hợp lệ | `f`, đoạn [3, 2] | `ValueError` | dòng "hai cận `a < b`" của đặc tả |

## Bốn cách kiểm áp lên bản do AI sinh

| Cách kiểm | Bắt được lỗi |
|---|---|
| C1 một ca thường | **không** |
| C2 bộ ba loại ca | có |
| C3 bộ ca thiết kế trước | có |
| C4 soát nguồn hằng số | có |

## Lỗi tìm được và năm bước gỡ

Bản do AI sinh có hai chỗ sai.

**Chỗ sai thứ nhất: hệ số nới đoạn 1,2 không có nguồn.** Dòng đầu hàm viết `b = b * 1.2`, kèm ý rằng nới đoạn ra cho "chắc chắn chứa nghiệm". Không tài liệu nào cho con số 1,2.

| Bước | Việc làm |
|---|---|
| 1. Tái lập | không tái lập được bằng kết quả; đoạn [2; 3,6] vẫn chứa nghiệm và vẫn đổi dấu, nên nghiệm vẫn đúng |
| 2. Đọc thông báo | không có thông báo nào |
| 3. Khoanh vùng | không dùng được, vì không có biểu hiện sai nào để khoanh |
| 4. Bảng vết | không dùng được |
| 5. Sửa | bỏ hẳn dòng nới đoạn; nếu muốn giữ thì phải ghi nguồn của hệ số |

**Chỗ sai thứ hai: không kiểm điều kiện áp dụng.** Hàm không kiểm `a < b` và không kiểm `f(a)·f(b) < 0`.

| Bước | Việc làm |
|---|---|
| 1. Tái lập | đoạn [0, 1], nơi `f` không đổi dấu |
| 2. Đọc thông báo | không có; hàm trả về một số như thể đó là nghiệm |
| 3. Khoanh vùng | so kết quả với nguồn độc lập; lệch ngay từ lượt đầu |
| 4. Bảng vết | bảng vết cho thấy `f(a)·f(giua)` dương ở mọi lượt, nên nhánh thu hẹp không bao giờ chạy |
| 5. Sửa | thêm bốn nhánh chặn ở đầu hàm và `raise ValueError` có thông điệp nêu hai cận |

## Điểm chính của bài

**Một ca thường không bắt được bản AI sinh, và lý do đáng ghi lại.** Hệ số 1,2 đưa cận trên từ 3,0 lên 3,6. Đoạn [2,0; 3,6] vẫn chứa nghiệm 2,0945 và vẫn đổi dấu, nên phép chia đôi hội tụ về đúng nghiệm ấy. Kết quả **đúng tới mọi chữ số**.

Tệp kiểm chứng ghi điều đó thành một khẳng định trực tiếp: `not _bon["C1 mot ca thuong"]`. Đây đúng là kết quả đã đo của [[b-boncach]] — C1 bắt được 0 trên 4 nhóm — nay lặp lại trên một bản mã khác.

Nhưng hệ số ấy **vẫn là một lỗi**, vì với một đoạn khác nó phá điều kiện áp dụng: đoạn [2; 2,1] nới thành [2; 2,52] thì vẫn ổn, còn một hàm có hai nghiệm gần nhau thì đoạn nới ra có thể chứa cả hai và phép chia đôi hội tụ về nghiệm người dùng không hỏi. Một lỗi không bộc lộ trên dữ liệu đang có vẫn là một lỗi.

**Quy trình năm bước không dùng được cho chỗ sai thứ nhất.** Bảng năm bước của nó có ba dòng "không dùng được", và ghi như vậy là đúng chứ không phải bỏ dở: bước 1 đòi tái lập lỗi, mà lỗi này không có biểu hiện nào để tái lập. Nó chỉ phát hiện được bằng C4, tức đọc mã và hỏi "con số này từ đâu ra".

Đây là giới hạn đã nêu ở Khối 8 Mục 6.4.1, nay gặp trên một bài cụ thể: hai nhóm lỗi nằm ngoài tầm của mọi ca kiểm thử, nên chúng cũng nằm ngoài tầm của quy trình gỡ lỗi, vì quy trình ấy bắt đầu bằng việc tái lập một biểu hiện.

**`FileNotFoundError` được chuyển thành `ValueError` có thông điệp rõ.** Hàm `doc_doan` bắt nó và phát sinh lại thành `ValueError(f"khong co tep {duong_dan}")`. Lý do: người gọi `doc_doan` quan tâm tới "dữ liệu vào không dùng được", không quan tâm tới việc nguyên nhân là tệp thiếu hay ô không phải số. Gom ba nguyên nhân vào một loại ngoại lệ ở **ranh giới của hàm** giữ cho người gọi chỉ phải bắt một loại.

**Bản khai báo dùng AI đủ ba thành phần.** Thành phần thứ ba ghi rõ hai việc: bộ bốn ca thiết kế trước đã chạy, và hệ số 1,2 đã soát nguồn mà không tìm thấy. Ghi cả việc soát **không** ra kết quả cũng là một phần của khai báo, vì nó phân biệt "đã kiểm và không có nguồn" với "chưa kiểm".

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `f(x) = x³ − 2x − 5` trên đoạn [2, 3] | nghiệm 2,094551; mọi ca thường đạt, nên một mình nó không kết luận được gì |
| Biên | nghiệm nằm đúng tại một cận | chương trình phải trả về đúng cận đó sau 0 lượt lặp |
| Không hợp lệ | đoạn không đổi dấu, và tên tệp dữ liệu không có | hai loại ngoại lệ khác nhau, bắt ở hai chỗ khác nhau; lỗi tên tệp bắt ngoài vòng lặp, lỗi đoạn bắt trong hàm |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
