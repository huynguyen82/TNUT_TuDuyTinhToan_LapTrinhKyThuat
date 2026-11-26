# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.1
Chương, mục : Chương 6, Mục 6.1.1
Đề bài      : Sinh một thông báo lỗi thực thi thật, qua ba tầng gọi
              hàm, rồi in nguyên văn toàn bộ thông báo đó. Thông báo
              in ra ở đây là nội dung của Hình 6.2 và của Khối 4.
Đầu vào     : không có
Đầu ra      : thông báo lỗi nguyên văn, in ra dòng chuẩn
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import os
import traceback
from pathlib import Path

THU_MUC = str(Path(__file__).resolve().parent) + os.sep
NGUONG_SAI_SO = 1e-10


def chia_doi(ham, a, b):
    """Nghiem cua ham tren doan [a, b] bang phep chia doi."""
    while b - a > NGUONG_SAI_SO:
        giua = (a + b) / 2.0
        if ham(a) * ham(giua) < 0.0:
            b = giua
        else:
            a = giua
    return (a + b) / 2.0


def in_rut_duong_dan(van_ban):
    """In thong bao loi, bo phan duong dan thu muc cho vua trang.

    Chi phan thu muc bi bo; moi dong con lai nguyen van, ke ca ten
    tep, so dong, ten ham va dong co mui tron chi vao cho sai.
    """
    print(van_ban.replace(THU_MUC, "").rstrip())


# --- in-sach ---
def f(x):
    """Ham cua bai toan A6: f(x) = x**3 - 2x - 5."""
    return x ** 3 - 2.0 * x - 5.0


def nghiem_tren_doan(ham, a, b):
    """Nghiem tren doan, co kiem doan hop le truoc khi tinh."""
    if a >= b:
        raise ValueError(f"can duoi {a} khong nho hon can tren {b}")
    return chia_doi(ham, a, b)


def bao_cao_nghiem(ham, a, b):
    """In nghiem tim duoc tren doan da cho."""
    nghiem = nghiem_tren_doan(ham, a, b)
    print(f"Nghiem tren [{a}, {b}]: {nghiem:.6f}")


bao_cao_nghiem(f, 2.0, 3.0)
# --- het-in-sach ---


# Lời gọi thứ hai, với hai cận viết ngược, làm chương trình dừng.
# Thông báo lỗi của nó in ngay dưới đây, nguyên văn.
try:
    bao_cao_nghiem(f, 3.0, 2.0)
except ValueError as _loi:
    _van_ban = traceback.format_exc()
    _thong_diep = str(_loi)
    in_rut_duong_dan(_van_ban)
else:
    _van_ban = ""
    _thong_diep = ""


if __name__ == "__main__":
    # Dòng cuối của thông báo cho loại lỗi và thông điệp.
    assert _van_ban.strip().splitlines()[-1].startswith(
        "ValueError"), "dong cuoi phai bat dau bang ValueError"

    # Thông điệp phải nêu rõ hai giá trị gây lỗi, không nói chung.
    assert "3.0" in _thong_diep and "2.0" in _thong_diep, \
        "thong diep phai neu ca hai can"

    # Hai tên hàm của đường gọi đều phải có trong thông báo.
    assert all(ten in _van_ban for ten in
               ("bao_cao_nghiem", "nghiem_tren_doan")), \
        "duong goi ham phai co trong thong bao"

    print()
    print("Moi khang dinh dat.")
