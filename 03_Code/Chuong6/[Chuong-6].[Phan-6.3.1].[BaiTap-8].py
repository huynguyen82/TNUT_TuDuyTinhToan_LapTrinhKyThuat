# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.8
Chương, mục : Chương 6, Mục 6.3.1
Đề bài      : Gỡ ba lỗi của chương trình Monte Carlo bằng đúng quy
              trình năm bước, và ghi lại bảng năm bước cho từng lỗi,
              trong đó bước 1 nêu bộ dữ liệu nhỏ nhất tái lập được.
Đầu vào     : chương trình Monte Carlo của đề bài
Đầu ra      : bảng năm bước cho ba lỗi, và kết quả bản đã sửa
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math
import random

HAT_GIONG = 12345


def uoc_luong_pi_con_loi(so_diem):
    """Ban con hai loi: dong 14 chia cho trong thay vi so_diem.

    Loi cu phap o dong 9 da sua rieng de ban nay chay duoc, con
    loi logic o dong 14 giu nguyen de do duoc bieu hien that.
    """
    bo_sinh = random.Random(HAT_GIONG)
    trong = 0
    for _ in range(so_diem):
        x = bo_sinh.random()
        y = bo_sinh.random()
        if x * x + y * y < 1.0:
            trong = trong + 1
    return 4.0 * trong / trong


def uoc_luong_pi(so_diem):
    """Ban da sua du ba loi."""
    if so_diem <= 0:
        raise ValueError(f"so diem phai duong, nhan duoc {so_diem}")
    bo_sinh = random.Random(HAT_GIONG)
    trong = 0
    for _ in range(so_diem):
        x = bo_sinh.random()
        y = bo_sinh.random()
        if x * x + y * y < 1.0:
            trong = trong + 1
    return 4.0 * trong / so_diem


# Bảng năm bước, một hàng cho mỗi lỗi.
NAM_BUOC = (
    ("Loi cu phap, dong 9",
     "chay bat ky, ke ca 1 diem",
     "SyntaxError: expected ':' tai dong 9",
     "khong can khoanh vung, thong bao da chi dung dong",
     "khong can bang vet",
     "them dau hai cham, chay lai ca bo ca"),
    ("Loi logic, dong 14",
     "1 diem la bo nho nhat tai lap duoc",
     "khong co thong bao nao",
     "chia doi: in gia tri trong va so_diem truoc dong return",
     "bang vet cho thay trong = so_diem khi n = 1, nen 4.0 luon ra",
     "doi mau so thanh so_diem, chay lai ca bo ca"),
    ("Loi thuc thi, dong 14",
     "0 diem",
     "ZeroDivisionError: float division by zero",
     "thong bao chi dung dong chia",
     "khong can bang vet",
     "chan so_diem <= 0 truoc vong lap bang raise ValueError"),
)
TEN_BUOC = ("Buoc 1 tai lap", "Buoc 2 doc thong bao",
            "Buoc 3 khoanh vung", "Buoc 4 bang vet", "Buoc 5 sua")


def in_bang_nam_buoc():
    """In bang nam buoc cho ba loi."""
    for hang in NAM_BUOC:
        print(hang[0])
        for ten, noi_dung in zip(TEN_BUOC, hang[1:]):
            print(f"  {ten:<22}: {noi_dung}")
        print()


def in_ket_qua():
    """In bang nam buoc va ket qua ban da sua."""
    in_bang_nam_buoc()
    print(f"Ban da sua, 100 000 diem : {uoc_luong_pi(100_000):.6f}")
    print(f"So pi that               : {math.pi:.6f}")
    print(f"Ban con loi, 100 000 diem: "
          f"{uoc_luong_pi_con_loi(100_000):.6f}")


if __name__ == "__main__":
    in_ket_qua()

    # Bản đã sửa gần số pi tới hai chữ số thập phân.
    assert abs(uoc_luong_pi(100_000) - math.pi) < 0.01, \
        "ban da sua phai gan so pi"

    # Lỗi logic ở dòng 14 cho đúng 4,0 với mọi số điểm, vì mẫu số
    # và tử số là cùng một biến. Đó là dấu hiệu nhận ra nó.
    assert uoc_luong_pi_con_loi(100_000) == 4.0, \
        "ban con loi luon cho 4.0"
    assert uoc_luong_pi_con_loi(1) == 4.0, \
        "mot diem cung cho 4.0, nen no la bo nho nhat tai lap duoc"

    # Bản đã sửa chặn trước lỗi thực thi thay vì để nó nổ.
    _da_chan = False
    try:
        uoc_luong_pi(0)
    except ValueError:
        _da_chan = True
    assert _da_chan, "ban da sua phai chan so diem bang 0"

    # Bảng năm bước đủ ba lỗi và đủ năm bước cho từng lỗi.
    assert len(NAM_BUOC) == 3, "phai co ba loi"
    assert all(len(h) == 6 for h in NAM_BUOC), "moi loi du nam buoc"

    print()
    print("Moi khang dinh dat.")
