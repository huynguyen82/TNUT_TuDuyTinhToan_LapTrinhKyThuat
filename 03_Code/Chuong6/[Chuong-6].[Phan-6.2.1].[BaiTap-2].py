# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.2
Chương, mục : Chương 6, Mục 6.2.1
Đề bài      : Xếp loại bốn ca kiểm thử của hàm khấu hao, chỉ ra loại
              ca còn thiếu, và nêu nhánh nào của hàm chưa ca nào đi
              qua.
Đầu vào     : hàm khau_hao và bốn ca của đề bài
Đầu ra      : bảng xếp loại, loại ca thiếu, số dòng chưa chạy
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import sys


def khau_hao(nguyen_gia, so_nam):
    """Gia tri con lai cuoi tung nam, nghin dong."""
    if so_nam <= 0:
        return []
    if nguyen_gia < 0.0:
        return []
    moi_nam = nguyen_gia / so_nam
    return [nguyen_gia - moi_nam * (nam + 1)
            for nam in range(so_nam)]


BON_CA = (
    ("ca_a", (100000.0, 10), "thuong"),
    ("ca_b", (100000.0, 5), "thuong"),
    ("ca_c", (100000.0, 1), "bien"),
    ("ca_d", (0.0, 10), "bien"),
)
LOAI_THIEU = "du lieu khong hop le"


def dong_than_ham(ham):
    """Tap so dong cua than ham, bo dong `def`."""
    ma = ham.__code__
    cac_dong = {d for _, _, d in ma.co_lines() if d is not None}
    return cac_dong - {ma.co_firstlineno}


def dong_da_chay(cac_doi_so):
    """Tap so dong cua khau_hao ma cac lan goi di qua."""
    ten_tep = khau_hao.__code__.co_filename
    da_chay = set()

    def theo_dau(khung, su_kien, doi_so):
        if (khung.f_code.co_filename == ten_tep
                and khung.f_code.co_name == "khau_hao"):
            if su_kien == "line":
                da_chay.add(khung.f_lineno)
            return theo_dau
        return None

    sys.settrace(theo_dau)
    try:
        for doi_so in cac_doi_so:
            khau_hao(*doi_so)
    finally:
        sys.settrace(None)
    return da_chay


TONG = len(dong_than_ham(khau_hao))
BON = dong_da_chay([d for _, d, _ in BON_CA])
# Hai ca dữ liệu không hợp lệ còn thiếu của đề bài.
NAM_SAU = dong_da_chay(
    [d for _, d, _ in BON_CA] + [(100000.0, 0), (-5000.0, 10)])


def in_ket_qua():
    """In bang xep loai bon ca va hai so dem dong."""
    print("Ca    | Du lieu vao        | Loai")
    for ten, doi_so, loai in BON_CA:
        print(f"{ten:<5} | {str(doi_so):<18} | {loai}")
    print()
    print(f"Loai ca con thieu         : {LOAI_THIEU}")
    print(f"Tong so dong than ham     : {TONG}")
    print(f"Bon ca cua de bai di qua  : {len(BON)}")
    print(f"Dong chua ca nao chay     : {sorted(TONG and
                                                (dong_than_ham(khau_hao)
                                                 - BON))}")
    print(f"Them hai ca khong hop le  : {len(NAM_SAU)}")


if __name__ == "__main__":
    in_ket_qua()

    # Bốn ca của đề bài không có ca dữ liệu không hợp lệ nào.
    assert LOAI_THIEU not in {loai for _, _, loai in BON_CA}, \
        "bon ca cua de bai khong co loai nay"

    # Hai ca thường khác giá trị vẫn chỉ là hai ca thường, nên
    # chúng không phủ thêm dòng nào so với một ca.
    _mot = dong_da_chay([(100000.0, 10)])
    _hai = dong_da_chay([(100000.0, 10), (100000.0, 5)])
    assert _mot == _hai, "hai ca thuong khong phu them dong nao"

    # Hai dòng `return []` chưa ca nào của đề bài chạy tới.
    assert len(BON) < TONG, "bon ca chua phu het than ham"
    assert TONG - len(BON) == 2, "con dung hai dong chua chay"

    # Thêm hai ca dữ liệu không hợp lệ thì phủ hết thân hàm.
    assert len(NAM_SAU) == TONG, "sau ca phai phu het than ham"

    print()
    print("Moi khang dinh dat.")
