# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.2
Chương, mục : Chương 1, Mục 1.3.1
Đề bài      : Cho một lưu đồ 8 khối tính tổng tải trên dầm, vi
              phạm hai trong năm quy tắc nối. Chỉ ra hai quy tắc
              bị vi phạm, nêu vị trí, và vẽ lại phần sai.
Đầu vào     : lưu đồ 8 khối mô tả bằng dữ liệu
Đầu ra      : danh sách số thứ tự quy tắc bị vi phạm
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên. Tệp này mô tả lưu đồ
đề bài và lưu đồ đã sửa bằng dữ liệu, rồi khẳng định kết quả
kiểm năm quy tắc.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cong_cu_luu_do import kiem_luu_do, so_khoi  # noqa: E402

# Lưu đồ của đề bài: 8 khối, tính tổng tải rồi so với tải cho
# phép. Khối kiem_nguong chỉ vẽ một lối ra, và nhánh cong_don
# quay về chính nó nên không bao giờ tới khối kết thúc.
KHOI_DE_BAI = {
    "bat_dau": "bat_dau",
    "nhap": "nhap",
    "khoi_tao": "xu_ly",
    "kiem_con_tai": "dieu_kien",
    "cong_don": "xu_ly",
    "kiem_nguong": "dieu_kien",
    "xuat": "xuat",
    "ket_thuc": "ket_thuc",
}
CANH_DE_BAI = [
    ("bat_dau", "nhap", ""),
    ("nhap", "khoi_tao", ""),
    ("khoi_tao", "kiem_con_tai", ""),
    ("kiem_con_tai", "cong_don", "Dung"),
    ("kiem_con_tai", "kiem_nguong", "Sai"),
    ("cong_don", "cong_don", ""),
    ("kiem_nguong", "xuat", "Dung"),
    ("xuat", "ket_thuc", ""),
]

# Lưu đồ đã sửa: nhánh cong_don quay về khối điều kiện, và khối
# kiem_nguong có đủ hai lối ra khác nhau.
KHOI_DA_SUA = dict(KHOI_DE_BAI, xuat_khong_dat="xuat")
CANH_DA_SUA = [
    ("bat_dau", "nhap", ""),
    ("nhap", "khoi_tao", ""),
    ("khoi_tao", "kiem_con_tai", ""),
    ("kiem_con_tai", "cong_don", "Dung"),
    ("kiem_con_tai", "kiem_nguong", "Sai"),
    ("cong_don", "kiem_con_tai", ""),
    ("kiem_nguong", "xuat", "Dung"),
    ("kiem_nguong", "xuat_khong_dat", "Sai"),
    ("xuat", "ket_thuc", ""),
    ("xuat_khong_dat", "ket_thuc", ""),
]

# Lưu đồ có hai khối bắt đầu, dùng cho trường hợp không hợp lệ.
KHOI_HAI_BAT_DAU = dict(KHOI_DA_SUA, bat_dau_2="bat_dau")
CANH_HAI_BAT_DAU = CANH_DA_SUA + [("bat_dau_2", "nhap", "")]


def tong_tai(cac_tai):
    """Tổng tải trên dầm, kN."""
    return sum(cac_tai)


def ket_luan_ben(cac_tai, tai_cho_phep):
    """Kết luận điều kiện bền: đạt khi tổng tải không vượt tải
    cho phép."""
    return tong_tai(cac_tai) <= tai_cho_phep


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Lưu đồ đề bài vi phạm đúng hai quy tắc: quy tắc 2 vì nhánh
    # cong_don quay về chính nó, và quy tắc 3 vì khối kiem_nguong
    # chỉ có một lối ra.
    vi_pham = kiem_luu_do(KHOI_DE_BAI, CANH_DE_BAI)
    assert vi_pham == [2, 3], vi_pham
    assert so_khoi(KHOI_DE_BAI) == 8, so_khoi(KHOI_DE_BAI)

    # Lưu đồ đã sửa không còn vi phạm quy tắc nào.
    assert kiem_luu_do(KHOI_DA_SUA, CANH_DA_SUA) == [], \
        kiem_luu_do(KHOI_DA_SUA, CANH_DA_SUA)
    assert so_khoi(KHOI_DA_SUA) == 9

    # Tổng tải của bộ dữ liệu đề bài.
    cac_tai = [8.0, 12.0, 6.0, 15.0]
    assert tong_tai(cac_tai) == 41.0
    assert ket_luan_ben(cac_tai, 50.0) is True

    # --- Trường hợp biên ---------------------------------------
    # Tổng tải đúng bằng tải cho phép vẫn được coi là đạt.
    assert ket_luan_ben([50.0], 50.0) is True
    assert ket_luan_ben([50.1], 50.0) is False
    # Dãy tải rỗng cho tổng 0,0 kN và kết luận đạt.
    assert tong_tai([]) == 0.0
    assert ket_luan_ben([], 50.0) is True
    # Sửa riêng quy tắc 2 mà chưa sửa quy tắc 3 thì vẫn còn một
    # vi phạm, nên phải sửa cả hai chỗ.
    canh_sua_mot_nua = [
        canh for canh in CANH_DE_BAI
        if canh != ("cong_don", "cong_don", "")
    ] + [("cong_don", "kiem_con_tai", "")]
    assert kiem_luu_do(KHOI_DE_BAI, canh_sua_mot_nua) == [3]

    # --- Trường hợp ngoại lệ -----------------------------------
    # Lưu đồ có hai khối bắt đầu vi phạm quy tắc 1.
    assert 1 in kiem_luu_do(KHOI_HAI_BAT_DAU, CANH_HAI_BAT_DAU)
    # Dạng khối ngoài bảy dạng hợp lệ phải bị chặn.
    da_chan = False
    try:
        kiem_luu_do(dict(KHOI_DA_SUA, la="hinh_sao"), CANH_DA_SUA)
    except ValueError:
        da_chan = True
    assert da_chan, "dang khoi khong hop le ma van chay"

    print("BT 1.2")
    print(f"  Luu do de bai vi pham quy tac: {vi_pham}")
    print(f"  Luu do da sua vi pham quy tac: "
          f"{kiem_luu_do(KHOI_DA_SUA, CANH_DA_SUA)}")
