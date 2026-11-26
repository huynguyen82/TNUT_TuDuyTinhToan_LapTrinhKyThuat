# Lời giải Bài tập 2.1

- Chương 2, Mục 2.1.1 · Mức 1 · 10 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.1.1].[BaiTap-1].py`
- Lời giải này không in vào giáo trình.

## Đoạn mã của đề bài

```
cong_suat_kw = 7.5
gio_chay = 8.0
gio_chay = 10.0
dien_nang_kwh = cong_suat_kw * gio_chay
print(dien_nang_kwh)
```

## Đáp án

Giá trị in ra là **75.0**, không phải 60.0.

Dự đoán sai thường gặp là 60.0, do đọc dòng `gio_chay = 8.0` rồi bỏ qua dòng gán đè ngay sau đó. Chênh lệch giữa hai con số là 15,0 kWh, tức 25 % so với đáp án đúng.

## Giải thích

Phép gán không phải đẳng thức mà là lệnh, và lệnh thực hiện theo đúng thứ tự viết. Dòng thứ ba đặt giá trị 10,0 vào biến `gio_chay`, xoá giá trị 8,0 trước đó. Khi dòng thứ tư chạy, biến đã mang giá trị 10,0.

Điểm then chốt: phép gán ở dòng thứ tư lấy giá trị của `gio_chay` **ngay lúc dòng đó chạy**, chứ không giữ một liên hệ nào với biến sau đó. Đó là lý do bộ dữ liệu biên cho kết quả khác hẳn.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Thứ tự dòng | Kết quả |
|---|---|---|
| Thường | Gán đè **trước** dòng tính | 75.0 |
| Biên | Gán đè **sau** dòng tính | 60.0; gán đè không ảnh hưởng vì dòng tính đã lấy giá trị cũ |
| Không hợp lệ | Dòng tính đặt **trước** cả hai phép gán | `NameError: name 'cong_suat_kw' is not defined` |

Hai hàm đầu trong tệp kiểm chứng chỉ khác nhau thứ tự hai dòng, không khác nội dung dòng nào. Đây là bằng chứng rằng thứ tự dòng là một phần của nghĩa chương trình, không phải chuyện trình bày.

## Vì sao lỗi này khó phát hiện

Chương trình chạy hết, không báo lỗi, in ra một con số đúng định dạng và nằm trong khoảng hợp lý cho một động cơ. Đây đúng là lỗi logic `L2.1-3` của Mục 2.1.1: cách phát hiện duy nhất là đối chiếu với kết quả mong đợi, theo quy trình truy vết đối chiếu của Mục 1.5.1.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
