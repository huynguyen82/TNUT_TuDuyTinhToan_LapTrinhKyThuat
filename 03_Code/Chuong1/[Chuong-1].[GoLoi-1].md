# Lời giải Bài gỡ lỗi GL1

- Chương 1 · Bài gỡ lỗi · 45 phút
- Tệp kiểm chứng: `[Chuong-1].[GoLoi-1].py`
- Lời giải này không in vào giáo trình.

## Ba lỗi

| Dòng | Loại | Chỗ sai | Cách sửa |
|---|---|---|---|
| 23 | cú pháp của mã giả | Dòng 21 mở khối `nếu` nhưng không có dòng `hết nếu` riêng; hai khối `nếu` ở dòng 21 và 23 dùng chung một dòng đóng ở dòng 25 | Thêm một dòng `hết nếu` sau dòng 22 |
| 17 | thực thi | `gán lech_A = (tong_A - trung_binh) / trung_binh * 100` chia cho `trung_binh` mà không kiểm `trung_binh` khác 0 | Bao ba dòng tính độ lệch bằng khối `nếu tong > 0 thì` |
| 7 | logic | `gán tong_B = cac_tai_B[1]` rồi vòng lặp cộng lại chính giá trị đó một lần nữa | Khởi tạo `tong_B = 0`, giống `tong_A` và `tong_C` |

## Kết quả đo được

| Bộ dữ liệu | Bản còn lỗi dòng 7 | Bản đã sửa |
|---|---|---|
| Ba pha 4+3,5+2,5 \| 5+2 \| 6+4+3 kW | tổng (10,0 · **12,0** · 13,0); lệch lớn nhất **14,29 %**; kết luận **đạt** | tổng (10,0 · 7,0 · 13,0); lệch lớn nhất **30,00 %**; kết luận **không đạt** |
| Ba pha 11,5 \| 10,0 \| 8,5 kW | — | lệch lớn nhất đúng 15,00 %; kết luận **đạt** |
| Ba pha đều 0 kW | — | dòng 17 không thực hiện được |

## Điểm chính của bài

**Lỗi dòng 7 làm kết luận đảo ngược mà không có dấu hiệu nào.** Bản còn lỗi cho 14,29 %, nằm dưới ngưỡng 15 %, nên nó kết luận tủ **đạt**. Bản đúng cho 30 %, gấp đôi ngưỡng, kết luận **không đạt**. Một lỗi khởi tạo ở một dòng làm cả báo cáo kỹ thuật nói ngược.

Đây đúng là lỗi `L1.3-3` của Mục 1.3.1 — khởi tạo biến tích luỹ bằng một phần tử dữ liệu — nay xuất hiện ở mã giả thay vì ở lưu đồ.

**Lỗi chỉ nằm ở một pha, nên bảng kết quả vẫn trông cân đối.** Pha A và pha C khởi tạo đúng bằng 0. Chỉ pha B sai. Ba tổng 10,0 · 12,0 · 13,0 trông hợp lý, ba con số cùng bậc độ lớn, không có gì bất thường để mắt bắt được. Nếu cả ba pha cùng sai thì tổng chung sẽ gấp đôi và dễ nhận ra hơn nhiều.

**Lỗi dòng 23 là lỗi cú pháp của mã giả, không phải của Python.** Mã giả không chạy trên máy nên không có trình thông dịch nào báo. Cách phát hiện duy nhất là đếm số dòng mở khối và số dòng đóng khối: hai dòng `nếu` ở dòng 21 và 23, chỉ một dòng `hết nếu` ở dòng 25. Quy tắc của Mục 1.4.1 — mọi khối `nếu` và `lặp` đều phải có dòng đóng thụt bằng dòng mở — chính là để đếm được như vậy.

Hậu quả cụ thể: không biết dòng 24 thuộc khối `nếu` của dòng 21 hay của dòng 23. Hai cách hiểu cho hai thuật toán khác nhau.

**Lỗi dòng 17 chỉ lộ ra ở ca không hợp lệ.** Với mọi bộ dữ liệu có tải, `trung_binh` khác 0 và phép chia chạy bình thường. Chỉ khi cả ba pha không mang tải thì nó mới hỏng. Đây là lý do bảng bộ dữ liệu kiểm thử bắt buộc có một ca không hợp lệ.

## Quy trình đã dùng

Quy trình truy vết đối chiếu năm bước của Mục 1.5.1:

1. Lập bảng giá trị mong đợi từ bảng đặc tả: ba tổng 10,0 · 7,0 · 13,0.
2. Lập bảng vết từ mã giả.
3. So hai bảng theo từng dòng.
4. Hai bảng lệch đầu tiên ở `tong_B`, nên vùng cần đọc là đoạn tính `tong_B`, tức dòng 7 đến dòng 10.
5. Sửa dòng 7, lập lại bảng vết, so lại.

Vùng phải đọc rút từ 30 dòng xuống 4 dòng.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Pha A 4,0 · 3,5 · 2,5; pha B 5,0 · 2,0; pha C 6,0 · 4,0 · 3,0 kW | Ba tổng 10,0 · 7,0 · 13,0 kW; độ lệch lớn nhất 30 %; kết luận không đạt |
| Biên | Pha A 11,5; pha B 10,0; pha C 8,5 kW | Độ lệch lớn nhất đúng 15 %; kết luận đạt, vì ngưỡng dùng dấu nhỏ hơn hoặc bằng |
| Không hợp lệ | Cả ba pha không mang tải | Dòng 17 không thực hiện được; phải báo dữ liệu không hợp lệ trước khi chia |
