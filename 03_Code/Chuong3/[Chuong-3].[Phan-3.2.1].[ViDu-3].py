# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 3
Chương, mục : Chương 3, Mục 3.2.1
Đề bài      : Tính tổng điện năng của một loạt động cơ bằng
              vòng lặp có đếm. Công suất động cơ thứ i sinh
              bằng công thức để số liệu tái lập được.
Đầu vào     : số động cơ, nhập từ bàn phím
Đầu ra      : tổng điện năng (kWh), một chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
GIO_CHAY = 8.0

so_dong_co = int(input("So dong co: "))

tong_kwh = 0.0
for chi_so in range(so_dong_co):
    cong_suat_kw = chi_so * 0.5 + 1.0
    tong_kwh = tong_kwh + cong_suat_kw * GIO_CHAY
    print(f"  dong co {chi_so}: {cong_suat_kw:.1f} kW")

print(f"Tong dien nang: {tong_kwh:.1f} kWh")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_dong_co == 4
    assert tong_kwh == 56.0, tong_kwh
    # Biến đếm của range(n) chạy từ 0 đến n-1, nên động cơ cuối
    # mang chỉ số 3 chứ không phải 4.
    assert chi_so == so_dong_co - 1

    # --- Trường hợp biên ---------------------------------------
    # range(0) chạy 0 lượt: vòng lặp không vào thân lần nào và
    # biến tích luỹ giữ nguyên giá trị khởi tạo.
    so_luot = 0
    for _ in range(0):
        so_luot = so_luot + 1
    assert so_luot == 0
    # range(1) chạy đúng một lượt.
    assert list(range(1)) == [0]
    # range với số âm cũng chạy 0 lượt, không báo lỗi.
    assert list(range(-5)) == []
    # Tổng của n động cơ đầu tiên tính lại được bằng công thức.
    for so_may in (1, 4, 10):
        tong_kiem = sum(
            (i * 0.5 + 1.0) * GIO_CHAY for i in range(so_may))
        tong_lap = 0.0
        for i in range(so_may):
            tong_lap = tong_lap + (i * 0.5 + 1.0) * GIO_CHAY
        assert tong_lap == tong_kiem, so_may

    # --- Trường hợp ngoại lệ -----------------------------------
    # range không nhận số thực, kể cả số thực tròn.
    da_chan = False
    try:
        range(4.0)
    except TypeError:
        da_chan = True
    assert da_chan, "range nhan so thuc ma van chay"
