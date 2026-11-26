# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 5
Chương, mục : Chương 2, Mục 2.4.1
Đề bài      : Cho thấy cách máy tính biểu diễn số thực: số 0,1
              không biểu diễn đúng được trong cơ số 2, và số
              nguyên Python không tràn số.
Đầu vào     : không có
Đầu ra      : giá trị thật của 0,1, thông số biểu diễn số thực
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import sys

# --- in-sach ---
# In 0.1 voi 20 chu so thap phan de thay gia tri thuc su.
print("0.1 in thong thuong:", 0.1)
print("0.1 voi 20 chu so  :", f"{0.1:.20f}")

print("So bit phan dinh tri:", sys.float_info.mant_dig)
print("So chu so thap phan :", sys.float_info.dig)
print("So thuc lon nhat    :", sys.float_info.max)

# So nguyen Python co do chinh xac tuy y, khong tran so.
so_lon = 2 ** 200
print("2 ** 200 co", len(str(so_lon)), "chu so")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert sys.float_info.mant_dig == 53
    assert sys.float_info.dig == 15
    # Giá trị thật của 0,1 lớn hơn 0,1 một chút.
    assert f"{0.1:.20f}" == "0.10000000000000000555"
    assert float(f"{0.1:.20f}") == 0.1
    assert len(str(2 ** 200)) == 61

    # --- Trường hợp biên ---------------------------------------
    # Một phần hai biểu diễn đúng được vì mẫu số là luỹ thừa 2.
    assert f"{0.5:.20f}" == "0.50000000000000000000"
    assert 0.5 + 0.25 == 0.75
    # Một phần mười thì không, nên tổng ba lần khác 0,3.
    assert 0.1 + 0.1 + 0.1 != 0.3
    # Epsilon là khoảng cách nhỏ nhất quanh 1,0.
    assert 1.0 + sys.float_info.epsilon != 1.0
    assert 1.0 + sys.float_info.epsilon / 2 == 1.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Số thực tràn khi luỹ thừa vượt miền biểu diễn; số nguyên
    # thì không. Đây là lỗi L2.4-2 của Mục 2.4.1.
    da_chan = False
    try:
        1e308 ** 2
    except OverflowError:
        da_chan = True
    assert da_chan, "so thuc vuot mien ma khong tran"
    assert 10 ** 400 > 0, "so nguyen lon phai tinh duoc"
