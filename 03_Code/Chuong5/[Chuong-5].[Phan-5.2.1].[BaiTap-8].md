# Lời giải Bài tập 5.8

- Chương 5, Mục 5.2.1 và 5.4.1 · Mức 3 · 40 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.2.1].[BaiTap-8].py`
- Lời giải này không in vào giáo trình.

## Bốn lựa chọn và số đo xác nhận

| Tình huống | Chọn | Độ phức tạp | Đo xác nhận |
|---|---|---|---|
| 1. Lưu 720 số đo theo giờ, lấy theo chỉ số | danh sách | O(1) lấy theo chỉ số | chỉ số 0,000036 ms so với duyệt tìm 0,000078 ms |
| 2. Tra bảng 50 000 dòng theo tên | từ điển | O(1) so với O(n) | duyệt chậm hơn tra từ điển khoảng 1,4 × 10⁴ lần |
| 3. Nhân cả 72 000 số đo với một hệ số | mảng NumPy | O(n) cả hai, khác hằng số nhân | vòng lặp chậm hơn NumPy khoảng 130 lần |
| 4. Bảng có cả tên mức lẫn nồng độ | từ điển | O(1) tra theo tên | mảng NumPy buộc cùng kiểu, nên nó cho `dtype=object` |

## Phát hiện chính: ba câu hỏi chưa đủ

Khối 4 của Mục 5.2.1 cho ba câu hỏi để chọn cấu trúc dữ liệu. Áp ba câu đó vào bốn tình huống:

| Tình huống | Thứ tự là một phần nghĩa | Phần tử có tên tự nhiên | Mọi phần tử cùng kiểu | Cấu trúc đúng |
|---|---|---|---|---|
| 1 | có | không | có | danh sách |
| 2 | không | có | không | từ điển |
| 3 | **có** | **không** | **có** | **mảng NumPy** |
| 4 | không | có | không | từ điển |

Tình huống 1 và tình huống 3 cho **cùng** ba câu trả lời mà cần hai cấu trúc khác nhau. Ba câu hỏi ấy chỉ chọn được giữa danh sách và từ điển; chúng không phân biệt được danh sách với mảng NumPy, vì cả hai dùng cho dữ liệu cùng kiểu không có tên tự nhiên.

**Câu hỏi thứ tư còn thiếu: phép tính có áp lên cả chuỗi, hay chỉ lấy từng phần tử?**

Áp lên cả chuỗi thì dùng mảng NumPy; lấy từng phần tử thì dùng danh sách. Tệp kiểm chứng ghi chỗ thiếu đó thành một khẳng định trực tiếp: `bon_cau_hoi(True, False, True, False)` khác `bon_cau_hoi(True, False, True, True)`, nên câu hỏi thứ tư là câu duy nhất phân biệt được hai tình huống.

Lý do câu hỏi thứ tư nằm ngoài ba câu kia: ba câu đầu nói về **dữ liệu**, câu thứ tư nói về **việc sẽ làm với dữ liệu**. Cùng một chuỗi số đo, nếu chỉ tra từng giờ thì danh sách đủ; nếu nhân cả chuỗi với một hệ số hiệu chuẩn thì mảng nhanh hơn 130 lần. Cấu trúc dữ liệu không chọn được chỉ từ dữ liệu.

## Vì sao ca kiểm thử chỉ khẳng định chiều, không khẳng định độ lớn

Hai khẳng định về thời gian trong tệp kiểm chứng viết dạng `t_td < t_bang`, không viết `t_bang / t_td > 1000`.

Lý do đo được: bản đầu của tệp này khẳng định `t_lap / t_np > 10.0` cho tình huống 3. Chạy riêng thì tỉ lệ đo được là 133; chạy qua công cụ `kiem_tra_toan_bo.py` thì nó đo được **7,9**, nên khẳng định thất bại dù không dòng nào trong chương trình sai. Nguyên nhân là nhiễu của phép đo thời gian, cùng nguyên nhân đã buộc Chương 5 đổi sang lấy giá trị nhỏ nhất của năm lần đo, ghi ở Phụ lục 2.

Quy tắc rút ra, và nó áp cho mọi ca kiểm thử dựa trên thời gian: khẳng định **chiều** của so sánh, không khẳng định độ lớn. Chiều lặp lại được; độ lớn thì không. Khi cần một ngưỡng độ lớn, đặt nó thấp hơn số đo thật vài lần — tệp này dùng ngưỡng 100 cho một tỉ lệ đo được khoảng 1,4 × 10⁴.

Và khi đại lượng cần chứng minh **đếm** được thì đếm, đừng đo: Bài tập 5.4 chứng minh cùng kết luận O(1) so với O(n) bằng cách đếm phép so, và ca kiểm thử ở đó không bao giờ thất bại thất thường.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 720 số đo theo giờ, lấy theo chỉ số | Danh sách; lấy theo chỉ số nhanh hơn duyệt tìm |
| Biên | Bảng 50 000 dòng tra theo tên | Từ điển; thời gian tra không đổi theo quy mô bảng |
| Không hợp lệ | Bảng có cả tên mức lẫn nồng độ | Không dùng mảng NumPy; cộng mảng số với mảng chuỗi báo lỗi |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
