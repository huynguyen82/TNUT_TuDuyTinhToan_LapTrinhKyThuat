# Lời giải Bài tập 1.9

- Chương 1, Mục 1.3.1 · Mức 4 · 90 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.3.1].[BaiTap-9].py`
- Lời giải này không in vào giáo trình. Bài mức 4 có nhiều cách phân rã đúng; bản dưới là một cách.

## 1. Phân rã

Tách theo đầu ra. Bài toán có bốn đầu ra, chia thành hai nhóm giống hệt nhau khác mỗi tên ca, nên đây là chỗ dùng trừu tượng hoá của Mục 1.2.2 để viết một phần chung.

| Tên phần | Đầu vào | Đầu ra | Kiểm riêng bằng |
|---|---|---|---|
| Kiểm một dòng số liệu | Bốn trường của một dòng | Hợp lệ hay không, kèm lý do | Một dòng có ca ghi sai |
| Lọc động cơ theo ca | Danh sách động cơ và tên ca | Danh sách con của ca đó | Danh sách không có động cơ nào của ca đó |
| Tính tổng và tìm lớn nhất | Danh sách con một ca | Tổng điện năng và mã lớn nhất | Nhóm rỗng, và nhóm có hai giá trị bằng nhau |

Phần thứ ba dùng chung cho cả hai ca; đó là toàn bộ lợi ích của việc phân rã ở bài này.

## 2. Bảng đặc tả ba phần

| Phần | Tên | Ý nghĩa, đơn vị, định dạng | Miền giá trị và trường hợp đặc biệt |
|---|---|---|---|
| Đầu ra | `tong_ngay`, `tong_dem` | Tổng điện năng mỗi ca, kWh, một chữ số thập phân | Ca không có động cơ nào trả về 0,0 |
| Đầu ra | `ma_ngay`, `ma_dem` | Mã động cơ tiêu thụ nhiều nhất mỗi ca, số nguyên | Hai động cơ bằng nhau thì lấy mã nhỏ hơn; ca rỗng thì không có giá trị |
| Đầu vào | `ma_dong_co` | Mã động cơ, số nguyên | Từ 1 đến 12 |
| Đầu vào | `cong_suat_kw` | Công suất danh định, kW | Từ 0,37 đến 200; ngoài miền thì báo dữ liệu không hợp lệ |
| Đầu vào | `gio_chay` | Số giờ chạy trong một ngày, h | Từ 0 đến 24; ngoài miền thì báo dữ liệu không hợp lệ |
| Đầu vào | `ca` | Ca làm việc, chuỗi | Nhận `ngay` hoặc `dem`; giá trị khác thì báo dữ liệu không hợp lệ kèm số thứ tự dòng |
| Bước xử lý | Bước 1 | Kiểm từng dòng theo miền đã khai báo | Không sinh đại lượng mới |
| Bước xử lý | Bước 2 | Với mỗi ca, lọc các động cơ thuộc ca đó | Sinh hai danh sách con |
| Bước xử lý | Bước 3 | Với mỗi danh sách con, cộng dồn điện năng và giữ mã lớn nhất | Sinh bốn đầu ra |

## 3. Lưu đồ

Mười ba khối, một vòng lặp lồng hai khối rẽ nhánh trong thân.

Khối bắt đầu dẫn tới khối nhập danh sách 12 động cơ, rồi tới khối khởi tạo bốn đại lượng tổng và hai mã lớn nhất, rồi tới khối điều kiện *Còn động cơ chưa xét?*. Nhánh Sai của khối điều kiện này dẫn tới khối xuất bốn kết quả rồi tới khối kết thúc.

Nhánh Đúng dẫn tới khối tính điện năng, rồi tới khối điều kiện *Dòng hợp lệ?*. Nhánh Sai dẫn tới khối xuất thông báo dữ liệu không hợp lệ rồi tới khối kết thúc. Nhánh Đúng dẫn tới khối điều kiện *Ca là ngay?*, từ đó hai nhánh cộng dồn vào tổng tương ứng và cập nhật mã lớn nhất tương ứng, rồi cùng dẫn tới khối tăng chỉ số, và khối này quay về khối điều kiện *Còn động cơ chưa xét?*.

Cả ba nhánh đều dẫn tới một khối kết thúc, và khối tăng chỉ số là thành phần thứ tư bắt buộc của vòng lặp.

## 4. Mã giả

```
nhập so_dong_co, ma[1..n], P[1..n] (kW), t[1..n] (h), ca[1..n]
gán tong_ngay = 0; tong_dem = 0
gán max_ngay = 0; max_dem = 0
gán ma_ngay = 0; ma_dem = 0
lặp với i từ 1 đến so_dong_co
    nếu ca[i] khác "ngay" và ca[i] khác "dem" thì
        xuất "du lieu khong hop le", i, ca[i]
        dừng
    hết nếu
    gán E = P[i] * t[i]
    nếu ca[i] = "ngay" thì
        gán tong_ngay = tong_ngay + E
        nếu E > max_ngay thì
            gán max_ngay = E
            gán ma_ngay = ma[i]
        hết nếu
    ngược lại
        gán tong_dem = tong_dem + E
        nếu E > max_dem thì
            gán max_dem = E
            gán ma_dem = ma[i]
        hết nếu
    hết nếu
hết lặp
xuất tong_ngay, ma_ngay, tong_dem, ma_dem
```

## 5. Bảng vết trên bộ rút gọn năm dòng đầu

| Lượt | `i` | `ca` | `E` (kWh) | `tong_ngay` | `tong_dem` | `ma_ngay` | `ma_dem` |
|---|---|---|---|---|---|---|---|
| trước vòng lặp | 0 | – | – | 0,0 | 0,0 | 0 | 0 |
| 1 | 1 | ngay | 60,0 | 60,0 | 0,0 | 1 | 0 |
| 2 | 2 | ngay | 90,0 | 150,0 | 0,0 | 2 | 0 |
| 3 | 3 | dem | 36,0 | 150,0 | 36,0 | 2 | 3 |
| 4 | 4 | ngay | 88,0 | 238,0 | 36,0 | 2 | 3 |
| 5 | 5 | dem | 110,0 | 238,0 | 146,0 | 2 | 5 |

Kết quả bộ rút gọn: ca ngày 238,0 kWh với động cơ số 2; ca đêm 146,0 kWh với động cơ số 5.

## 6. Đáp số trên cả 12 dòng

| Ca | Tổng điện năng | Động cơ tiêu thụ nhiều nhất |
|---|---|---|
| Ngày | 497,5 kWh | số 2 |
| Đêm | 336,7 kWh | số 5 |

Tổng hai ca bằng 834,2 kWh, đúng bằng tổng điện năng toàn phân xưởng. Đây là một phép kiểm miễn phí: hai tổng riêng phải cộng lại bằng tổng chung.

## 7. Điểm biên mà bộ rút gọn không phủ được

Trong cả tệp, ca ngày có **ba** động cơ cùng tiêu thụ đúng 90,0 kWh là mã 2, mã 8 và mã 10, vì 15,0 nhân 6 bằng 30,0 nhân 3 bằng 45,0 nhân 2 bằng 90. Quy tắc hai động cơ bằng nhau thì lấy mã nhỏ hơn chỉ có tác dụng ở chỗ này.

Bộ rút gọn năm dòng đầu chỉ chứa một trong ba động cơ đó, nên quy tắc không bao giờ được dùng tới, và một lời giải cài sai quy tắc này vẫn cho đúng đáp số trên bộ rút gọn.

Bộ dữ liệu cần thêm: ba dòng có mã 2, 8 và 10, tức ba động cơ cùng 90,0 kWh ở ca ngày. Với bộ đó, lời giải đúng cho mã 2, còn lời giải lấy mã lớn hơn hoặc lấy động cơ gặp sau cùng sẽ cho mã 10.

Đây đúng là ý của lỗi `L1.5-2` ở Mục 1.5.1: bộ dữ liệu không chứa điểm biên thì không bộc lộ được lỗi, và bảng vết trông vẫn hoàn toàn đúng.

## 8. Nối tiếp sang Chương 2

Bảng đặc tả ở phần 2 và mã giả ở phần 4 được dùng lại làm đầu vào cho bài tập đầu của Chương 2, nơi mã giả này được chuyển thành chương trình Python chạy thật. Nên giữ lại bản viết tay.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Bốn đáp số đúng trên cả 12 dòng, và bảng vết đúng trên bộ rút gọn | 5,0 |
| Xử lý đúng ca ghi sai, ca rỗng, và quy tắc hai động cơ bằng nhau | 2,5 |
| Đủ cả năm việc: phân rã, bảng đặc tả, lưu đồ, mã giả, bảng vết; lưu đồ thoả năm quy tắc nối | 1,5 |
| Chỉ ra đúng điểm biên mà bộ rút gọn không phủ được | 1,0 |
