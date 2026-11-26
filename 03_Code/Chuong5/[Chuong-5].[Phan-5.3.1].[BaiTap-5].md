# Lời giải Bài tập 5.5

- Chương 5, Mục 5.3.1 · Mức 2 · 30 phút
- Tệp kiểm chứng: `[Chuong-5].[Phan-5.3.1].[BaiTap-5].py`
- Lời giải này không in vào giáo trình.

## Bảng đặc tả ba phần

| Phần | Nội dung |
|---|---|
| Đầu vào | Tệp `04_DuLieu/pm25_ngay.txt`, mỗi dòng một số thực, đơn vị µg/m³ |
| Xử lý | Chặn tệp không có; đọc từng dòng, `strip` rồi chuyển kiểu; tính năm đại lượng của Bài tập 5.3; ghi năm dòng ra tệp mới bằng chế độ `"w"` |
| Đầu ra | Tệp `bao_cao_bt55.txt` gồm năm dòng, hai số thực hai chữ số thập phân |

## Kết quả

```
Gio cao nhat        : 8
Gio thap nhat       : 3
Trung binh ngay     : 43.67
So gio vuot nguong  : 7
Trung binh cao diem : 60.80
```

Năm con số trùng đúng Bài tập 5.3, nơi cùng chuỗi số đo được viết thẳng trong mã.

## Điểm chính của bài

Hai lần chạy liên tiếp cho đúng cùng một tệp báo cáo, **từng ký tự**. Tệp kiểm chứng khẳng định điều đó bằng cách so hai chuỗi nội dung: `TEP_RA.read_text() == lan_mot`. Đây là điều mà cách gõ tay bằng `input` không làm được, và nó là toàn bộ lý do dùng tệp.

Lý do sâu hơn: một ca kiểm thử cần dữ liệu vào **cố định**. Bàn phím không cố định, nên một chương trình đọc bàn phím không có ca kiểm thử nào theo nghĩa của Mục 4.3.1 — chỉ có những lần chạy thử do người gõ. Bài tập 4.7 đã phải lách chỗ này bằng cách cho hàm nhận nguồn dữ liệu qua tham số; tệp giải nó ở gốc.

Về thông báo lỗi khi tệp không có. Hàm `doc_so_do` kiểm `duong_dan.exists()` rồi tự phát sinh `FileNotFoundError` kèm **đường dẫn đầy đủ**, thay vì để lệnh `open` tự báo. Lý do: thông báo mặc định của `open` chỉ nêu tên tệp như người gọi đã viết, nên khi đường dẫn tương đối sai thì nó không cho biết chương trình đang tìm ở thư mục nào. Tệp kiểm chứng khẳng định tên tệp có mặt trong thông báo.

Đường dẫn dựng từ `Path(__file__).resolve().parents[2]`, tức từ vị trí của chính tệp mã nguồn, không từ thư mục đang làm việc. Nhờ vậy chương trình chạy đúng dù gọi từ thư mục nào — và đó là lỗi thực thi mà Bài gỡ lỗi GL5 cài sẵn.

Về trường hợp tệp một dòng. Đoạn cắt lát ba giờ cao điểm `day[6:9]` cho danh sách **rỗng** với một dòng dữ liệu, nên hàm `nam_dai_luong` lấy cả danh sách thay vì để phép chia gặp số 0. Quyết định này có chủ ý: báo cáo phải đủ năm dòng với mọi tệp hợp lệ, kể cả tệp một dòng. Nó cũng là một ví dụ của Khối 8 Mục 5.1.1: cắt lát không báo lỗi, nên chỗ dùng phải tự kiểm `len`.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Tệp 24 dòng | Báo cáo năm dòng; `43.67`; trùng Bài tập 5.3; hai lần chạy giống nhau từng ký tự |
| Biên | Tệp một dòng | Báo cáo vẫn đủ năm dòng; trung bình `42.60`; đoạn cao điểm rỗng nên lấy cả danh sách |
| Không hợp lệ | Tên tệp không có | `FileNotFoundError` kèm đường dẫn đầy đủ; tệp rỗng cho `ValueError` từ hàm tính |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
