# Lời giải Bài tập 5.3

- Chương 5, Mục 5.1.2 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.1.2].[BaiTap-3].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | Danh sách 24 số đo kiểu số thực, đơn vị µg/m³, mỗi số trong miền từ 0 đến 1 000; danh sách không rỗng |
| Xử lý | Chặn danh sách rỗng và số đo ngoài miền; tính cực trị kèm vị trí, trung bình, số giờ vượt ngưỡng 50, và trung bình riêng đoạn cắt lát `[6:9]` |
| Đầu ra | Hai cặp giờ–nồng độ, hai số thực hai chữ số thập phân, một số nguyên |

## Năm hàm

| Hàm | Việc | Kiểm riêng bằng |
|---|---|---|
| `kiem_day` | chặn danh sách rỗng và số đo ngoài miền | danh sách rỗng; số đo −1,0; số đo 1 001,0 |
| `gio_cao_nhat` | giờ và nồng độ cao nhất | một phần tử duy nhất cho `(0, 42.6)` |
| `gio_thap_nhat` | giờ và nồng độ thấp nhất | cùng một phần tử cho cả hai hàm |
| `trung_binh` | nồng độ trung bình | một phần tử cho chính nó |
| `dem_vuot_nguong` | số giờ vượt ngưỡng | số đo đúng bằng 50,0 và 50,1 |
| `trung_binh_cao_diem` | trung bình riêng khoảng giờ cao điểm | độ dài đoạn cắt lát bằng 3 |

## Kết quả

| Đại lượng | Giá trị |
|---|---|
| Giờ cao nhất | giờ 8, 71,5 µg/m³ |
| Giờ thấp nhất | giờ 3, 25,1 µg/m³ |
| Trung bình ngày | `43.67` µg/m³ |
| Số giờ vượt ngưỡng 50 | 7 |
| Trung bình ba giờ cao điểm sáng | `60.80` µg/m³ |

## Điểm chính của bài

Trung bình ba giờ cao điểm là 60,80 µg/m³, **vượt** ngưỡng 50, trong khi trung bình cả ngày là 43,67 µg/m³, dưới ngưỡng. Cùng một chuỗi số đo cho hai kết luận trái nhau tuỳ khoảng thời gian lấy trung bình. Tệp kiểm chứng ghi quan hệ đó thành một khẳng định: `trung_binh_cao_diem(ngay) > trung_binh(ngay)`.

Hệ quả cho báo cáo kỹ thuật: khoảng thời gian lấy trung bình là một phần của kết luận, không phải chi tiết tính toán. Một báo cáo nêu "trung bình ngày 43,67 µg/m³, dưới ngưỡng" là đúng về số mà sai về điều nó gợi ý, vì ba giờ cao điểm vượt ngưỡng và 7 trong 24 giờ cũng vậy.

Về cách tách hàm: phép chặn dữ liệu nằm ở **một** hàm riêng là `kiem_day`, và bốn hàm kia gọi nó. Nhờ vậy điều kiện chặn có một chỗ duy nhất, đúng tinh thần Mục 4.1.1: một chỗ sửa thay vì bốn.

Hàm `trung_binh_cao_diem` không gọi `kiem_day` trực tiếp mà gọi `trung_binh` trên đoạn đã cắt, nên phép chặn vẫn chạy. Chi tiết này đáng chú ý: khi đoạn cắt lát rỗng, hàm lấy cả danh sách thay vì để `trung_binh` báo lỗi, vì một tệp một dòng vẫn phải cho ra báo cáo đủ năm dòng. Đó là một quyết định có chủ ý, không phải một phép lách.

Về ca kiểm thử của trường hợp ngoại lệ: bốn hàm cùng được gọi với danh sách rỗng trong một vòng lặp, và cả bốn phải phát sinh `ValueError`. Cách viết này khẳng định một tính chất của **cả bộ hàm**, không chỉ của từng hàm, nên nó bắt được trường hợp một hàm mới thêm vào mà quên gọi `kiem_day`.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 24 số đo của Mục 5.1.1 | Giờ 8 và giờ 3; `43.67`; 7 giờ vượt; cao điểm `60.80` |
| Biên | Một số đo đúng bằng 50,0 | Không đếm là vượt; số đo 50,1 thì đếm |
| Không hợp lệ | Danh sách rỗng | Cả bốn hàm phát sinh `ValueError`, nên khoanh vùng được |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
