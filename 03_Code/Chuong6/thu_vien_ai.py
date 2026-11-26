# -*- coding: utf-8 -*-
"""
Mã bài      : minh chứng nhóm lỗi thứ hai của Mục 6.4.1
Chương, mục : Chương 6, Mục 6.4.1
Đề bài      : Một module phụ trợ do công cụ AI sinh, dùng tên hàm
              `numpy.trapz` đã thôi dùng ở NumPy 2.x. Module này
              tồn tại riêng để cho thấy cảnh báo thôi dùng **không**
              hiện ra khi lời gọi nằm ngoài module `__main__`.
Đầu vào     : một dãy số thực và bước lưới
Đầu ra      : diện tích dưới đường cong
Python      : 3.12
Thư viện    : NumPy 2.1.3
Cài đặt     : pip install -r 03_Code/requirements.txt
"""

import numpy as np


def dien_tich_ten_cu(day, buoc=1.0):
    """Dien tich duoi duong cong, dung ten ham da thoi dung."""
    return float(np.trapz(day, dx=buoc))


def dien_tich_ten_moi(day, buoc=1.0):
    """Dien tich duoi duong cong, dung ten ham cua NumPy 2.x."""
    return float(np.trapezoid(day, dx=buoc))


if __name__ == "__main__":
    _day = [0.0, 1.0, 2.0, 3.0]
    _cu = dien_tich_ten_cu(_day)
    _moi = dien_tich_ten_moi(_day)
    print(f"Ten cu : {_cu}")
    print(f"Ten moi: {_moi}")

    # Hai tên hàm cho đúng cùng một kết quả, nên không ca kiểm thử
    # nào trên kết quả phân biệt được hai bản.
    assert _cu == _moi, "hai ten ham phai cho cung ket qua"

    # Quy tắc hình thang trên 0, 1, 2, 3 với bước 1 cho 4,5.
    assert _cu == 4.5, "dien tich phai bang 4,5"

    # Tên cũ vẫn còn trong NumPy 2.1.3, nên lỗi này không phải
    # AttributeError mà là một cảnh báo thôi dùng.
    assert hasattr(np, "trapz"), "ten cu phai con ton tai"

    print("Moi khang dinh dat.")
