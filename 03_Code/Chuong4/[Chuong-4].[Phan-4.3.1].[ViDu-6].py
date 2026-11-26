# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 6
Chương, mục : Chương 4, Mục 4.3.1
Đề bài      : Viết ca kiểm thử bằng lệnh assert cho hàm tính
              giá trị hiện tại, đủ ba trường hợp thường, biên
              và ngoại lệ.
Đầu vào     : không có
Đầu ra      : một dòng báo mọi ca đã đạt
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
def gia_tri_hien_tai(gia_tri_tuong_lai, lai_suat, so_ky):
    """Gia tri hien tai cua mot dong tien tuong lai."""
    if so_ky < 0:
        raise ValueError("so ky khong duoc am")
    return gia_tri_tuong_lai / (1 + lai_suat) ** so_ky


# Truong hop thuong.
assert abs(gia_tri_hien_tai(100000.0, 0.008, 12)
           - 90881.11) < 0.01

# Truong hop bien: so ky bang 0 thi khong chiet khau.
assert gia_tri_hien_tai(100000.0, 0.008, 0) == 100000.0
# Lai suat bang 0 thi gia tri khong doi.
assert gia_tri_hien_tai(100000.0, 0.0, 12) == 100000.0

# Truong hop ngoai le: so ky am khong co nghia.
da_chan = False
try:
    gia_tri_hien_tai(100000.0, 0.008, -1)
except ValueError:
    da_chan = True
assert da_chan, "so ky am ma van tinh duoc"

print("Ba ca kiem thu deu dat")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert abs(gia_tri_hien_tai(100000.0, 0.008, 24)
               - 82593.76) < 0.01
    # Gia tri hien tai giam khi so ky tang.
    assert (gia_tri_hien_tai(100000.0, 0.008, 24)
            < gia_tri_hien_tai(100000.0, 0.008, 12))

    # --- Trường hợp biên ---------------------------------------
    # So sanh so thuc bang dau bang chi an toan khi khong qua
    # phep chia; o day phai dung sai so, theo Muc 2.4.2.
    assert gia_tri_hien_tai(100000.0, 0.0, 999) == 100000.0
    # Viet assert voi dau ngoac tao mot bo hai phan tu, va bo
    # khac rong luon dung, nen ca kiem thu mat tac dung.
    assert bool((False, "thong bao")) is True
    assert bool(False) is False

    # --- Trường hợp ngoại lệ -----------------------------------
    da_chan_am = False
    try:
        gia_tri_hien_tai(100000.0, 0.008, -5)
    except ValueError as loi:
        da_chan_am = "so ky" in str(loi)
    assert da_chan_am, "so ky am ma van tinh duoc"
