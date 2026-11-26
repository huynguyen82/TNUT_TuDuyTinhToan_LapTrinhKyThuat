# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.9
Chương, mục : Chương 1, Mục 1.3.1
Đề bài      : Từ tệp số liệu 12 động cơ của phân xưởng, tính
              tổng điện năng của riêng ca ngày và riêng ca đêm,
              và chỉ ra động cơ tiêu thụ nhiều nhất của mỗi ca.
Đầu vào     : 04_DuLieu/Chuong1_DongCo.csv, bốn trường mỗi dòng
Đầu ra      : hai tổng điện năng (kWh, một chữ số thập phân) và
              hai mã động cơ (số nguyên)
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng, lưu đồ và mã giả nằm ở tệp .md cùng tên.
Chương 1 không dạy đọc tệp bằng chương trình; phần đọc tệp ở
đây chỉ phục vụ việc kiểm chứng đáp số, không in vào sách.
"""

import csv
from pathlib import Path

CAC_CA_HOP_LE = ("ngay", "dem")
MIEN_CONG_SUAT = (0.37, 200.0)
MIEN_GIO_CHAY = (0.0, 24.0)
TEP_DU_LIEU = (
    Path(__file__).resolve().parents[2]
    / "04_DuLieu" / "Chuong1_DongCo.csv"
)


def doc_du_lieu(duong_dan=TEP_DU_LIEU):
    """Đọc tệp số liệu, trả về danh sách bốn trường mỗi dòng."""
    with duong_dan.open(encoding="utf-8", newline="") as tep:
        return [
            (int(dong["ma_dong_co"]),
             float(dong["cong_suat_kw"]),
             float(dong["gio_chay"]),
             dong["ca"].strip())
            for dong in csv.DictReader(tep)
        ]


def kiem_mot_dong(ma, cong_suat, gio_chay, ca):
    """Kiểm một dòng theo miền giá trị của bảng đặc tả."""
    if ca not in CAC_CA_HOP_LE:
        raise ValueError(
            f"du lieu khong hop le o dong co {ma}: ca = {ca}")
    if not MIEN_CONG_SUAT[0] <= cong_suat <= MIEN_CONG_SUAT[1]:
        raise ValueError(
            f"du lieu khong hop le o dong co {ma}: "
            f"cong suat = {cong_suat}")
    if not MIEN_GIO_CHAY[0] <= gio_chay <= MIEN_GIO_CHAY[1]:
        raise ValueError(
            f"du lieu khong hop le o dong co {ma}: "
            f"gio chay = {gio_chay}")


def tong_va_lon_nhat(cac_dong_co):
    """Phần chung của hai ca, rút ra bằng trừu tượng hoá.

    Trả về (tong_kwh, ma_lon_nhat). Nhóm rỗng trả về (0,0, None).
    Hai động cơ bằng nhau thì lấy mã nhỏ hơn.
    """
    tong = 0.0
    ma_lon_nhat = None
    lon_nhat = None
    for ma, cong_suat, gio_chay in sorted(cac_dong_co):
        dien_nang = cong_suat * gio_chay
        tong = tong + dien_nang
        if lon_nhat is None or dien_nang > lon_nhat:
            lon_nhat = dien_nang
            ma_lon_nhat = ma
    return round(tong, 1), ma_lon_nhat


def giai(cac_dong_co):
    """Trả về {ten_ca: (tong_kwh, ma_lon_nhat)} cho hai ca."""
    for dong in cac_dong_co:
        kiem_mot_dong(*dong)
    return {
        ten_ca: tong_va_lon_nhat([
            (ma, cong_suat, gio_chay)
            for ma, cong_suat, gio_chay, ca in cac_dong_co
            if ca == ten_ca
        ])
        for ten_ca in CAC_CA_HOP_LE
    }


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    cac_dong_co = doc_du_lieu()
    assert len(cac_dong_co) == 12, len(cac_dong_co)
    ket_qua = giai(cac_dong_co)
    assert ket_qua["ngay"] == (497.5, 2), ket_qua["ngay"]
    assert ket_qua["dem"] == (336.7, 5), ket_qua["dem"]
    # Tổng hai ca bằng tổng toàn phân xưởng.
    tong_hai_ca = ket_qua["ngay"][0] + ket_qua["dem"][0]
    assert abs(tong_hai_ca - 834.2) < 1e-9, tong_hai_ca

    # --- Trường hợp biên ---------------------------------------
    # Điểm biên mà bộ rút gọn năm dòng đầu không phủ được: ở ca
    # ngày của cả tệp có ba động cơ cùng 90,0 kWh là mã 2, 8 và
    # 10, nên quy tắc lấy mã nhỏ hơn mới có tác dụng. Năm dòng
    # đầu chỉ có một động cơ ngày lớn nhất nên không lộ ra.
    nam_dong_dau = cac_dong_co[:5]
    ket_qua_rut_gon = giai(nam_dong_dau)
    assert ket_qua_rut_gon["ngay"] == (238.0, 2)
    assert ket_qua_rut_gon["dem"] == (146.0, 5)
    cac_ngay = [
        (ma, cong_suat * gio)
        for ma, cong_suat, gio, ca in cac_dong_co if ca == "ngay"
    ]
    bang_90 = sorted(ma for ma, e in cac_ngay if e == 90.0)
    assert bang_90 == [2, 8, 10], bang_90
    assert len([ma for ma, e in cac_ngay[:3] if e == 90.0]) == 1
    # Tệp chỉ có ca ngày: tổng ca đêm bằng 0,0 và không có động
    # cơ lớn nhất của ca đêm.
    chi_ca_ngay = [
        dong for dong in cac_dong_co if dong[3] == "ngay"
    ]
    assert giai(chi_ca_ngay)["dem"] == (0.0, None)
    # Số giờ chạy bằng 0 là hợp lệ và cho điện năng bằng 0.
    assert tong_va_lon_nhat([(1, 7.5, 0.0)]) == (0.0, 1)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ca ghi sai phải bị chặn, kèm số thứ tự dòng và giá trị sai.
    da_chan = False
    try:
        giai([(7, 18.5, 5.0, "chieu")])
    except ValueError as loi:
        da_chan = "chieu" in str(loi) and "7" in str(loi)
    assert da_chan, "ca khong hop le ma van tinh duoc"
    # Công suất ngoài miền cũng bị chặn.
    da_chan_2 = False
    try:
        giai([(1, 500.0, 8.0, "ngay")])
    except ValueError as loi:
        da_chan_2 = "cong suat" in str(loi)
    assert da_chan_2, "cong suat ngoai mien ma van tinh duoc"

    print("BT 1.9")
    for ten_ca in CAC_CA_HOP_LE:
        tong, ma = ket_qua[ten_ca]
        print(f"  Ca {ten_ca:<5}: {tong:>7.1f} kWh, "
              f"dong co lon nhat so {ma}")
    print(f"  Bo rut gon 5 dong dau: ngay "
          f"{ket_qua_rut_gon['ngay']}, dem "
          f"{ket_qua_rut_gon['dem']}")
    print(f"  Diem bien bo rut gon khong phu: ba dong co cung "
          f"90,0 kWh o ca ngay, ma {bang_90}")
