# Lời giải Bài tập 2.6

- Chương 2, Mục 2.3.1 · Mức 2 · 20 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.3.1].[BaiTap-6].py`
- Lời giải này không in vào giáo trình.

## Lời giải

Một dòng phiếu dựng bằng một chuỗi định dạng ba phần:

```
f"{ten_ca:<10}{dien_nang_kwh:>8.1f} kWh"
```

Bề rộng cột đặt thành hằng số ở đầu tệp thay vì viết thẳng số 10 và 8 vào chuỗi. Lợi ích đo được: khi đổi bề rộng cột, phải sửa một dòng thay vì mọi chỗ có chuỗi định dạng.

## Hai dòng phiếu với số liệu Bài tập 1.9

```
ngay         497.5 kWh
dem          336.7 kWh
```

Hai dòng dài bằng nhau nên cột số thẳng hàng. Tệp kiểm chứng khẳng định đúng điều đó bằng cách so độ dài hai chuỗi.

## Trường hợp biên là chỗ `print` thô hỏng

Với tổng điện năng tròn là 500,0 kWh:

- Chuỗi định dạng `:>8.1f` cho `   500.0`, vẫn đúng tám ký tự và vẫn thẳng cột.
- Lệnh `print` thô in giá trị 500.0 thành `500.0`, nhưng nếu giá trị là số nguyên 500 thì in thành `500`, lệch một ký tự và cả cột xô lệch theo.

Đây là lý do bảng đặc tả phải ghi số chữ số thập phân, và là lý do hệ thống tự chấm so chuỗi chứ không so giá trị.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `ngay` và 497.5 | `ngay         497.5 kWh` |
| Biên | `dem` và 500.0 | `dem          500.0 kWh`, vẫn thẳng cột |
| Không hợp lệ | Tên ca dài hơn 10 ký tự | Cột bị **đẩy**, không bị cắt; phải nới bề rộng cột |

Điểm cuối đáng nhớ: đặc tả bề rộng là bề rộng **tối thiểu**, không phải bề rộng tối đa. Chuỗi dài hơn thì in đủ và đẩy phần sau, chứ Python không cắt bớt.

## Một trường hợp ngoại lệ thật

Bề rộng âm như `:>{-8}` **không** báo lỗi mà bị bỏ qua, nên không dùng được làm phép kiểm. Trường hợp thật sự bị chặn là áp đặc tả số thực lên một chuỗi: `f"{'50.03':.1f}"` cho `ValueError: Unknown format code 'f' for object of type 'str'`. Đó chính là lỗi gặp phải khi quên ép kiểu sau `input`.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
