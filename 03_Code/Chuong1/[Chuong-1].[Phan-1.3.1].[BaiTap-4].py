# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.4
Chương, mục : Chương 1, Mục 1.3.1
Đề bài      : Vẽ lưu đồ tuần tự tính tổn thất công suất trên
              đường dây, dựa trên bảng đặc tả của Bài tập 1.3.
              Lưu đồ phải có khối kiểm dữ liệu đầu vào đặt trước
              khối tính và phải thoả cả năm quy tắc nối.
Đầu vào     : bảng đặc tả của Bài tập 1.3
Đầu ra      : lưu đồ mô tả bằng dữ liệu, kèm số khối
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng và mô tả hình vẽ nằm ở tệp .md cùng tên.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cong_cu_luu_do import kiem_luu_do, so_khoi  # noqa: E402

# Lưu đồ lời giải: bảy khối. Khối kiem_dau_vao đứng trước khối
# tinh_ton_that, và nhánh Sai của nó cũng dẫn tới khối kết thúc.
KHOI_LOI_GIAI = {
    "bat_dau": "bat_dau",
    "nhap": "nhap",
    "kiem_dau_vao": "dieu_kien",
    "tinh_ton_that": "xu_ly",
    "xuat_ket_qua": "xuat",
    "xuat_loi": "xuat",
    "ket_thuc": "ket_thuc",
}
CANH_LOI_GIAI = [
    ("bat_dau", "nhap", ""),
    ("nhap", "kiem_dau_vao", ""),
    ("kiem_dau_vao", "tinh_ton_that", "Dung"),
    ("kiem_dau_vao", "xuat_loi", "Sai"),
    ("tinh_ton_that", "xuat_ket_qua", ""),
    ("xuat_ket_qua", "ket_thuc", ""),
    ("xuat_loi", "ket_thuc", ""),
]

# Biến thể sai hay gặp: đặt khối kiểm sau khối tính.
KHOI_KIEM_SAU = dict(KHOI_LOI_GIAI)
CANH_KIEM_SAU = [
    ("bat_dau", "nhap", ""),
    ("nhap", "tinh_ton_that", ""),
    ("tinh_ton_that", "kiem_dau_vao", ""),
    ("kiem_dau_vao", "xuat_ket_qua", "Dung"),
    ("kiem_dau_vao", "xuat_loi", "Sai"),
    ("xuat_ket_qua", "ket_thuc", ""),
    ("xuat_loi", "ket_thuc", ""),
]

MIEN_DONG_DIEN = (0.0, 1000.0)
MIEN_DIEN_TRO = (0.01, 5.00)
MIEN_CHIEU_DAI = (0.0, 100.0)


def trong_mien(gia_tri, mien):
    """Giá trị có nằm trong miền đóng đã khai báo hay không."""
    return mien[0] <= gia_tri <= mien[1]


def dau_vao_hop_le(dong_dien, dien_tro, chieu_dai):
    """Khối điều kiện kiem_dau_vao của lưu đồ."""
    return (trong_mien(dong_dien, MIEN_DONG_DIEN)
            and trong_mien(dien_tro, MIEN_DIEN_TRO)
            and trong_mien(chieu_dai, MIEN_CHIEU_DAI))


def chay_luu_do(dong_dien, dien_tro, chieu_dai):
    """Thực hiện lưu đồ lời giải, trả về (duong_di, dau_ra).

    duong_di là danh sách mã khối đã đi qua, dùng để đối chiếu
    với ba bộ dữ liệu kiểm thử của đề bài.
    """
    duong_di = ["bat_dau", "nhap", "kiem_dau_vao"]
    if not dau_vao_hop_le(dong_dien, dien_tro, chieu_dai):
        duong_di += ["xuat_loi", "ket_thuc"]
        return duong_di, "du lieu khong hop le"
    ton_that = dong_dien ** 2 * dien_tro * chieu_dai
    duong_di += ["tinh_ton_that", "xuat_ket_qua", "ket_thuc"]
    return duong_di, f"{ton_that:.2f}"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert kiem_luu_do(KHOI_LOI_GIAI, CANH_LOI_GIAI) == [], \
        kiem_luu_do(KHOI_LOI_GIAI, CANH_LOI_GIAI)
    assert so_khoi(KHOI_LOI_GIAI) == 7, so_khoi(KHOI_LOI_GIAI)
    duong_di, dau_ra = chay_luu_do(50.0, 0.25, 1.2)
    assert dau_ra == "750.00", dau_ra
    assert "tinh_ton_that" in duong_di
    assert duong_di[-1] == "ket_thuc"

    # --- Trường hợp biên ---------------------------------------
    # Chiều dài bằng 0 vẫn đi qua nhánh Đúng của khối kiểm.
    duong_di_bien, dau_ra_bien = chay_luu_do(50.0, 0.25, 0.0)
    assert dau_ra_bien == "0.00", dau_ra_bien
    assert "xuat_ket_qua" in duong_di_bien
    assert "xuat_loi" not in duong_di_bien
    # Điện trở đúng ở cận dưới 0,01 Ω/km vẫn hợp lệ.
    assert dau_vao_hop_le(50.0, 0.01, 1.2)
    assert not dau_vao_hop_le(50.0, 0.0, 1.2)
    # Lưu đồ đặt khối kiểm sau khối tính vẫn thoả năm quy tắc
    # nối, nên bộ kiểm quy tắc không bắt được lỗi này; chỉ có
    # việc truy vết đường đi mới cho thấy phép tính đã chạy
    # trước khi dữ liệu được kiểm.
    assert kiem_luu_do(KHOI_KIEM_SAU, CANH_KIEM_SAU) == []
    thu_tu_sai = [ma for _, ma, _ in CANH_KIEM_SAU]
    assert (thu_tu_sai.index("tinh_ton_that")
            < thu_tu_sai.index("kiem_dau_vao"))

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dòng điện âm đi qua nhánh Sai, và nhánh đó cũng tới được
    # khối kết thúc.
    duong_di_loi, dau_ra_loi = chay_luu_do(-10.0, 0.25, 1.2)
    assert dau_ra_loi == "du lieu khong hop le"
    assert "tinh_ton_that" not in duong_di_loi
    assert duong_di_loi[-1] == "ket_thuc"

    print("BT 1.4")
    print(f"  So khoi: {so_khoi(KHOI_LOI_GIAI)}")
    for tham_so in ((50.0, 0.25, 1.2), (50.0, 0.25, 0.0),
                    (-10.0, 0.25, 1.2)):
        di, ra = chay_luu_do(*tham_so)
        print(f"  {tham_so} -> {ra}")
        print(f"    duong di: {' > '.join(di)}")
