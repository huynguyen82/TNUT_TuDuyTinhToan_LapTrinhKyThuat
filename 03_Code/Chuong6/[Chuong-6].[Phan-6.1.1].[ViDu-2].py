# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.2
Chương, mục : Chương 6, Mục 6.1.1
Đề bài      : Bài toán B6, ước lượng số pi bằng phương pháp Monte
              Carlo. In kết quả của bản đúng và của bản thiếu hệ số
              4, để thấy lỗi logic không có thông báo nào.
Đầu vào     : không có; hạt giống cố định nên kết quả lặp lại được
Đầu ra      : ba con số, in ra dòng chuẩn
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math
import random

# --- in-sach ---
SO_DIEM = 100_000
HAT_GIONG = 12345


def uoc_luong_pi(so_diem, hat_giong):
    """Uoc luong so pi bang cach gieo diem vao hinh vuong don vi."""
    bo_sinh = random.Random(hat_giong)
    trong = 0
    for _ in range(so_diem):
        x = bo_sinh.random()
        y = bo_sinh.random()
        if x * x + y * y < 1.0:
            trong = trong + 1
    return 4.0 * trong / so_diem


print(f"Ban dung        : {uoc_luong_pi(SO_DIEM, HAT_GIONG):.6f}")
print(f"So pi that      : {math.pi:.6f}")
# --- het-in-sach ---


def uoc_luong_pi_thieu_he_so(so_diem, hat_giong):
    """Ban loi logic: giong het ham tren, bo he so 4 o dong cuoi."""
    bo_sinh = random.Random(hat_giong)
    trong = 0
    for _ in range(so_diem):
        x = bo_sinh.random()
        y = bo_sinh.random()
        if x * x + y * y < 1.0:
            trong = trong + 1
    return trong / so_diem


print("Ban thieu he so : "
      f"{uoc_luong_pi_thieu_he_so(SO_DIEM, HAT_GIONG):.6f}")


if __name__ == "__main__":
    _dung = uoc_luong_pi(SO_DIEM, HAT_GIONG)
    _thieu = uoc_luong_pi_thieu_he_so(SO_DIEM, HAT_GIONG)

    # Bản đúng phải gần số pi tới hai chữ số thập phân.
    assert abs(_dung - math.pi) < 0.01, \
        "ban dung phai gan so pi"

    # Bản lỗi đúng bằng một phần tư bản đúng, nên nó là lỗi hệ số
    # chứ không phải lỗi của phép gieo điểm.
    assert math.isclose(_thieu * 4.0, _dung), \
        "ban loi phai bang mot phan tu ban dung"

    # Bản lỗi vẫn chạy xong và trả về một số thực hợp lệ, tức là
    # nó không có thông báo lỗi nào.
    assert 0.0 < _thieu < 1.0, "ban loi van tra ve so hop le"

    print()
    print("Moi khang dinh dat.")
