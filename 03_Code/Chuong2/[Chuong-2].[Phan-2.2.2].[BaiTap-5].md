# Lời giải Bài tập 2.5

- Chương 2, Mục 2.2.2 · Mức 2 · 20 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.2.2].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Lời giải

Hai dòng tính, dùng đúng hai toán tử dành cho việc này:

```
so_ca_day = tong_gio // do_dai_ca
gio_du = tong_gio % do_dai_ca
```

Dòng kiểm tra in ra quan hệ `so_ca_day * do_dai_ca + gio_du == tong_gio`. Quan hệ này đúng với **mọi** cặp giá trị, nên nó là một phép kiểm miễn phí: lời giải nào làm hỏng quan hệ đó thì chắc chắn sai mà không cần biết đáp số đúng.

## Vì sao kiểm miền trước khi chia

Hàm `chia_ca` kiểm cả hai đầu vào theo miền từ 1 đến 168 trước khi thực hiện phép chia. Miền bắt đầu từ 1 chứ không từ 0, nên sau bước kiểm thì `ZeroDivisionError` không bao giờ xảy ra được.

Đây là nguyên tắc của Mục 1.1.1 áp dụng vào mã thật: khối kiểm điều kiện của một phép chia luôn đứng trước phép chia đó. Tệp kiểm chứng khẳng định cả hai mặt — hàm có kiểm thì ném `ValueError` kèm tên đại lượng sai, còn phép `24 // 0` trần thì ném `ZeroDivisionError`.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | 24 và 7 | 3 ca đầy, dư 3 giờ |
| Biên | 21 và 7 | 3 ca đầy, dư 0 giờ |
| Không hợp lệ | 24 và 0 | Báo dữ liệu không hợp lệ ở bước kiểm, trước khi chia |

Hai bộ biên nữa đáng thêm: độ dài ca **lớn hơn** tổng giờ, tức 5 và 7, cho 0 ca đầy và dư 5 giờ; và độ dài ca đúng bằng tổng giờ, tức 7 và 7, cho 1 ca đầy không dư.

## Phép kiểm theo tính chất

Tệp kiểm chứng duyệt mọi cặp trong một tập giá trị và khẳng định hai tính chất cho từng cặp: quan hệ ba đại lượng đúng, và phần dư luôn thoả `0 <= du < do_dai_ca`. Cách kiểm này mạnh hơn kiểm từng đáp số vì nó phủ nhiều cặp mà không phải viết từng đáp số ra, và nó là dạng kiểm thử trình bày đầy đủ ở Mục 6.2.2.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
