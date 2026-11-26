# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 3
Chương, mục : Chương 2, Mục 2.2.2
Đề bài      : Chia thời gian vận hành 24 giờ của một dây chuyền
              thành các ca 7 giờ, cần số ca đầy và số giờ còn dư.
              Cho thấy ba phép chia khác nhau của Python.
Đầu vào     : tổng số giờ và độ dài một ca, viết thẳng trong mã
Đầu ra      : thương số thực, số ca đầy, số giờ dư
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
tong_gio = 24
do_dai_ca = 7

thuong_thuc = tong_gio / do_dai_ca    # luon tra so thuc
so_ca_day = tong_gio // do_dai_ca     # chia nguyen
gio_du = tong_gio % do_dai_ca         # lay du

print("24 / 7  =", thuong_thuc)
print("24 // 7 =", so_ca_day)
print("24 % 7  =", gio_du)
print("Kiem tra:", so_ca_day * do_dai_ca + gio_du)

# Chia nguyen lam tron xuong ve phia am vo cuc.
print("-7 // 2 =", -7 // 2)
print("int(-7 / 2) =", int(-7 / 2))
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert thuong_thuc == 24 / 7
    assert so_ca_day == 3
    assert gio_du == 3
    # Quan hệ bắt buộc giữa ba phép chia.
    assert so_ca_day * do_dai_ca + gio_du == tong_gio

    # --- Trường hợp biên ---------------------------------------
    # Chia hết thì phần dư bằng 0.
    assert 21 // 7 == 3 and 21 % 7 == 0
    # Với số dương, chia nguyên trùng với cắt phần thập phân.
    assert 7 // 2 == int(7 / 2) == 3
    # Với số âm thì hai cách khác nhau một đơn vị.
    assert -7 // 2 == -4
    assert int(-7 / 2) == -3
    assert -7 // 2 != int(-7 / 2)
    # Phép chia thường luôn trả số thực, kể cả khi chia hết.
    assert 6 / 3 == 2.0
    assert isinstance(6 / 3, float)
    assert isinstance(6 // 3, int)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Chia cho 0 phải phát sinh ZeroDivisionError; đây là lỗi
    # L2.2-5 của Mục 2.2.2.
    da_chan = False
    try:
        tong_gio / 0
    except ZeroDivisionError:
        da_chan = True
    assert da_chan, "chia cho 0 ma van chay"
    # Chia nguyên cho 0 cũng bị chặn.
    da_chan_2 = False
    try:
        tong_gio // 0
    except ZeroDivisionError:
        da_chan_2 = True
    assert da_chan_2, "chia nguyen cho 0 ma van chay"
