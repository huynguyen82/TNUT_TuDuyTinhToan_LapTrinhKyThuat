# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.6
Chương, mục : Chương 3, Mục 3.2.3
Đề bài      : Đếm số giờ PM2.5 vượt ngưỡng trong một ca, bỏ qua
              số đo lỗi là số âm bằng lệnh continue. Báo cả số
              giờ vượt ngưỡng lẫn số số đo lỗi đã bỏ qua.
Đầu vào     : các số đo (µg/m³) của một ca
Đầu ra      : số giờ vượt ngưỡng và số số đo lỗi
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

NGUONG_PM25 = 50.0


def dem_gio_vuot(cac_so_do):
    """Trả về (so_gio_vuot, so_do_loi).

    Số đo âm là lỗi cảm biến: bỏ qua bằng continue chứ không
    dừng vòng lặp, để các giờ sau vẫn được xử lý.
    """
    so_gio_vuot = 0
    so_do_loi = 0
    for thu_tu in range(len(cac_so_do)):
        so_do = cac_so_do[thu_tu]
        if so_do < 0:
            so_do_loi = so_do_loi + 1
            continue
        if so_do > NGUONG_PM25:
            so_gio_vuot = so_gio_vuot + 1
    return so_gio_vuot, so_do_loi


def dem_gio_vuot_dung_break(cac_so_do):
    """Biến thể sai dùng break thay continue, để so sánh."""
    so_gio_vuot = 0
    so_do_loi = 0
    for thu_tu in range(len(cac_so_do)):
        so_do = cac_so_do[thu_tu]
        if so_do < 0:
            so_do_loi = so_do_loi + 1
            break
        if so_do > NGUONG_PM25:
            so_gio_vuot = so_gio_vuot + 1
    return so_gio_vuot, so_do_loi


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    sau_so_do = (42.0, 55.0, 61.0, 48.0, 50.0, 73.0)
    assert dem_gio_vuot(sau_so_do) == (3, 0)

    # --- Trường hợp biên ---------------------------------------
    # So do dung bang nguong khong duoc dem, vi dung dau lon hon.
    assert dem_gio_vuot((50.0,)) == (0, 0)
    assert dem_gio_vuot((50.1,)) == (1, 0)
    # Day rong: vong lap chay 0 luot, hai so dem giu gia tri 0.
    assert dem_gio_vuot(()) == (0, 0)
    # So do loi o giua: cac gio sau van duoc xu ly.
    co_loi = (42.0, -5.0, 61.0, 73.0)
    assert dem_gio_vuot(co_loi) == (2, 1)
    # Dung break thay continue lam mat hai gio vuot nguong sau do.
    assert dem_gio_vuot_dung_break(co_loi) == (0, 1)
    assert dem_gio_vuot(co_loi) != dem_gio_vuot_dung_break(co_loi)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Moi so do deu loi: khong gio nao vuot, va so do loi bang
    # so phan tu. Hai cach khac nhau ngay o ca nay.
    toan_loi = (-1.0, -2.0, -3.0)
    assert dem_gio_vuot(toan_loi) == (0, 3)
    assert dem_gio_vuot_dung_break(toan_loi) == (0, 1)

    print("BT 3.6")
    for ten, day in (("binh thuong", sau_so_do),
                     ("co so do loi", co_loi)):
        vuot, loi = dem_gio_vuot(day)
        print(f"  {ten:<14}{vuot} gio vuot nguong, "
              f"{loi} so do loi")
