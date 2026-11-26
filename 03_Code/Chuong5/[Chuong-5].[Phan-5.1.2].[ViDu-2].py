# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 2
Chương, mục : Chương 5, Mục 5.1.2
Đề bài      : Bốn đại lượng của bài toán A5 tính từ một danh
              sách 24 số đo: cực trị, trung bình, số giờ vượt
              ngưỡng.
Đầu vào     : 24 số đo cố định trong mã
Đầu ra      : giờ cao nhất, giờ thấp nhất, trung bình, số giờ
              vượt ngưỡng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

NGUONG = 50.0
ngay = [
    31.2, 28.5, 26.0, 25.1, 27.4, 34.8,
    48.6, 62.3, 71.5, 58.9, 44.2, 39.7,
    36.1, 35.4, 38.0, 42.6, 51.3, 64.8,
    69.2, 55.7, 46.3, 40.1, 36.8, 33.5,
]


# --- in-sach ---
def dem_vuot_nguong(day, nguong):
    """So gio co nong do vuot nguong."""
    vuot = 0
    for so_do in day:
        if so_do > nguong:
            vuot = vuot + 1
    return vuot


cao_nhat = max(ngay)
thap_nhat = min(ngay)
trung_binh = sum(ngay) / len(ngay)
so_gio_vuot = dem_vuot_nguong(ngay, NGUONG)

print(f"cao nhat   : {cao_nhat} luc {ngay.index(cao_nhat)} gio")
print(f"thap nhat  : {thap_nhat} luc {ngay.index(thap_nhat)} gio")
print(f"trung binh : {trung_binh:.2f}")
print(f"so gio vuot nguong {NGUONG}: {so_gio_vuot}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert cao_nhat == 71.5
    assert ngay.index(cao_nhat) == 8
    assert thap_nhat == 25.1
    assert ngay.index(thap_nhat) == 3
    assert f"{trung_binh:.4f}" == "43.6667"
    assert so_gio_vuot == 7

    # --- Trường hợp biên ---------------------------------------
    # So do dung bang nguong KHONG dem la vuot.
    assert dem_vuot_nguong([50.0], NGUONG) == 0
    assert dem_vuot_nguong([50.1], NGUONG) == 1
    # Day rong cho 0, khong bao loi.
    assert dem_vuot_nguong([], NGUONG) == 0
    # Mot phan tu: trung binh bang chinh no.
    assert sum([42.6]) / len([42.6]) == 42.6
    # Trung binh ngay KHONG vuot nguong du 7 gio vuot: trung binh
    # mot ngay khong noi duoc gi ve so gio vuot nguong.
    assert trung_binh < NGUONG and so_gio_vuot > 0
    # sum trung math.fsum tren day nay, Python 3.12 bu sai so.
    import math
    assert sum(ngay) == math.fsum(ngay)

    # --- Trường hợp ngoại lệ -----------------------------------
    # max cua danh sach rong bao loi.
    da_chan = False
    try:
        max([])
    except ValueError:
        da_chan = True
    assert da_chan, "max cua danh sach rong ma chay"
    # Khoi tao bien cuc dai bang 0 la SAI voi day toan so am.
    sai = 0.0
    for gia_tri in (-5.0, -12.0, -3.0):
        if gia_tri > sai:
            sai = gia_tri
    assert sai == 0.0
    assert max([-5.0, -12.0, -3.0]) == -3.0
    assert sai != max([-5.0, -12.0, -3.0])
