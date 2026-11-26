# Lời giải Bài tập 2.4

- Chương 2, Mục 2.2.1 · Mức 2 · 20 phút
- Tệp kiểm chứng: `[Chuong-2].[Phan-2.2.1].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Quyết định thiết kế quan trọng nhất

Đề bài yêu cầu phân biệt **ba** tình huống: đạt, không đạt, và chuỗi không ép kiểu được. Nếu để phép ép kiểu ném lỗi ra ngoài thì chương trình dừng ở tình huống thứ ba, tức chỉ phân biệt được hai tình huống đầu.

Lời giải cho hàm `ep_kieu_kich_thuoc` trả về `None` khi không ép được, thay vì để lỗi thoát ra. Nhờ vậy hàm `ket_luan_dung_sai` trả đúng một trong ba câu kết luận trong mọi trường hợp.

Đây là một lựa chọn chứ không phải quy tắc: khi bài toán yêu cầu dừng ngay lúc gặp dữ liệu sai thì để lỗi thoát ra lại đúng hơn. Cách chọn dựa vào đầu ra mà bảng đặc tả yêu cầu.

## Hai cận thuộc miền hợp lệ

Miền dung sai là từ 49,95 đến 50,05 mm, và phép so sánh viết `can_duoi <= kich_thuoc <= can_tren`, tức hai cận **thuộc** miền. Đổi sang dấu nhỏ hơn thuần thì chi tiết đo đúng 50,05 mm bị loại, trong khi bản vẽ chấp nhận nó.

Bộ dữ liệu biên 50,05 là bộ duy nhất phân biệt được hai cách viết. Bài làm nào chỉ thử 50,03 và 50,20 thì hai cách viết cho cùng kết quả, và lỗi không lộ ra.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | `50.03` | đạt |
| Biên | `50.05` | đạt, vì cận trên thuộc miền hợp lệ |
| Không hợp lệ | `50,03` | báo dữ liệu không hợp lệ |

Bốn bộ nữa đã kiểm: `49.95` đạt, `50.06` và `49.94` không đạt, chuỗi rỗng báo không hợp lệ.

## Hai chuỗi bất ngờ vẫn ép kiểu được

Chuỗi `  50.03  ` có khoảng trắng thừa hai đầu vẫn ép kiểu được, vì hàm `float` bỏ qua khoảng trắng. Chuỗi `5.003e1` viết theo ký hiệu khoa học cũng ép được và cho đúng 50,03.

Hai trường hợp này đáng biết khi đọc dữ liệu từ phiếu đo đánh máy, và chúng cho thấy phép ép kiểu dễ dãi hơn người ta tưởng; thứ nó chặn là dấu phẩy thập phân và chữ.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
