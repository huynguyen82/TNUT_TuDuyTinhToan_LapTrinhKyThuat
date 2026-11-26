# Mã nguồn kèm giáo trình *Tư duy tính toán và lập trình kỹ thuật*

Học phần TEE109 · Trường Đại học Kỹ thuật Công nghiệp · Khoa Điện tử

## Mục tiêu

Kho này giữ toàn bộ mã in trong giáo trình và mã lời giải bài tập, để người học chạy lại được mọi ví dụ và đối chiếu lời giải của mình với một lời giải chạy được. Mọi tệp ở đây đều đã chạy thật trước khi in sách: kết quả in trong sách chính là kết quả của lần chạy ấy.

Kho không chứa đề bài. Đề bài nằm trong giáo trình và trong tài liệu thực hành; kho này chỉ chứa mã.

## Cài đặt

```
python --version          # cần 3.12 trở lên
pip install -r 03_Code/requirements.txt
python 03_Code/kiem_tra_may.py
```

Tệp `kiem_tra_may.py` in ra một bảng năm dòng. Năm dòng đều *đạt* thì máy đã đủ để chạy mọi tệp trong kho. Chương 1 đến Chương 4 chỉ cần Python; từ Chương 5 trở đi cần thêm NumPy và Matplotlib.

## Cách chạy một tệp

Chạy từ thư mục gốc của kho, không chạy từ bên trong thư mục chương, vì các tệp đọc số liệu theo đường dẫn tính từ gốc kho:

```
python "03_Code/Chuong2/[Chuong-2].[Phan-2.1.1].[ViDu-1].py"
```

Dấu ngoặc vuông trong tên tệp là một phần của tên, nên trên Windows PowerShell hãy đặt cả đường dẫn trong dấu nháy kép như trên.

## Quy ước tên tệp

- `[Chuong-N].[Phan-N.x.y].[ViDu-k].py` — ví dụ thứ *k* của mục *N.x.y*, chính là đoạn mã in trong sách.
- `[Chuong-N].[Phan-N.x.y].[BaiTap-k].py` — lời giải bài tập *k* của mục *N.x.y*.
- `[Chuong-N].[GoLoi-N].py` — chương trình có lỗi cài sẵn, dùng cho mục gỡ lỗi cuối chương.
- `[Chuong-N].[ChuongTrinhMau].py` — chương trình hoàn chỉnh của cả chương.
- Tệp `.md` cùng tên là lời giải trình bày bằng lời.
- Tệp `.in` cùng tên là dữ liệu gõ vào sẵn, dùng khi chương trình hỏi người dùng.

Mỗi tệp `.py` đều tự kiểm: chạy xong không báo lỗi nghĩa là mọi khẳng định trong tệp đều đúng.

## Cây thư mục

```
MaNguon/
├── README.md
├── 03_Code/
│   ├── kiem_tra_may.py      kiểm tra máy đã đủ công cụ chưa
│   ├── requirements.txt     danh sách thư viện
│   ├── Chuong1/               Tư duy tính toán và cách mô tả thuật toán
│   ├── Chuong2/               Chương trình Python đầu tiên
│   ├── Chuong3/               Rẽ nhánh và lặp
│   ├── Chuong4/               Hàm và cách tách bài toán
│   ├── Chuong5/               Danh sách, tệp và số liệu đo
│   └── Chuong6/               Kiểm thử, gỡ lỗi và hoàn thiện chương trình
└── 04_DuLieu/              số liệu cho Chương 1 và Chương 5
```

### Chương 1 — Tư duy tính toán và cách mô tả thuật toán

- `[Chuong-1].[GoLoi-1].py` — Gỡ lỗi GL 1: Mã giả 30 dòng tính độ lệch tải ba pha chứa đúng ba lỗi: một lỗi cú pháp của mã giả, một lỗi thực thi và một lỗi logic. Thuộc Chương 1, Bài gỡ lỗi GL1 · lời giải: `[Chuong-1].[GoLoi-1].md`
- `[Chuong-1].[Phan-1.1.1].[BaiTap-1].py` — Bài tập BT 1.1: Điền bốn ô bị xoá trong bảng đặc tả ba phần của bài toán phân xưởng, và giải thích hậu quả khi thiếu mỗi ô. Thuộc Chương 1, Mục 1.1.1 · lời giải: `[Chuong-1].[Phan-1.1.1].[BaiTap-1].md`
- `[Chuong-1].[Phan-1.1.1].[BaiTap-3].py` — Bài tập BT 1.3: Lập bảng đặc tả ba phần cho bài toán tính tổn thất công suất trên một đoạn đường dây tải điện, theo công thức tổn thất bằng bình phương dòng điện nhân điện trở một kilômét nhân chiều dài. Thuộc Chương 1, Mục 1.1.1 · lời giải: `[Chuong-1].[Phan-1.1.1].[BaiTap-3].md`
- `[Chuong-1].[Phan-1.2.2].[BaiTap-7].py` — Bài tập BT 1.7: Cho ba đề bài cùng dạng cộng dồn rồi so với ngưỡng. Thuộc Chương 1, Mục 1.2.2 · lời giải: `[Chuong-1].[Phan-1.2.2].[BaiTap-7].md`
- `[Chuong-1].[Phan-1.3.1].[BaiTap-2].py` — Bài tập BT 1.2: Cho một lưu đồ 8 khối tính tổng tải trên dầm, vi phạm hai trong năm quy tắc nối. Thuộc Chương 1, Mục 1.3.1 · lời giải: `[Chuong-1].[Phan-1.3.1].[BaiTap-2].md`
- `[Chuong-1].[Phan-1.3.1].[BaiTap-4].py` — Bài tập BT 1.4: Vẽ lưu đồ tuần tự tính tổn thất công suất trên đường dây, dựa trên bảng đặc tả của Bài tập 1.3. Thuộc Chương 1, Mục 1.3.1 · lời giải: `[Chuong-1].[Phan-1.3.1].[BaiTap-4].md`
- `[Chuong-1].[Phan-1.3.1].[BaiTap-9].py` — Bài tập BT 1.9: Từ tệp số liệu 12 động cơ của phân xưởng, tính tổng điện năng của riêng ca ngày và riêng ca đêm, và chỉ ra động cơ tiêu thụ nhiều nhất của mỗi ca. Thuộc Chương 1, Mục 1.3.1 · lời giải: `[Chuong-1].[Phan-1.3.1].[BaiTap-9].md`
- `[Chuong-1].[Phan-1.4.1].[BaiTap-6].py` — Bài tập BT 1.6: Chuyển lưu đồ kết luận cân pha của bài toán tủ phân phối thành mã giả, rồi kiểm hai biểu diễn tương đương nhau bằng cách lập bảng vết cho cả hai và so theo từng dòng. Thuộc Chương 1, Mục 1.4.1 · lời giải: `[Chuong-1].[Phan-1.4.1].[BaiTap-6].md`
- `[Chuong-1].[Phan-1.5.1].[BaiTap-5].py` — Bài tập BT 1.5: Lập bảng vết thực thi cho mã giả tính trung bình cộng của một dãy số đo nồng độ bụi, trên hai bộ dữ liệu: dãy bốn số đo và dãy rỗng. Thuộc Chương 1, Mục 1.5.1 · lời giải: `[Chuong-1].[Phan-1.5.1].[BaiTap-5].md`
- `[Chuong-1].[Phan-1.5.1].[BaiTap-8].py` — Bài tập BT 1.8: Cho mã giả 14 dòng tính tổng tải trên dầm và kết luận điều kiện bền. Thuộc Chương 1, Mục 1.5.1 · lời giải: `[Chuong-1].[Phan-1.5.1].[BaiTap-8].md`
- `[Chuong-1].[Phan-1.5.1].[ViDu-1].py` — Ví dụ 1, công cụ kiểm chứng của Chương 1: Cài đặt năm bài toán A, B, C, D, E của Chương 1 rồi khẳng định mọi đáp số sẽ in trong sách. Thuộc Chương 1, dùng cho mọi mục từ 1.1 đến 1.5
- `cong_cu_luu_do.py` — Thư viện dùng chung: Mô tả một lưu đồ bằng dữ liệu rồi kiểm năm quy tắc nối ở Bảng quy tắc của Mục 1.3.1. Thuộc Chương 1, Mục 1.3.1

### Chương 2 — Chương trình Python đầu tiên

- `[Chuong-2].[GoLoi-2].py` — Gỡ lỗi GL 2: Chương trình 24 dòng kiểm dung sai một chi tiết chứa đúng ba lỗi: một cú pháp, một thực thi, một logic. Thuộc Chương 2, Bài gỡ lỗi GL2 · lời giải: `[Chuong-2].[GoLoi-2].md`
- `[Chuong-2].[Phan-2.1.1].[BaiTap-1].py` — Bài tập BT 2.1: Dự đoán giá trị in ra của một đoạn mã có gán đè biến, rồi chạy và đối chiếu. Thuộc Chương 2, Mục 2.1.1 · lời giải: `[Chuong-2].[Phan-2.1.1].[BaiTap-1].md`
- `[Chuong-2].[Phan-2.1.1].[BaiTap-3].py` — Bài tập BT 2.3: Chuyển phần tính điện năng của mã giả Bài tập 1.9 thành chương trình Python cho một động cơ: nhập công suất và số giờ chạy, tính và in điện năng. Thuộc Chương 2, Mục 2.1.1 và 2.3.1 · lời giải: `[Chuong-2].[Phan-2.1.1].[BaiTap-3].md`
- `[Chuong-2].[Phan-2.1.1].[ViDu-1].py` — Ví dụ 1: Chuyển phần tính điện năng của mã giả Bài tập 1.9 thành chương trình Python cho một động cơ, dùng biến và phép gán. Thuộc Chương 2, Mục 2.1.1
- `[Chuong-2].[Phan-2.2.1].[BaiTap-2].py` — Bài tập BT 2.2: Cho ba đoạn mã, mỗi đoạn một lỗi. Thuộc Chương 2, Mục 2.2.1 · lời giải: `[Chuong-2].[Phan-2.2.1].[BaiTap-2].md`
- `[Chuong-2].[Phan-2.2.1].[BaiTap-4].py` — Bài tập BT 2.4: Nhận kích thước đo được dưới dạng chuỗi, ép kiểu, kiểm dung sai của chi tiết trục danh nghĩa 50,00 mm với dung sai ±0,05 mm, và in kết luận. Thuộc Chương 2, Mục 2.2.1 · lời giải: `[Chuong-2].[Phan-2.2.1].[BaiTap-4].md`
- `[Chuong-2].[Phan-2.2.1].[ViDu-2].py` — Ví dụ 2: Phiếu đo ghi kích thước chi tiết trục dưới dạng chuỗi. Thuộc Chương 2, Mục 2.2.1
- `[Chuong-2].[Phan-2.2.2].[BaiTap-5].py` — Bài tập BT 2.5: Một dây chuyền vận hành tong_gio giờ liên tục, chia thành các ca do_dai_ca giờ. Thuộc Chương 2, Mục 2.2.2 · lời giải: `[Chuong-2].[Phan-2.2.2].[BaiTap-5].md`
- `[Chuong-2].[Phan-2.2.2].[ViDu-3].py` — Ví dụ 3: Chia thời gian vận hành 24 giờ của một dây chuyền thành các ca 7 giờ, cần số ca đầy và số giờ còn dư. Thuộc Chương 2, Mục 2.2.2
- `[Chuong-2].[Phan-2.3.1].[BaiTap-6].py` — Bài tập BT 2.6: In phiếu báo điện năng của phân xưởng theo mẫu ba cột: tên ca căn trái trong 10 ký tự, tổng điện năng căn phải trong 8 ký tự với một chữ số thập phân, rồi đơn vị. Thuộc Chương 2, Mục 2.3.1 · lời giải: `[Chuong-2].[Phan-2.3.1].[BaiTap-6].md`
- `[Chuong-2].[Phan-2.3.1].[ViDu-4].py` — Ví dụ 4: Nhập kích thước đo được từ bàn phím, kiểm dung sai và in phiếu kết quả theo đúng định dạng của bảng đặc tả: kích thước hai chữ số thập phân, các cột căn phải. Thuộc Chương 2, Mục 2.3.1
- `[Chuong-2].[Phan-2.4.1].[ViDu-5].py` — Ví dụ 5: Cho thấy cách máy tính biểu diễn số thực: số 0,1 không biểu diễn đúng được trong cơ số 2, và số nguyên Python không tràn số. Thuộc Chương 2, Mục 2.4.1
- `[Chuong-2].[Phan-2.4.2].[BaiTap-7].py` — Bài tập BT 2.7: Chạy năm ví dụ sai số cho sẵn, ghi kết quả bất thường, chỉ ra nguồn sai số và đo sai số tuyệt đối cùng sai số tương đối khi đo được. Thuộc Chương 2, Mục 2.4.1 và 2.4.2 · lời giải: `[Chuong-2].[Phan-2.4.2].[BaiTap-7].md`
- `[Chuong-2].[Phan-2.4.2].[BaiTap-8].py` — Bài tập BT 2.8: Cho bốn tình huống so sánh, chọn giữa phép bằng, math.isclose với abs_tol và math.isclose với rel_tol; nêu ngưỡng cụ thể và lý giải lựa chọn. Thuộc Chương 2, Mục 2.4.2 · lời giải: `[Chuong-2].[Phan-2.4.2].[BaiTap-8].md`
- `[Chuong-2].[Phan-2.4.2].[BaiTap-9].py` — Bài tập BT 2.9: Kiểm dung sai một loạt chi tiết: nhận kích thước danh nghĩa, dung sai và số chi tiết; với mỗi chi tiết nhận kích thước đo dạng chuỗi, ép kiểu, kết luận, cộng dồn; cuối cùng in số chi tiết đạt, kích thước trung bình và sai số tương đối của trung bình so với kích thước danh nghĩa. Thuộc Chương 2, Mục 1.1.1 và cả sáu tiểu mục Chương 2 · lời giải: `[Chuong-2].[Phan-2.4.2].[BaiTap-9].md`
- `[Chuong-2].[Phan-2.4.2].[ViDu-6].py` — Ví dụ 6: Đo sai số của phép cộng dồn số thực và so sánh ba cách cộng một dãy, rồi kiểm dung sai bằng math.isclose thay cho dấu bằng. Thuộc Chương 2, Mục 2.4.2

### Chương 3 — Rẽ nhánh và lặp

- `[Chuong-3].[ChuongTrinhMau].[Buoc-1].py` — Chương trình mẫu Chương trình mẫu Chương 3, bước 1: Bản tối thiểu chạy được của chương trình theo dõi nhiệt độ một ca trực. Thuộc Chương 3, mục Chương trình mẫu
- `[Chuong-3].[ChuongTrinhMau].py` — Chương trình mẫu Chương trình mẫu Chương 3, bản đầy đủ: Theo dõi nhiệt độ một ca trực. Thuộc Chương 3, mục Chương trình mẫu
- `[Chuong-3].[GoLoi-3].py` — Gỡ lỗi GL 3: Chương trình 28 dòng đếm số lần của ba trạng thái nhiệt độ chứa đúng ba lỗi: một cú pháp, một thực thi, một logic. Thuộc Chương 3, Bài gỡ lỗi GL3 · lời giải: `[Chuong-3].[GoLoi-3].md`
- `[Chuong-3].[Phan-3.1.1].[BaiTap-1].py` — Bài tập BT 3.1: Dự đoán đầu ra của đoạn mã dùng bốn lệnh if độc lập có hai miền chồng lấn, rồi chạy đối chiếu. Thuộc Chương 3, Mục 3.1.1 · lời giải: `[Chuong-3].[Phan-3.1.1].[BaiTap-1].md`
- `[Chuong-3].[Phan-3.1.1].[BaiTap-3].py` — Bài tập BT 3.3: Phân loại trạng thái động cơ theo bốn miền nhiệt độ, dùng chuỗi elif. Thuộc Chương 3, Mục 3.1.1 · lời giải: `[Chuong-3].[Phan-3.1.1].[BaiTap-3].md`
- `[Chuong-3].[Phan-3.1.1].[BaiTap-4].py` — Bài tập BT 3.4: Tra bảng tiết diện dây theo dòng điện bằng chuỗi elif năm nhánh cộng một nhánh báo vượt bảng. Thuộc Chương 3, Mục 3.1.1 · lời giải: `[Chuong-3].[Phan-3.1.1].[BaiTap-4].md`
- `[Chuong-3].[Phan-3.1.1].[ViDu-1].py` — Ví dụ 1: Phân loại trạng thái động cơ theo bốn miền nhiệt độ, dùng chuỗi if elif else. Thuộc Chương 3, Mục 3.1.1
- `[Chuong-3].[Phan-3.1.2].[ViDu-2].py` — Ví dụ 2: Chỉ phát cảnh báo khi nhiệt độ vượt ngưỡng và động cơ đang chạy. Thuộc Chương 3, Mục 3.1.2
- `[Chuong-3].[Phan-3.2.1].[BaiTap-5].py` — Bài tập BT 3.5: Chuyển chương trình kiểm dung sai của Bài tập 2.9 sang dùng vòng lặp có đếm. Thuộc Chương 3, Mục 3.2.1 · lời giải: `[Chuong-3].[Phan-3.2.1].[BaiTap-5].md`
- `[Chuong-3].[Phan-3.2.1].[ViDu-3].py` — Ví dụ 3: Tính tổng điện năng của một loạt động cơ bằng vòng lặp có đếm. Thuộc Chương 3, Mục 3.2.1
- `[Chuong-3].[Phan-3.2.2].[BaiTap-2].py` — Bài tập BT 3.2: Cho ba vòng lặp while, chỉ ra vòng nào chạy mãi, nêu dòng còn thiếu hoặc viết sai, và sửa. Thuộc Chương 3, Mục 3.2.2 · lời giải: `[Chuong-3].[Phan-3.2.2].[BaiTap-2].md`
- `[Chuong-3].[Phan-3.2.2].[ViDu-4].py` — Ví dụ 4: Đọc liên tiếp các số đo nhiệt độ cho tới khi gặp giá trị kết thúc, không biết trước bao nhiêu số. Thuộc Chương 3, Mục 3.2.2
- `[Chuong-3].[Phan-3.2.3].[BaiTap-6].py` — Bài tập BT 3.6: Đếm số giờ PM2.5 vượt ngưỡng trong một ca, bỏ qua số đo lỗi là số âm bằng lệnh continue. Thuộc Chương 3, Mục 3.2.3 · lời giải: `[Chuong-3].[Phan-3.2.3].[BaiTap-6].md`
- `[Chuong-3].[Phan-3.2.3].[BaiTap-8].py` — Bài tập BT 3.8: Chọn giữa for, while và for có break cho bốn tình huống; nêu độ phức tạp tiệm cận và lý giải. Thuộc Chương 3, Mục 3.2.2 và 3.2.3 · lời giải: `[Chuong-3].[Phan-3.2.3].[BaiTap-8].md`
- `[Chuong-3].[Phan-3.2.3].[ViDu-5].py` — Ví dụ 5: Tra bảng tiết diện dây nhỏ nhất chịu được dòng điện cho trước, thoát vòng lặp ngay khi tìm thấy. Thuộc Chương 3, Mục 3.2.3
- `[Chuong-3].[Phan-3.3.1].[BaiTap-7].py` — Bài tập BT 3.7: Thiết kế ca kiểm thử phân biệt được hai đoạn mã khác nhau ở cận trên của range, lập bảng vết, chỉ ra đoạn sai và giải thích vì sao ca n = 100 không phân biệt được. Thuộc Chương 3, Mục 3.3.1 · lời giải: `[Chuong-3].[Phan-3.3.1].[BaiTap-7].md`
- `[Chuong-3].[Phan-3.3.1].[BaiTap-9].py` — Bài tập BT 3.9: Theo dõi nhiệt độ một ca trực: đọc số đo tới khi gặp giá trị kết thúc, phân loại theo bốn miền, đếm từng trạng thái, bỏ qua số đo lỗi, và dừng ngay khi gặp trạng thái dừng máy. Thuộc Chương 3, Mục 2.3.1 và cả sáu tiểu mục Chương 3 · lời giải: `[Chuong-3].[Phan-3.3.1].[BaiTap-9].md`
- `[Chuong-3].[Phan-3.3.1].[ViDu-6].py` — Ví dụ 6: Hai vòng lặp khác nhau đúng một ký tự ở cận trên của range. Thuộc Chương 3, Mục 3.3.1

### Chương 4 — Hàm và cách tách bài toán

- `[Chuong-4].[ChuongTrinhMau].py` — Chương trình mẫu Chương trình mẫu Chương 4: Chương trình phiếu ca trực của Chương 3, nay tách thành bộ hàm. Thuộc Chương 4, mục Chương trình mẫu
- `[Chuong-4].[GoLoi-4].py` — Gỡ lỗi GL 4: Chương trình 22 dòng tính số tháng trả hết nợ và tổng lãi đã trả chứa đúng ba lỗi: một cú pháp, một thực thi, một logic. Thuộc Chương 4, Bài gỡ lỗi GL4 · lời giải: `[Chuong-4].[GoLoi-4].md`
- `[Chuong-4].[Phan-4.1.1].[BaiTap-1].py` — Bài tập BT 4.1: Hàm thiếu lệnh return trả None; chỉ ra khoảng cách giữa dòng báo lỗi và dòng sai thật. Thuộc Chương 4, Mục 4.1.1 · lời giải: `[Chuong-4].[Phan-4.1.1].[BaiTap-1].md`
- `[Chuong-4].[Phan-4.1.1].[BaiTap-3].py` — Bài tập BT 4.3: Viết hàm tính số dư sau một tháng trả nợ, có chuỗi tài liệu, rồi gọi ba lần cho ba tháng đầu. Thuộc Chương 4, Mục 4.1.1 · lời giải: `[Chuong-4].[Phan-4.1.1].[BaiTap-3].md`
- `[Chuong-4].[Phan-4.1.1].[BaiTap-5].py` — Bài tập BT 4.5: Chuyển chương trình tra tiết diện dây của Bài tập 3.4 thành một hàm, rồi tra ba dòng điện trong một lần chạy. Thuộc Chương 4, Mục 4.1.1 · lời giải: `[Chuong-4].[Phan-4.1.1].[BaiTap-5].md`
- `[Chuong-4].[Phan-4.1.1].[ViDu-1].py` — Ví dụ 1: Định nghĩa hàm tính số dư sau một tháng trả nợ, rồi gọi lại ba lần cho ba tháng liên tiếp. Thuộc Chương 4, Mục 4.1.1
- `[Chuong-4].[Phan-4.1.2].[BaiTap-2].py` — Bài tập BT 4.2: Ba hàm dùng một tên trùng biến toàn cục theo ba cách: chỉ đọc, chỉ gán, đọc rồi gán. Thuộc Chương 4, Mục 4.1.2 · lời giải: `[Chuong-4].[Phan-4.1.2].[BaiTap-2].md`
- `[Chuong-4].[Phan-4.1.2].[ViDu-2].py` — Ví dụ 2: So hai cách lấy lãi suất vào trong hàm: đọc từ biến toàn cục và nhận qua tham số. Thuộc Chương 4, Mục 4.1.2
- `[Chuong-4].[Phan-4.1.3].[BaiTap-4].py` — Bài tập BT 4.4: Hàm tính giá trị hiện tại, lãi suất là tham số mặc định; gọi theo ba cách. Thuộc Chương 4, Mục 4.1.3 · lời giải: `[Chuong-4].[Phan-4.1.3].[BaiTap-4].md`
- `[Chuong-4].[Phan-4.1.3].[ViDu-3].py` — Ví dụ 3: Hàm tính số tháng trả hết nợ, với lãi suất là tham số có giá trị mặc định. Thuộc Chương 4, Mục 4.1.3
- `[Chuong-4].[Phan-4.2.1].[BaiTap-7].py` — Bài tập BT 4.7: Tách chương trình kiểm dung sai của Bài tập 3.5 thành bộ bốn hàm, mỗi hàm kiểm riêng được. Thuộc Chương 4, Mục 4.2.1 · lời giải: `[Chuong-4].[Phan-4.2.1].[BaiTap-7].md`
- `[Chuong-4].[Phan-4.2.1].[ViDu-4].py` — Ví dụ 4: Ba hàm nhỏ của bộ bốn hàm tách từ chương trình theo dõi ca trực của Bài tập 3.9. Thuộc Chương 4, Mục 4.2.1
- `[Chuong-4].[Phan-4.2.1].[ViDu-5].py` — Ví dụ 5: Hàm đếm của bộ bốn hàm và chương trình chính, tiếp nối ba hàm nhỏ của Ví dụ 4. Thuộc Chương 4, Mục 4.2.1
- `[Chuong-4].[Phan-4.3.1].[BaiTap-6].py` — Bài tập BT 4.6: Viết bộ ca kiểm thử bằng assert cho hàm tra tiết diện dây, rồi sửa cố ý một mốc để xác nhận bộ ca phát hiện được. Thuộc Chương 4, Mục 4.3.1 · lời giải: `[Chuong-4].[Phan-4.3.1].[BaiTap-6].md`
- `[Chuong-4].[Phan-4.3.1].[BaiTap-8].py` — Bài tập BT 4.8: Bộ bốn hàm theo dõi ca trực, đúng một hàm sai; khoanh vùng hàm sai bằng ca kiểm thử từng hàm. Thuộc Chương 4, Mục 4.3.1 · lời giải: `[Chuong-4].[Phan-4.3.1].[BaiTap-8].md`
- `[Chuong-4].[Phan-4.3.1].[BaiTap-9].py` — Bài tập BT 4.9: Chương trình tư vấn khoản vay thiết bị: số tháng trả hết, tổng lãi cộng dồn, và giá trị hiện tại của khoản trả tháng cuối. Thuộc Chương 4, cả năm tiểu mục · lời giải: `[Chuong-4].[Phan-4.3.1].[BaiTap-9].md`
- `[Chuong-4].[Phan-4.3.1].[ViDu-6].py` — Ví dụ 6: Viết ca kiểm thử bằng lệnh assert cho hàm tính giá trị hiện tại, đủ ba trường hợp thường, biên và ngoại lệ. Thuộc Chương 4, Mục 4.3.1

### Chương 5 — Danh sách, tệp và số liệu đo

- `[Chuong-5].[GoLoi-5].py` — Gỡ lỗi GL 5: Chương trình 23 dòng đọc tệp số đo một ngày rồi tính nồng độ trung bình và số giờ vượt ngưỡng, chứa đúng ba lỗi: một cú pháp, một thực thi, một logic. Thuộc Chương 5, Bài gỡ lỗi GL5 · lời giải: `[Chuong-5].[GoLoi-5].md`
- `[Chuong-5].[Phan-5.1.1].[BaiTap-1].py` — Bài tập BT 5.1: Dự đoán bốn phép cắt lát, trong đó hai phép vượt ra ngoài danh sách mà không báo lỗi. Thuộc Chương 5, Mục 5.1.1 · lời giải: `[Chuong-5].[Phan-5.1.1].[BaiTap-1].md`
- `[Chuong-5].[Phan-5.1.1].[ViDu-1].py` — Ví dụ 1: Lưu 24 số đo PM2.5 của một ngày vào một danh sách, lấy theo chỉ số và cắt lát ba giờ cao điểm sáng. Thuộc Chương 5, Mục 5.1.1
- `[Chuong-5].[Phan-5.1.2].[BaiTap-2].py` — Bài tập BT 5.2: Chỉ ra bộ dữ liệu làm đoạn mã khởi tạo biến cực đại bằng 0 cho kết quả sai; nối với Bài tập 1.8. Thuộc Chương 5, Mục 5.1.2 · lời giải: `[Chuong-5].[Phan-5.1.2].[BaiTap-2].md`
- `[Chuong-5].[Phan-5.1.2].[BaiTap-3].py` — Bài tập BT 5.3: Năm đại lượng của bài toán A5, mỗi đại lượng một hàm theo Mục 4.2.1. Thuộc Chương 5, Mục 5.1.2 · lời giải: `[Chuong-5].[Phan-5.1.2].[BaiTap-3].md`
- `[Chuong-5].[Phan-5.1.2].[ViDu-2].py` — Ví dụ 2: Bốn đại lượng của bài toán A5 tính từ một danh sách 24 số đo: cực trị, trung bình, số giờ vượt ngưỡng. Thuộc Chương 5, Mục 5.1.2
- `[Chuong-5].[Phan-5.2.1].[BaiTap-4].py` — Bài tập BT 5.4: Bảng mức chất lượng không khí bằng từ điển, hàm trả về tên mức của một nồng độ, và số phép so của hai cách tra ở ba quy mô bảng. Thuộc Chương 5, Mục 5.2.1 · lời giải: `[Chuong-5].[Phan-5.2.1].[BaiTap-4].md`
- `[Chuong-5].[Phan-5.2.1].[BaiTap-8].py` — Bài tập BT 5.8: Chọn cấu trúc dữ liệu cho bốn tình huống, nêu độ phức tạp tiệm cận, rồi đo lại để xác nhận. Thuộc Chương 5, Mục 5.2.1 và 5.4.1 · lời giải: `[Chuong-5].[Phan-5.2.1].[BaiTap-8].md`
- `[Chuong-5].[Phan-5.2.1].[ViDu-3].py` — Ví dụ 3: Bảng tra mức chất lượng không khí bằng từ điển, so với cách duyệt danh sách. Thuộc Chương 5, Mục 5.2.1
- `[Chuong-5].[Phan-5.3.1].[BaiTap-5].py` — Bài tập BT 5.5: Chuyển chương trình Bài tập 5.3 sang đọc số đo từ tệp và ghi báo cáo ra tệp mới; xác nhận hai lần chạy cho cùng kết quả. Thuộc Chương 5, Mục 5.3.1 · lời giải: `[Chuong-5].[Phan-5.3.1].[BaiTap-5].md`
- `[Chuong-5].[Phan-5.3.1].[ViDu-4].py` — Ví dụ 4: Đọc 24 số đo từ tệp pm25_ngay.txt, tính bốn đại lượng, rồi ghi báo cáo ra một tệp mới. Thuộc Chương 5, Mục 5.3.1
- `[Chuong-5].[Phan-5.3.2].[BaiTap-7].py` — Bài tập BT 5.7: Xử lý tệp 720 dòng theo cả ba cách xử lý ô trống, lập bảng ba giá trị trung bình, và nêu cách nào nên dùng. Thuộc Chương 5, Mục 5.3.2 · lời giải: `[Chuong-5].[Phan-5.3.2].[BaiTap-7].md`
- `[Chuong-5].[Phan-5.3.2].[ViDu-5].py` — Ví dụ 5: Đọc tệp số liệu dạng bảng 720 dòng có dòng thiếu cột, dòng ghi chữ và ô trống; báo số dòng đã bỏ. Thuộc Chương 5, Mục 5.3.2
- `[Chuong-5].[Phan-5.4.1].[BaiTap-6].py` — Bài tập BT 5.6: Vẽ đồ thị PM2.5 theo giờ đủ năm phép bắt buộc, rồi vẽ lại bản thiếu tên trục để so. Thuộc Chương 5, Mục 5.4.1 · lời giải: `[Chuong-5].[Phan-5.4.1].[BaiTap-6].md`
- `[Chuong-5].[Phan-5.4.1].[BaiTap-9].py` — Bài tập BT 5.9: Chương trình báo cáo chất lượng không khí một tháng: đọc tệp, xử lý dòng lỗi, tính đại lượng, tra mức, vẽ đồ thị, ghi báo cáo. Thuộc Chương 5, cả sáu tiểu mục · lời giải: `[Chuong-5].[Phan-5.4.1].[BaiTap-9].md`
- `[Chuong-5].[Phan-5.4.1].[ViDu-6].py` — Ví dụ 6: Mảng NumPy cho chuỗi số đo một ngày, và đồ thị nồng độ theo giờ có tên trục, đơn vị, chú giải và đường ngưỡng. Thuộc Chương 5, Mục 5.4.1

### Chương 6 — Kiểm thử, gỡ lỗi và hoàn thiện chương trình

- `[Chuong-6].[GoLoi-6].py` — Gỡ lỗi GL 6: Chương trình 24 dòng tìm nghiệm bằng phương pháp Newton chứa đúng ba lỗi: một cú pháp, một thực thi, một logic. Thuộc Chương 6, Bài gỡ lỗi GL6 · lời giải: `[Chuong-6].[GoLoi-6].md`
- `[Chuong-6].[Phan-6.1.1].[BaiTap-1].py` — Bài tập Bài tập 6.1: Xếp sáu thông báo lỗi lấy từ năm chương trước vào ba loại, và cho biết thông báo có nói được dòng mã sai hay không. Thuộc Chương 6, Mục 6.1.1 · lời giải: `[Chuong-6].[Phan-6.1.1].[BaiTap-1].md`
- `[Chuong-6].[Phan-6.1.1].[BaiTap-3].py` — Bài tập Bài tập 6.3: Chương trình chia đôi 18 dòng chứa ba lỗi, mỗi lỗi một loại. Thuộc Chương 6, Mục 6.1.1 · lời giải: `[Chuong-6].[Phan-6.1.1].[BaiTap-3].md`
- `[Chuong-6].[Phan-6.1.1].[ViDu-1].py` — Ví dụ Ví dụ 6.1: Sinh một thông báo lỗi thực thi thật, qua ba tầng gọi hàm, rồi in nguyên văn toàn bộ thông báo đó. Thuộc Chương 6, Mục 6.1.1
- `[Chuong-6].[Phan-6.1.1].[ViDu-2].py` — Ví dụ Ví dụ 6.2: Bài toán B6, ước lượng số pi bằng phương pháp Monte Carlo. Thuộc Chương 6, Mục 6.1.1
- `[Chuong-6].[Phan-6.2.1].[BaiTap-2].py` — Bài tập Bài tập 6.2: Xếp loại bốn ca kiểm thử của hàm khấu hao, chỉ ra loại ca còn thiếu, và nêu nhánh nào của hàm chưa ca nào đi qua. Thuộc Chương 6, Mục 6.2.1 · lời giải: `[Chuong-6].[Phan-6.2.1].[BaiTap-2].md`
- `[Chuong-6].[Phan-6.2.1].[BaiTap-4].py` — Bài tập Bài tập 6.4: Viết bộ ba loại ca cho hàm chia đôi, rồi đếm số dòng của thân hàm mà bộ ca đi qua, so với một ca thường. Thuộc Chương 6, Mục 6.2.1 · lời giải: `[Chuong-6].[Phan-6.2.1].[BaiTap-4].md`
- `[Chuong-6].[Phan-6.2.1].[BaiTap-7].py` — Bài tập Bài tập 6.7: Thiết kế bộ ca cho hàm Newton trước khi viết hàm, rồi viết hàm, rồi gieo ba lỗi cài sẵn khác ba lỗi của Ví dụ 6.4 và đếm số lỗi bộ ca bắt được. Thuộc Chương 6, Mục 6.2.1 · lời giải: `[Chuong-6].[Phan-6.2.1].[BaiTap-7].md`
- `[Chuong-6].[Phan-6.2.1].[ViDu-3].py` — Ví dụ Ví dụ 6.3: Bộ ba loại ca kiểm thử cho hàm chia đôi của bài toán A6, và số dòng của hàm mà bộ ca đi qua, so với một ca thường duy nhất. Thuộc Chương 6, Mục 6.2.1
- `[Chuong-6].[Phan-6.2.1].[ViDu-4].py` — Ví dụ Ví dụ 6.4: Bộ ca kiểm thử của hàm Newton, thiết kế từ bảng đặc tả trước khi viết hàm, chạy trên ba bản lỗi cài sẵn và trên bản đúng. Thuộc Chương 6, Mục 6.2.2
- `[Chuong-6].[Phan-6.3.1].[BaiTap-5].py` — Bài tập Bài tập 6.5: Thêm try và except theo loại cụ thể vào bộ đọc tệp bảng của Mục 5.3.2, rồi so số dòng xử lý được trước và sau. Thuộc Chương 6, Mục 6.3.1 · lời giải: `[Chuong-6].[Phan-6.3.1].[BaiTap-5].md`
- `[Chuong-6].[Phan-6.3.1].[BaiTap-8].py` — Bài tập Bài tập 6.8: Gỡ ba lỗi của chương trình Monte Carlo bằng đúng quy trình năm bước, và ghi lại bảng năm bước cho từng lỗi, trong đó bước 1 nêu bộ dữ liệu nhỏ nhất tái lập được. Thuộc Chương 6, Mục 6.3.1 · lời giải: `[Chuong-6].[Phan-6.3.1].[BaiTap-8].md`
- `[Chuong-6].[Phan-6.3.1].[ViDu-5].py` — Ví dụ Ví dụ 6.5: Đọc tệp số liệu một tháng theo hai cách, không bắt ngoại lệ và bắt ngoại lệ theo loại, rồi so số dòng xử lý được của hai cách. Thuộc Chương 6, Mục 6.3.1
- `[Chuong-6].[Phan-6.4.1].[BaiTap-6].py` — Bài tập Bài tập 6.6: Bốn đoạn mã do công cụ AI sinh. Thuộc Chương 6, Mục 6.4.1 · lời giải: `[Chuong-6].[Phan-6.4.1].[BaiTap-6].md`
- `[Chuong-6].[Phan-6.4.1].[BaiTap-9].py` — Bài tập Bài tập 6.9: Kiểm tra đầy đủ một chương trình do công cụ AI sinh giải bài toán tìm nghiệm phương trình: đặc tả, bộ ca thiết kế trước, bốn cách kiểm, năm bước gỡ từng lỗi, bắt ngoại lệ, và bản khai báo việc dùng AI. Thuộc Chương 6, cả bốn tiểu mục · lời giải: `[Chuong-6].[Phan-6.4.1].[BaiTap-9].md`
- `[Chuong-6].[Phan-6.4.1].[ViDu-6].py` — Ví dụ Ví dụ 6.6: Bốn đoạn mã do công cụ AI sinh, mỗi đoạn một nhóm lỗi, đem kiểm bằng bốn cách. Thuộc Chương 6, Mục 6.4.1
- `thu_vien_ai.py` — Thư viện dùng chung: Một module phụ trợ do công cụ AI sinh, dùng tên hàm `numpy.trapz` đã thôi dùng ở NumPy 2.x. Thuộc Chương 6, Mục 6.4.1

## Số liệu kèm theo

- `Chuong1_DongCo.csv` — bảng công suất động cơ, dùng ở Chương 1.
- `pm25_ngay.txt` — số đo bụi mịn một ngày, dùng ở Chương 5.
- `pm25_thang.csv` — số đo bụi mịn một tháng, có ô hỏng cố ý, dùng ở Chương 5 và Chương 6.
- `doan_a6.txt` — đoạn văn bản dùng ở phụ lục.

Các tệp kết quả như `bao_cao_ngay.txt` không có sẵn ở đây: chúng do chính mã sinh ra khi chạy.

## Bản quyền

Toàn bộ mã trong kho do nhóm soạn giáo trình tự viết. Số liệu kỹ thuật kèm theo là số liệu giả định của đề bài, đặt trong miền giá trị thực tế của ngành, không lấy từ bộ dữ liệu có bản quyền nào. Trang *Nguồn, bản quyền và công cụ biên soạn* ở đầu giáo trình ghi đầy đủ phần này.

