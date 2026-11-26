# Lời giải Bài tập 1.2

- Chương 1, Mục 1.3.1 · Mức 1 · 15 phút
- Tệp kiểm chứng: `[Chuong-1].[Phan-1.3.1].[BaiTap-2].py`
- Lời giải này không in vào giáo trình.

## Lưu đồ đề bài

Tám khối, theo thứ tự: `Bắt đầu` → `Nhập dãy tải và tải cho phép` → `Khởi tạo tổng và chỉ số` → `Còn tải chưa cộng?` → `Cộng dồn một tải` → `Tổng ≤ tải cho phép?` → `Xuất kết luận` → `Kết thúc`.

## Hai quy tắc bị vi phạm

| Quy tắc | Vị trí | Mô tả vi phạm | Biểu hiện khi thực hiện |
|---|---|---|---|
| 2 | Khối `Cộng dồn một tải` | Mũi tên ra của khối quay về chính khối đó, không về khối điều kiện `Còn tải chưa cộng?` | Luồng thực hiện kẹt vĩnh viễn ở khối cộng dồn, không bao giờ tới khối kết thúc |
| 3 | Khối `Tổng ≤ tải cho phép?` | Khối điều kiện chỉ vẽ một lối ra mang nhãn `Đúng` | Khi tổng tải vượt tải cho phép, người thực hiện dừng giữa lưu đồ và không có đầu ra |

Hai vi phạm này khác nhau ở chỗ dễ lẫn: nhánh quay về **khối điều kiện** là vòng lặp hợp lệ, còn nhánh quay về **chính nó** là nhánh cụt. Tệp kiểm chứng khẳng định cả hai trường hợp.

## Phần đã vẽ lại

**Sửa vi phạm quy tắc 2.** Đổi mũi tên ra của khối `Cộng dồn một tải` để nó dẫn về khối điều kiện `Còn tải chưa cộng?`. Khi đó mỗi lượt cộng dồn một tải rồi quay lại kiểm, và điều kiện đổi giá trị sau mỗi lượt nên vòng lặp dừng được.

**Sửa vi phạm quy tắc 3.** Thêm lối ra `Sai` cho khối `Tổng ≤ tải cho phép?`, dẫn tới một khối xuất thứ hai mang nội dung `Xuất: dầm không đạt`. Khối xuất thứ hai cũng phải dẫn tới khối kết thúc, nếu không thì sửa quy tắc 3 lại đẻ ra vi phạm quy tắc 2.

Lưu đồ sau khi sửa có 9 khối, tăng một khối so với đề bài, và không còn vi phạm quy tắc nào.

## Kết quả kiểm bằng máy

| Lưu đồ | Quy tắc bị vi phạm | Số khối |
|---|---|---|
| Đề bài | 2 và 3 | 8 |
| Chỉ sửa quy tắc 2 | 3 | 8 |
| Đã sửa cả hai | không có | 9 |
| Thêm một khối bắt đầu thứ hai | 1 | 10 |

Dòng thứ hai của bảng là chỗ đáng lưu ý khi chấm: sửa một trong hai chỗ thì lưu đồ vẫn chưa hợp lệ, nên bài làm chỉ nêu một quy tắc không được tính là đúng một nửa mà là chưa đạt yêu cầu *chỉ ra hai quy tắc*.

## Các con số phụ đã kiểm

Tổng tải của dãy 8,0 · 12,0 · 6,0 · 15,0 kN bằng 41,0 kN; với tải cho phép 50 kN thì dầm đạt. Tổng đúng bằng 50,0 kN vẫn đạt vì điều kiện dùng dấu nhỏ hơn hoặc bằng; 50,1 kN thì không đạt. Dãy tải rỗng cho tổng 0,0 kN và kết luận đạt.

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Chỉ đúng cả hai quy tắc bị vi phạm và đúng vị trí | 5,0 |
| Vẽ lại đủ cả hai chỗ, trong đó nhánh `Sai` mới cũng dẫn tới khối kết thúc | 2,5 |
| Lưu đồ vẽ lại dùng đúng hình dạng khối theo bảng tra nhanh | 1,5 |
| Đặt tên khối bằng một động từ và một danh từ | 1,0 |
