# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 2
Chương, mục : Chương 3, Mục 3.1.2
Đề bài      : Chỉ phát cảnh báo khi nhiệt độ vượt ngưỡng và
              động cơ đang chạy. So hai cách viết: điều kiện
              lồng hai tầng và điều kiện kết hợp bằng and.
Đầu vào     : nhiệt độ (°C) và trạng thái chạy, nhập từ bàn phím
Đầu ra      : kết luận của hai cách viết, phải trùng nhau
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
NGUONG_CANH_BAO = 60.0

nhiet_do = float(input("Nhiet do (do C): "))
dang_chay = input("Dang chay (co/khong): ") == "co"

# Cach 1: hai tang dieu kien long.
if dang_chay:
    if nhiet_do >= NGUONG_CANH_BAO:
        canh_bao_long = True
    else:
        canh_bao_long = False
else:
    canh_bao_long = False

# Cach 2: mot dieu kien ket hop.
canh_bao_gop = dang_chay and nhiet_do >= NGUONG_CANH_BAO

print("Cach long:", canh_bao_long)
print("Cach gop :", canh_bao_gop)
print("Hai cach trung nhau:", canh_bao_long == canh_bao_gop)
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert nhiet_do == 72.5
    assert dang_chay is True
    assert canh_bao_long is True
    assert canh_bao_gop is True
    assert canh_bao_long == canh_bao_gop

    # --- Trường hợp biên ---------------------------------------
    # Bốn tổ hợp của hai điều kiện cho cùng kết quả ở hai cách.
    for nhiet in (45.0, 60.0, 90.0):
        for chay in (True, False):
            gop = chay and nhiet >= NGUONG_CANH_BAO
            if chay:
                long = nhiet >= NGUONG_CANH_BAO
            else:
                long = False
            assert long == gop, (nhiet, chay)
    # Nhiệt độ đúng bằng ngưỡng vẫn phát cảnh báo, vì điều kiện
    # dùng dấu lớn hơn hoặc bằng.
    assert (True and 60.0 >= NGUONG_CANH_BAO) is True
    assert (True and 59.9 >= NGUONG_CANH_BAO) is False

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dùng or thay cho and là lỗi L3.1-6: cảnh báo cả khi động cơ
    # đã dừng, tức kết quả khác hẳn với mọi nhiệt độ vượt ngưỡng.
    assert (False or 90.0 >= NGUONG_CANH_BAO) is True
    assert (False and 90.0 >= NGUONG_CANH_BAO) is False
