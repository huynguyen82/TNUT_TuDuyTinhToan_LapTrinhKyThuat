# Lời giải Bài tập 6.4

- Chương 6, Mục 6.2.1 · Mức 2 · 25 phút
- Tệp kiểm chứng: `[Chuong-6].[Phan-6.2.1].[BaiTap-4].py`
- Lời giải này không in vào giáo trình.

## Bảng ba ca, điền trước khi chạy

| Loại ca | Dữ liệu vào | Kết quả mong đợi | Nguồn của kết quả mong đợi |
|---|---|---|---|
| Thường | `f`, đoạn [2, 3] | nghiệm 2,094551 | nghiệm của `x³ − 2x − 5`, tính riêng |
| Biên | `x − 2`, đoạn [2, 3] | nghiệm đúng 2,0; **0** lượt lặp | nghiệm nằm đúng tại cận dưới, nên hàm phải trả về ngay |
| Không hợp lệ | `f`, đoạn [0, 1] | giá trị quy ước −1,0 và −1 | đặc tả: hàm không đổi dấu trên đoạn |

Ba kết quả chạy thật khớp cả ba: 2,094551 sau 34 lượt; 2,0 sau 0 lượt; −1,0 và −1.

## Số dòng đi qua

| Bộ ca | Số dòng | Tỉ lệ |
|---|---|---|
| Một ca thường | 17 trên 22 | 77,3 % |
| Thêm ca biên | 18 trên 22 | 81,8 % |
| Bộ ba loại ca | 19 trên 22 | 86,4 % |

Dòng `def` bị loại khỏi số đếm, vì nó chạy một lần lúc nạp module chứ không chạy trong mỗi lần gọi hàm. Giữ nó lại thì mọi tỉ lệ bị thiếu đúng một dòng.

## Điểm chính của bài

**Mỗi loại ca thêm vào phủ đúng thêm một dòng.** 17 → 18 → 19. Không loại nào thừa, và không loại nào thay được loại khác: ca biên phủ dòng `return a, 0`, ca không hợp lệ phủ dòng trả về giá trị quy ước khi hàm không đổi dấu. Bỏ bất kỳ loại nào thì dòng tương ứng không bao giờ chạy.

**Nhưng bộ ba loại ca vẫn chưa đủ.** Ba dòng còn lại, tức 13,6 % thân hàm, là ba nhánh tại mốc:

| Dòng chưa chạy | Nhánh | Ca cần để phủ |
|---|---|---|
| `return KHONG_TINH_DUOC, -1` đầu hàm | cận dưới không nhỏ hơn cận trên | `chia_doi(f, 3.0, 2.0)` |
| `return b, 0` | nghiệm nằm đúng tại cận trên | `x − 3` trên đoạn [2, 3] |
| `return giua, so_luot` | nghiệm nằm đúng tại một trung điểm | `x − 2.5` trên đoạn [2, 3] |

Cả ba đều là ca **tại mốc**, và hàm này có ba mốc chứ không một. Bộ ba loại ca chỉ cấp một ca biên, nên nó phủ được một mốc. Đó là lý do bước 3 của [[b-bonbuoc]] nói "với mỗi mốc sinh hai ca" chứ không nói "sinh một ca biên".

**Tệp kiểm chứng khẳng định đúng chiều, không khẳng định con số tuyệt đối duy nhất.** Khẳng định chính viết `MOT_CA < HAI_CA < BO_BA < TONG`. Nó đúng dù hàm `chia_doi` được viết lại dài hơn hay ngắn hơn, miễn cấu trúc nhánh giữ nguyên. Con số 3 dòng còn thiếu được khẳng định riêng, vì nó là số nhánh tại mốc chứ không phải số dòng.

## Ba bộ dữ liệu kiểm thử

| Trường hợp | Dữ liệu vào | Kết quả |
|---|---|---|
| Thường | đoạn [2, 3] | 17 trên 22 dòng, tức 77,3 % |
| Biên | thêm ca nghiệm tại cận dưới | 18 trên 22; một ca biên thêm đúng 1 dòng |
| Không hợp lệ | thêm ca đoạn không đổi dấu | 19 trên 22; ba dòng còn lại đều là nhánh tại mốc |

## Thang điểm

| Hạng mục | Điểm |
|---|---|
| Tính đúng đắn trên bộ dữ liệu thường | 5,0 |
| Xử lý trường hợp biên và dữ liệu không hợp lệ | 2,5 |
| Chất lượng chú thích | 1,5 |
| Cách đặt tên biến | 1,0 |
