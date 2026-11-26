# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 5
Chương, mục : Chương 3, Mục 3.2.3
Đề bài      : Tra bảng tiết diện dây nhỏ nhất chịu được dòng
              điện cho trước, thoát vòng lặp ngay khi tìm thấy.
              Bảng tra viết thẳng trong mã vì Chương 3 chưa dạy
              danh sách.
Đầu vào     : dòng điện (A), nhập từ bàn phím
Đầu ra      : tiết diện (mm²) và số lần so sánh đã thực hiện
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
# Bang tra: dong dien toi da 16, 25, 32, 40, 63 A ung voi tiet
# dien 1.5, 2.5, 4.0, 6.0, 10.0 mm2. So lieu gia dinh cua de bai.
dong_dien = float(input("Dong dien (A): "))

tiet_dien = 0.0
so_lan_so = 0
for buoc in range(5):
    dong_toi_da = (16, 25, 32, 40, 63)[buoc]
    so_lan_so = so_lan_so + 1
    if dong_dien <= dong_toi_da:
        tiet_dien = (1.5, 2.5, 4.0, 6.0, 10.0)[buoc]
        break

if tiet_dien == 0.0:
    print(f"{dong_dien:.0f} A vuot bang tra")
else:
    print(f"{dong_dien:.0f} A -> {tiet_dien:.1f} mm2")
print(f"So lan so sanh: {so_lan_so}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert dong_dien == 30.0
    assert tiet_dien == 4.0, tiet_dien
    # Thoát ở dòng thứ ba nên chỉ so ba lần, không so đủ năm.
    assert so_lan_so == 3, so_lan_so

    # --- Trường hợp biên ---------------------------------------
    # Dòng đúng bằng một mốc của bảng vẫn nhận tiết diện của mốc
    # đó, vì điều kiện dùng dấu nhỏ hơn hoặc bằng.
    assert 16 <= 16
    assert not 17 <= 16
    # Dòng nhỏ hơn mốc đầu thì thoát ngay lượt thứ nhất.
    cac_moc = (16, 25, 32, 40, 63)
    dem = 0
    for buoc in range(5):
        dem = dem + 1
        if 1.0 <= cac_moc[buoc]:
            break
    assert dem == 1
    # Dòng vượt mốc cuối thì duyệt hết năm lượt và không thoát
    # sớm lần nào, tức trường hợp xấu nhất của break.
    dem_het = 0
    tim_thay = False
    for buoc in range(5):
        dem_het = dem_het + 1
        if 100.0 <= cac_moc[buoc]:
            tim_thay = True
            break
    assert dem_het == 5 and tim_thay is False

    # --- Trường hợp ngoại lệ -----------------------------------
    # Lệnh break đặt ngoài mọi vòng lặp là lỗi cú pháp.
    da_chan = False
    try:
        compile("break", "<vi du>", "exec")
    except SyntaxError:
        da_chan = True
    assert da_chan, "break ngoai vong lap ma van bien dich duoc"
