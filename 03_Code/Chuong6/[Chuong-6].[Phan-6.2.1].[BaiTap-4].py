# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.4
Chương, mục : Chương 6, Mục 6.2.1
Đề bài      : Viết bộ ba loại ca cho hàm chia đôi, rồi đếm số dòng
              của thân hàm mà bộ ca đi qua, so với một ca thường.
Đầu vào     : hàm chia_doi của Ví dụ 6.3
Đầu ra      : bảng ba ca và ba số đếm dòng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import sys

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200
KHONG_TINH_DUOC = -1.0


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


def chia_doi(ham, a, b):
    """Nghiem cua ham tren doan [a, b]. Tra ve (nghiem, so luot)."""
    if a >= b:
        return KHONG_TINH_DUOC, -1
    f_a = ham(a)
    f_b = ham(b)
    if f_a == 0.0:
        return a, 0
    if f_b == 0.0:
        return b, 0
    if f_a * f_b > 0.0:
        return KHONG_TINH_DUOC, -1
    so_luot = 0
    while b - a > SAI_SO and so_luot < SO_LAN_TOI_DA:
        giua = (a + b) / 2.0
        f_giua = ham(giua)
        so_luot += 1
        if f_giua == 0.0:
            return giua, so_luot
        if f_a * f_giua < 0.0:
            b = giua
        else:
            a = giua
            f_a = f_giua
    return (a + b) / 2.0, so_luot


# Bảng ba ca, kết quả mong đợi điền trước khi chạy.
BA_CA = (
    ("thuong", (f, 2.0, 3.0), 2.094551, None),
    ("bien", (lambda x: x - 2.0, 2.0, 3.0), 2.0, 0),
    ("khong hop le", (f, 0.0, 1.0), KHONG_TINH_DUOC, -1),
)


def chay_mot_ca(doi_so):
    """Chay mot ca va tra ve (nghiem, so luot)."""
    return chia_doi(*doi_so)


def dong_than_ham(ham):
    """Tap so dong cua than ham, bo dong `def`."""
    ma = ham.__code__
    cac_dong = {d for _, _, d in ma.co_lines() if d is not None}
    return cac_dong - {ma.co_firstlineno}


def dong_da_chay(cac_doi_so):
    """Tap so dong cua chia_doi ma cac lan goi di qua."""
    ten_tep = chia_doi.__code__.co_filename
    da_chay = set()

    def theo_dau(khung, su_kien, _dso):
        if (khung.f_code.co_filename == ten_tep
                and khung.f_code.co_name == "chia_doi"):
            if su_kien == "line":
                da_chay.add(khung.f_lineno)
            return theo_dau
        return None

    sys.settrace(theo_dau)
    try:
        for doi_so in cac_doi_so:
            chia_doi(*doi_so)
    finally:
        sys.settrace(None)
    return da_chay


TONG = len(dong_than_ham(chia_doi))
MOT_CA = len(dong_da_chay([BA_CA[0][1]]))
HAI_CA = len(dong_da_chay([ca[1] for ca in BA_CA[:2]]))
BO_BA = len(dong_da_chay([ca[1] for ca in BA_CA]))


def in_ket_qua():
    """In bang ba ca va ba so dem dong."""
    print("Loai ca      | Nghiem      | So luot")
    for ten, doi_so, _md, _ml in BA_CA:
        nghiem, so_luot = chay_mot_ca(doi_so)
        print(f"{ten:<12} | {nghiem:>11.6f} | {so_luot}")
    print()
    print(f"Tong so dong than ham : {TONG}")
    print(f"Mot ca thuong         : {MOT_CA} ({MOT_CA/TONG:.1%})")
    print(f"Them ca bien          : {HAI_CA} ({HAI_CA/TONG:.1%})")
    print(f"Bo ba loai ca         : {BO_BA} ({BO_BA/TONG:.1%})")


if __name__ == "__main__":
    in_ket_qua()

    # Từng ca cho đúng kết quả mong đợi đã điền trước.
    for _ten, _dso, _nghiem, _luot in BA_CA:
        _n, _l = chay_mot_ca(_dso)
        assert abs(_n - _nghiem) < 1e-5, f"ca {_ten} sai nghiem"
        if _luot is not None:
            assert _l == _luot, f"ca {_ten} sai so luot"

    # Mỗi loại ca thêm vào đều phủ thêm dòng, nhưng bộ ba vẫn
    # chưa phủ hết thân hàm: ba dòng còn lại là nhánh tại mốc.
    assert MOT_CA < HAI_CA < BO_BA < TONG, \
        "moi loai ca phai phu them dong, va bo ba van chua du"
    assert TONG - BO_BA == 3, "con dung ba dong chua chay"

    print()
    print("Moi khang dinh dat.")
