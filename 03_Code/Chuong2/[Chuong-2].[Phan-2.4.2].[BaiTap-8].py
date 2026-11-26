# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.8
Chương, mục : Chương 2, Mục 2.4.2
Đề bài      : Cho bốn tình huống so sánh, chọn giữa phép bằng,
              math.isclose với abs_tol và math.isclose với
              rel_tol; nêu ngưỡng cụ thể và lý giải lựa chọn.
Đầu vào     : bốn cặp giá trị kèm đơn vị và dung sai
Đầu ra      : bốn lựa chọn kèm ngưỡng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

import math

PHEP_BANG = "=="
THEO_ABS = "isclose abs_tol"
THEO_REL = "isclose rel_tol"


def chon_phep_so_sanh(la_so_nguyen, co_the_gan_0, dung_sai):
    """Chọn phép so sánh theo hai câu hỏi của gợi ý đề bài.

    la_so_nguyen: hai giá trị là số nguyên hay số thực
    co_the_gan_0: một trong hai giá trị có thể bằng 0 hay không
    dung_sai: dung sai tuyệt đối bài toán cho sẵn, hoặc None
    """
    if la_so_nguyen:
        return PHEP_BANG
    if co_the_gan_0 or dung_sai is not None:
        return THEO_ABS
    return THEO_REL


def so_sanh(phep, a, b, nguong):
    """Thực hiện phép so sánh đã chọn."""
    if phep == PHEP_BANG:
        return a == b
    if phep == THEO_ABS:
        return math.isclose(a, b, rel_tol=0.0, abs_tol=nguong)
    return math.isclose(a, b, rel_tol=nguong)


# Bốn tình huống của đề bài.
CAC_TINH_HUONG = (
    ("kich thuoc", 50.02, 50.00, False, False, 0.05),
    ("dien nang", 497.5, 497.50000001, False, False, None),
    ("sai lech", 1e-12, 0.0, False, True, 1e-9),
    ("ma dong co", 2, 2, True, False, None),
)


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Kích thước có dung sai cho sẵn nên dùng ngưỡng tuyệt đối.
    assert chon_phep_so_sanh(False, False, 0.05) == THEO_ABS
    assert so_sanh(THEO_ABS, 50.02, 50.00, 0.05) is True
    assert so_sanh(THEO_ABS, 50.06, 50.00, 0.05) is False
    # Hai tổng điện năng lớn, không có dung sai cho sẵn và không
    # thể bằng 0, nên dùng ngưỡng tương đối.
    assert chon_phep_so_sanh(False, False, None) == THEO_REL
    assert so_sanh(THEO_REL, 497.5, 497.50000001, 1e-9) is True

    # --- Trường hợp biên ---------------------------------------
    # Đại lượng có thể bằng 0 thì ngưỡng tương đối vô dụng, vì
    # mọi sai lệch chia cho 0 đều lớn vô hạn.
    assert chon_phep_so_sanh(False, True, 1e-9) == THEO_ABS
    assert math.isclose(1e-12, 0.0, abs_tol=1e-9) is True
    assert math.isclose(1e-12, 0.0) is False
    # Số nguyên so bằng dấu bằng là đúng, không cần ngưỡng.
    assert chon_phep_so_sanh(True, False, None) == PHEP_BANG
    assert so_sanh(PHEP_BANG, 2, 2, None) is True
    assert so_sanh(PHEP_BANG, 2, 3, None) is False
    # Ngưỡng bằng đúng dung sai thì giá trị ở biên vẫn được nhận.
    assert so_sanh(THEO_ABS, 50.05, 50.00, 0.05) is True

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ngưỡng âm không có nghĩa và bị chặn.
    da_chan = False
    try:
        math.isclose(1.0, 1.0, rel_tol=-0.1)
    except ValueError as loi:
        da_chan = "non-negative" in str(loi)
    assert da_chan, "nguong am ma van chay"

    print("BT 2.8")
    for ten, a, b, nguyen, gan_0, dung_sai in CAC_TINH_HUONG:
        phep = chon_phep_so_sanh(nguyen, gan_0, dung_sai)
        nguong = dung_sai if dung_sai is not None else 1e-9
        print(f"  {ten:<12}{phep:<18}nguong {nguong} -> "
              f"{so_sanh(phep, a, b, nguong)}")
