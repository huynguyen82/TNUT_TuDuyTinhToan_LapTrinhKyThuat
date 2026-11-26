# Lời giải Bài tập 4.2

- Chương 4, Mục 4.1.2 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-4].[Phan-4.1.2].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Ba hàm của đề bài

Cả ba hàm dùng cùng một tên `LAI_SUAT`, trùng với một biến toàn cục bằng 0,008. Khác nhau duy nhất là cách dùng tên đó.

## Kết luận cho từng hàm

| Hàm | Cách dùng tên | Chạy được | Giá trị trả về | Biến toàn cục sau đó |
|---|---|---|---|---|
| `chi_doc` | chỉ đọc | có | `0.008` | 0,008, không đổi |
| `chi_gan` | chỉ gán | có | `0.02` | 0,008, **không đổi** |
| `doc_roi_gan` | đọc rồi gán | **không** | `UnboundLocalError` | 0,008, không đổi |

Thông báo lỗi nguyên văn của hàm thứ ba:

`UnboundLocalError: cannot access local variable 'LAI_SUAT' where it is not associated with a value`

## Điểm chính của bài

Quy tắc chung chỉ có một câu: **một tên được gán ở bất kỳ dòng nào trong hàm thì là biến cục bộ ở mọi dòng của hàm đó.**

Ba hàm là ba hệ quả của đúng một câu ấy. Hàm thứ nhất không gán, nên `LAI_SUAT` là biến toàn cục và đọc được. Hàm thứ hai gán, nên `LAI_SUAT` là biến cục bộ, và cái nó gán là biến cục bộ đó chứ không phải biến toàn cục. Hàm thứ ba cũng gán, nên `LAI_SUAT` là cục bộ ngay từ dòng đầu tiên — và dòng đầu tiên lại đọc nó trước khi nó có giá trị.

Hàm thứ hai là trường hợp đáng lo nhất trong ba, dù nó không báo lỗi. Người viết tưởng mình đã đổi lãi suất của cả chương trình, nhưng không. Mọi phần khác vẫn dùng 0,008, và không có thông báo nào nói điều đó.

Hàm thứ ba trông như một lỗi vô lý: dòng đọc đứng **trước** dòng gán mà vẫn báo lỗi ở dòng đọc. Nguyên nhân là Python quyết định một tên là cục bộ hay toàn cục khi **biên dịch** hàm, bằng cách xem cả thân hàm, chứ không quyết định dần theo từng dòng khi chạy.

Cách đúng là hàm `nhan_qua_tham_so`: nhận giá trị qua tham số. Nó kiểm được với mọi lãi suất, không phụ thuộc thứ tự chạy, và không có câu hỏi nào về phạm vi biến.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | Hàm chỉ đọc | `0.008`; chạy được |
| Biên | Hàm chỉ gán | `0.02` trả về, nhưng biến toàn cục vẫn 0,008 |
| Không hợp lệ | Hàm đọc rồi gán | `UnboundLocalError` báo ở dòng đọc |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
