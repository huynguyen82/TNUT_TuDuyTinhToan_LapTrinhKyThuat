# Lời giải Bài tập 5.9

- Chương 5, cả sáu tiểu mục · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.4.1].[BaiTap-9].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | Tệp `04_DuLieu/pm25_thang.csv`, 720 dòng ba cột `ngay,gio,pm25`; ô trống và dòng hỏng cho phép xuất hiện |
| Xử lý | Chặn tệp không có; đọc theo dòng, tách cột, phân ba loại dòng hỏng và đếm riêng từng loại; tính bốn đại lượng bằng NumPy; tra mức chất lượng theo từ điển; vẽ đồ thị đủ năm phép bắt buộc; ghi báo cáo gồm cả cách xử lý và số dòng đã bỏ |
| Đầu ra | Tệp báo cáo 13 dòng; tệp hình; bốn đại lượng kiểu số thực và một tên mức kiểu chuỗi |

## Năm hàm và ca kiểm thử riêng của từng hàm

| Hàm | Việc | Ca thường | Ca biên | Ca ngoại lệ |
|---|---|---|---|---|
| `doc_bang` | đọc tệp, trả về dãy và ba số đếm | 715 dòng, ba số đếm (1, 1, 3) | tệp chỉ có dòng tiêu đề cho dãy rỗng và (0, 0, 0) | tệp không có cho `FileNotFoundError` kèm tên tệp |
| `bon_dai_luong` | cực trị, trung bình, số giờ vượt | trung bình `49.4964` | NumPy trùng `sum`/`len` của Python | dãy rỗng cho `ValueError` |
| `ten_muc` | tra mức theo nồng độ | `49.4964` cho `kem` | 35,5 cho `kem`; 35,4 cho `trung binh` | nồng độ âm cho `ValueError` |
| `ve_do_thi` | đồ thị đủ năm phép bắt buộc | tệp trên 10 kB | bề ngang dưới 6,3 inch | — |
| `ghi_bao_cao` | ghi báo cáo có cách xử lý và số dòng bỏ | có dòng `Cach xu ly o trong` | có dòng `So gio vuot nguong` | — |

## Kết quả

```
BAO CAO CHAT LUONG KHONG KHI MOT THANG
So dong du lieu     : 720
So dong dung duoc   : 715
So dong bo qua      : 5
  thieu cot         : 1
  ghi chu thay so   : 1
  o trong           : 3
Cach xu ly o trong  : bo dong
Cao nhat            : 83.1
Thap nhat           : 25.1
Trung binh thang    : 49.4964
Muc chat luong      : kem
So gio vuot nguong  : 289
```

## Điểm chính của bài

**Số dòng bỏ qua là một phần của kết quả.** Hàm `doc_bang` trả về bốn thứ: dãy số đo và ba số đếm dòng hỏng. Đó là quyết định thiết kế quan trọng nhất của bài. Nếu hàm chỉ trả về dãy, ba số đếm hoặc bị mất hoặc phải lưu vào một biến toàn cục — và biến toàn cục làm hàm mất khả năng kiểm riêng, đúng như Mục 4.1.2 đã chỉ ra.

Báo cáo ghi cả bảy dòng về dữ liệu vào trước khi ghi một con số kết quả nào: tổng dòng, dòng dùng được, dòng bỏ qua theo ba loại, và cách xử lý ô trống. Người đọc biết con số 49,4964 dựa trên 715 trong 720 dòng, chứ không phải trên toàn bộ tháng.

**Trung bình tháng che mất số giờ vượt ngưỡng, lần thứ hai trong chương.** Trung bình 49,4964 µg/m³ không vượt ngưỡng 50, nhưng **289** trong 715 giờ vượt ngưỡng, tức 40 % số giờ. Tệp kiểm chứng ghi điều đó thành ba khẳng định cạnh nhau: trung bình dưới ngưỡng; khoảng cách tới ngưỡng dưới 1 µg/m³; và số giờ vượt lớn hơn 0.

Đây đúng là tình huống mà Mục 5.1.2 đã nêu trên dữ liệu một ngày, nay lặp lại trên dữ liệu một tháng với tỉ lệ nặng hơn nhiều. Một báo cáo chỉ nêu trung bình tháng sẽ nói "tháng này không vượt ngưỡng", trong khi hai phần năm số giờ của tháng vượt ngưỡng. Vì vậy ca biên của bài khẳng định báo cáo **phải có** dòng số giờ vượt ngưỡng.

**Trung bình sát ngưỡng làm cách xử lý ô trống trở nên quan trọng.** 49,4964 cách ngưỡng 50 đúng 0,5036 µg/m³, tức 1 %. Bài tập 5.7 đo được ba cách xử lý ô trống chênh nhau 0,026 µg/m³; chênh lệch đó nhỏ hơn khoảng cách tới ngưỡng, nên với tháng này cả ba cách cùng cho một kết luận. Nhưng biên an toàn chỉ còn 1 %, và báo cáo ghi rõ cách đã chọn chính vì biên hẹp như vậy.

**NumPy ở đây dùng cho 715 phần tử, trên quy mô hoà vốn 20 phần tử rất nhiều.** Tệp kiểm chứng khẳng định `np.mean` cho đúng cùng kết quả với `sum(day) / len(day)` của Python, tới bốn chữ số thập phân. Hai cách trùng nhau, nên việc chọn NumPy ở đây là chọn vì gọn hơn, không phải vì khác kết quả.

**Mỗi hàm chặn dữ liệu của riêng nó.** Tệp không có bị `doc_bang` chặn; dãy rỗng bị `bon_dai_luong` chặn; nồng độ âm bị `ten_muc` chặn. Ba lỗi khác nhau hiện ra ở ba hàm khác nhau, nên khi báo cáo sai thì chạy năm bộ ca kiểm thử là biết ngay hàm nào hỏng — đúng cái lợi mà Mục 4.3.1 đo được là giảm công soát từ bốn hàm xuống một.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Tệp 720 dòng, bỏ dòng có ô trống | 715 dòng; `49.4964`; mức `kem`; 5 dòng bỏ qua gồm 1 thiếu cột, 1 ghi chữ, 3 ô trống |
| Biên | Trung bình 49,4964 so với ngưỡng 50,0 | Không vượt ngưỡng, nhưng 289 trong 715 giờ vượt; báo cáo phải nêu cả hai |
| Không hợp lệ | Tệp chỉ có dòng tiêu đề | `doc_bang` cho dãy rỗng; `bon_dai_luong` phát sinh `ValueError` trước khi chia |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
