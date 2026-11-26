# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.6
Chương, mục : Chương 6, Mục 6.4.1
Đề bài      : Bốn đoạn mã do công cụ AI sinh. Tìm nhóm lỗi của từng
              đoạn theo bốn nhóm của Mục 6.4.1, và cho biết chạy một
              lần trên bộ dữ liệu thường có phát hiện được không.
Đầu vào     : bốn đoạn mã của đề bài
Đầu ra      : bảng bốn dòng, và số đoạn chạy một lần phát hiện được
Python      : 3.12
Thư viện    : NumPy 2.1.3
Cài đặt     : pip install -r 03_Code/requirements.txt
"""

import numpy as np

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200


def doan_a(day):
    """Nhom 2: ten ham thu vien da thoi dung."""
    return float(np.trapz(day, dx=1.0))


def doan_a_dung(day):
    """Ban dung cua doan A."""
    return float(np.trapezoid(day, dx=1.0))


def doan_d(nguyen_gia, so_nam):
    """Nhom 3: phep chia nguyen cho cho can phep chia thuc."""
    return nguyen_gia // so_nam


def doan_d_dung(nguyen_gia, so_nam):
    """Ban dung cua doan D."""
    return nguyen_gia / so_nam


def doan_g():
    """Nhom 4: he so 1,15 'theo tieu chuan', khong ghi so hieu."""
    return 1.15


def doan_j(ham, a, b, sau=0):
    """Nhom 1: de quy thieu dieu kien dung va dieu kien ap dung."""
    if sau > SO_LAN_TOI_DA:
        raise RecursionError("vuot so lan de quy cho phep")
    giua = (a + b) / 2.0
    if ham(giua) == 0.0:
        return giua
    return doan_j(ham, a, giua, sau + 1)


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


def c1_phat_hien_duoc(ten):
    """Chay mot lan tren bo du lieu thuong, co phat hien duoc."""
    if ten == "A":
        return doan_a([0.0, 1.0, 2.0]) != doan_a_dung([0.0, 1.0, 2.0])
    if ten == "D":
        return doan_d(100000.0, 10) != doan_d_dung(100000.0, 10)
    if ten == "G":
        # Khong co nguon doc lap nao de so he so 1,15.
        return False
    try:
        doan_j(f, 2.0, 3.0)
    except RecursionError:
        return True
    return False


BON_DOAN = (
    ("A", "nhom 2: ten ham thu vien da thoi dung"),
    ("D", "nhom 3: tron kieu im lang"),
    ("G", "nhom 4: hang so khong co nguon"),
    ("J", "nhom 1: thieu dieu kien ap dung"),
)


def in_bang():
    """In bang bon doan va ket qua cach kiem thu nhat."""
    print("Doan | Nhom loi                              | C1")
    for ten, nhom in BON_DOAN:
        co = "co" if c1_phat_hien_duoc(ten) else "khong"
        print(f"  {ten}  | {nhom:<37} | {co}")
    so = sum(c1_phat_hien_duoc(t) for t, _ in BON_DOAN)
    print()
    print(f"Chay mot lan phat hien duoc: {so} / 4 doan")
    print(f"He so khong nguon cua doan G: {doan_g()}")


if __name__ == "__main__":
    in_bang()

    # Đoạn A cho đúng cùng kết quả với bản dùng tên hàm mới, nên
    # không ca kiểm thử nào trên kết quả bắt được nó.
    assert doan_a([0.0, 1.0, 2.0]) == doan_a_dung([0.0, 1.0, 2.0]), \
        "doan A phai cho dung ket qua"

    # Đoạn D im lặng trên bộ dữ liệu thường và chỉ sai ở ca biên.
    assert doan_d(100000.0, 10) == doan_d_dung(100000.0, 10), \
        "doan D dung khi nguyen gia chia het"
    assert doan_d(100000.0, 7) != doan_d_dung(100000.0, 7), \
        "doan D sai khi nguyen gia khong chia het"

    # Đoạn J là đoạn duy nhất mà một lần chạy phát hiện được.
    assert sum(c1_phat_hien_duoc(t) for t, _ in BON_DOAN) == 1, \
        "chi mot doan bi mot lan chay phat hien"
    assert c1_phat_hien_duoc("J"), "doan J phai bi phat hien"

    print()
    print("Moi khang dinh dat.")
