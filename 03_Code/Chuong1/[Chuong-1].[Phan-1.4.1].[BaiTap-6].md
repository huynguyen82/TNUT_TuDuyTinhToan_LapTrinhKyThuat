# Lời giải Bài tập 1.6

- Chương 1, Mục 1.4.1 · Mức 2 · 20 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.4.1].[BaiTap-6].py`
- Lời giải này không in vào giáo trình.

## Mã giả tương đương lưu đồ

Mười dòng, dùng đúng bảy từ khoá của bảng tra nhanh và quy tắc thụt lề bốn khoảng trắng.

```
nhập cong_suat[1..3] (kW)
gán tong = cong_suat[1] + cong_suat[2] + cong_suat[3]
gán trung_binh = tong / 3
gán lech_max = 0
lặp với i từ 1 đến 3
    gán lech = (cong_suat[i] - trung_binh) / trung_binh * 100
    nếu tri_tuyet_doi(lech) > lech_max thì
        gán lech_max = tri_tuyet_doi(lech)
    hết nếu
hết lặp
nếu lech_max <= 15 thì
    xuất "đạt"
ngược lại
    xuất "không đạt"
hết nếu
```

Lưu ý một khác biệt có chủ ý: lưu đồ tính ba độ lệch thành ba khối xử lý riêng, còn mã giả gộp thành một vòng lặp ba lượt. Hai biểu diễn vẫn tương đương vì cho cùng mọi đầu ra; đây đúng là cái mà Mục 1.3.1 nêu khi nói lưu đồ tuần tự cần `3n + 4` khối còn vòng lặp thì không đổi theo `n`.

## Hai bảng vết đã so khớp

Bộ dữ liệu 10,0 · 7,0 · 13,0 kW, trung bình 10,0 kW.

| Lượt | Pha | `lech` (%) | `lech_max` (%) | `i < 3` |
|---|---|---|---|---|
| trước vòng lặp | – | – | 0 | Đúng |
| 1 | A | +0 | 0 | Đúng |
| 2 | B | −30 | 30 | Đúng |
| 3 | C | +30 | 30 | Sai, dừng |

Bảng vết của lưu đồ cho cùng ba giá trị độ lệch và cùng `lech_max` bằng 30 %, nên hai biểu diễn trùng nhau. Kết luận: tủ không đạt.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | `lech_max` | Kết luận |
|---|---|---|---|
| Thường | 10,0 · 7,0 · 13,0 kW | 30 % | không đạt |
| Biên | 11,5 · 10,0 · 8,5 kW | đúng 15 % | đạt |
| Không hợp lệ | 0 · 0 · 0 kW | – | bước chia cho trung bình không thực hiện được |

Trường hợp biên là chỗ quyết định của bài này: điều kiện viết `lech_max <= 15` nên độ lệch đúng bằng ngưỡng vẫn đạt. Đổi thành `lech_max < 15` thì bộ dữ liệu biên lật sang *không đạt*, trong khi hai bộ còn lại không đổi. Bài làm nào không có bộ biên thì không phát hiện được sự khác nhau giữa hai dấu so sánh. Tệp kiểm chứng còn khẳng định 11,6 · 10,0 · 8,4 kW cho kết luận *không đạt*, tức ngay sát bên kia ngưỡng.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Mã giả cho đúng ba kết luận ứng với ba bộ dữ liệu kiểm thử | 5,0 |
| Có bộ biên 15 % và lý giải đúng vai trò của dấu nhỏ hơn hoặc bằng | 2,5 |
| Dùng đúng bảy từ khoá, có đủ dòng `hết nếu` và `hết lặp`, thụt lề bốn khoảng trắng | 1,5 |
| Tên đại lượng trong mã giả khớp tên trong lưu đồ | 1,0 |
