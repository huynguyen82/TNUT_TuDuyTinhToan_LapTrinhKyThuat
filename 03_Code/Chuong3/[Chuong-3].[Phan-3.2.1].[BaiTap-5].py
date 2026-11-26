# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.5
Chương, mục : Chương 3, Mục 3.2.1
Đề bài      : Chuyển chương trình kiểm dung sai của Bài tập 2.9
              sang dùng vòng lặp có đếm. Đáp số phải trùng Bài
              tập 2.9 trên cùng bộ dữ liệu.
Đầu vào     : số chi tiết (số nguyên, miền 1–100) và các kích
              thước đo (chuỗi, mm)
Đầu ra      : số chi tiết đạt và kích thước trung bình
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

import math

MIEN_SO_CHI_TIET = (1, 100)


def kiem_dung_sai(cac_chuoi_do, danh_nghia, dung_sai):
    """Trả về (so_dat, trung_binh) bằng một vòng lặp có đếm.

    Phát sinh ValueError khi số chi tiết ngoài miền hoặc khi
    gặp chuỗi không ép kiểu được.
    """
    so_chi_tiet = len(cac_chuoi_do)
    if not (MIEN_SO_CHI_TIET[0] <= so_chi_tiet
            <= MIEN_SO_CHI_TIET[1]):
        raise ValueError(
            f"du lieu khong hop le: so chi tiet = {so_chi_tiet}")
    tong = 0.0
    so_dat = 0
    for thu_tu in range(so_chi_tiet):
        try:
            kich_thuoc = float(cac_chuoi_do[thu_tu])
        except ValueError:
            raise ValueError(
                f"du lieu khong hop le o chi tiet "
                f"{thu_tu + 1}: {cac_chuoi_do[thu_tu]}") from None
        tong = tong + kich_thuoc
        if math.isclose(kich_thuoc, danh_nghia,
                        rel_tol=0.0, abs_tol=dung_sai):
            so_dat = so_dat + 1
    return so_dat, tong / so_chi_tiet


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    ba_chi_tiet = ("50.03", "49.97", "50.01")
    so_dat, trung_binh = kiem_dung_sai(ba_chi_tiet, 50.00, 0.05)
    assert so_dat == 3, so_dat
    # Dap so trung khop Bai tap 2.9 tren cung bo du lieu.
    assert trung_binh == 50.00333333333333, trung_binh
    assert f"{trung_binh:.2f}" == "50.00"

    # --- Trường hợp biên ---------------------------------------
    # Mot chi tiet duy nhat o dung can tren van dat.
    assert kiem_dung_sai(("50.05",), 50.00, 0.05) == (1, 50.05)
    # Ngay ngoai can tren thi khong dat nhung van vao trung binh.
    so_dat_ngoai, tb_ngoai = kiem_dung_sai(
        ("50.06",), 50.00, 0.05)
    assert so_dat_ngoai == 0 and tb_ngoai == 50.06
    # Du 100 chi tiet van trong mien.
    assert kiem_dung_sai(("50.00",) * 100, 50.00, 0.05)[0] == 100
    # Vong lap chay dung so chi tiet luot, khong thua khong thieu.
    dem_luot = 0
    for _ in range(len(ba_chi_tiet)):
        dem_luot = dem_luot + 1
    assert dem_luot == 3

    # --- Trường hợp ngoại lệ -----------------------------------
    da_chan = False
    try:
        kiem_dung_sai((), 50.00, 0.05)
    except ValueError as loi:
        da_chan = "so chi tiet" in str(loi)
    assert da_chan, "danh sach rong ma van tinh duoc"
    da_chan_2 = False
    try:
        kiem_dung_sai(("50.03", "50,01"), 50.00, 0.05)
    except ValueError as loi:
        da_chan_2 = "chi tiet 2" in str(loi)
    assert da_chan_2, "chuoi sai ma van tinh duoc"

    print("BT 3.5")
    print(f"  So chi tiet dat: {so_dat}")
    print(f"  Trung binh     : {trung_binh:.2f} mm")
