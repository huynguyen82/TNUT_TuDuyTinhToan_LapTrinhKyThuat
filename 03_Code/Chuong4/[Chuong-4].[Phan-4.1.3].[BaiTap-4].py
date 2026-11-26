# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.4
Chương, mục : Chương 4, Mục 4.1.3
Đề bài      : Hàm tính giá trị hiện tại, lãi suất là tham số
              mặc định; gọi theo ba cách.
Đầu vào     : giá trị tương lai, số kỳ, lãi suất tuỳ chọn
Đầu ra      : ba giá trị hiện tại, hai chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

LAI_SUAT_THANG = 0.008
MIEN_SO_KY = (0, 600)
MIEN_LAI_SUAT = (0.0, 0.05)


def gia_tri_hien_tai(gia_tri_tuong_lai, so_ky,
                     lai_suat=LAI_SUAT_THANG):
    """Giá trị hiện tại của một dòng tiền tương lai, nghìn đồng.

    Tham số lai_suat có giá trị mặc định 0,008 một kỳ, là lãi
    suất thường dùng của bài toán. Phát sinh ValueError khi số
    kỳ hoặc lãi suất nằm ngoài miền.
    """
    if not MIEN_SO_KY[0] <= so_ky <= MIEN_SO_KY[1]:
        raise ValueError(f"du lieu khong hop le: so ky = {so_ky}")
    if not MIEN_LAI_SUAT[0] <= lai_suat <= MIEN_LAI_SUAT[1]:
        raise ValueError(
            f"du lieu khong hop le: lai suat = {lai_suat}")
    return gia_tri_tuong_lai / (1 + lai_suat) ** so_ky


def ba_cach_goi(gia_tri_tuong_lai, so_ky):
    """Ba cách gọi cùng một hàm, cho cùng một kết quả."""
    bo_qua = gia_tri_hien_tai(gia_tri_tuong_lai, so_ky)
    theo_thu_tu = gia_tri_hien_tai(
        gia_tri_tuong_lai, so_ky, LAI_SUAT_THANG)
    theo_ten = gia_tri_hien_tai(
        gia_tri_tuong_lai, so_ky, lai_suat=LAI_SUAT_THANG)
    return bo_qua, theo_thu_tu, theo_ten


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert f"{gia_tri_hien_tai(100000.0, 12):.2f}" == "90881.11"
    bo_qua, theo_thu_tu, theo_ten = ba_cach_goi(100000.0, 12)
    assert bo_qua == theo_thu_tu == theo_ten
    # Chuoi tai lieu noi ro gia tri mac dinh.
    assert "0,008" in gia_tri_hien_tai.__doc__

    # --- Trường hợp biên ---------------------------------------
    # So ky bang 0: gia tri hien tai bang dung gia tri tuong lai.
    assert gia_tri_hien_tai(100000.0, 0) == 100000.0
    # Lai suat 0: khong chiet khau, moi so ky cho cung ket qua.
    assert gia_tri_hien_tai(100000.0, 12, 0.0) == 100000.0
    assert gia_tri_hien_tai(100000.0, 600, 0.0) == 100000.0
    # So ky dung bang can tren cua mien van hop le.
    assert gia_tri_hien_tai(100000.0, 600) > 0.0
    # Lai suat cao hon lam gia tri hien tai nho hon.
    assert (gia_tri_hien_tai(100000.0, 12, 0.015)
            < gia_tri_hien_tai(100000.0, 12, 0.008))

    # --- Trường hợp ngoại lệ -----------------------------------
    da_chan = 0
    for thu_tu in range(3):
        bo = ((100000.0, -3, 0.008), (100000.0, 601, 0.008),
              (100000.0, 12, 0.5))[thu_tu]
        try:
            gia_tri_hien_tai(bo[0], bo[1], bo[2])
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 3, "co bo du lieu khong hop le ma khong chan"
    # Khong chan thi so ky am cho ket qua LON hon gia tri tuong lai.
    assert 100000.0 / (1 + 0.008) ** -3 > 100000.0

    print(f"bo qua tham so  : {bo_qua:.2f}")
    print(f"truyen thu tu   : {theo_thu_tu:.2f}")
    print(f"truyen theo ten : {theo_ten:.2f}")
