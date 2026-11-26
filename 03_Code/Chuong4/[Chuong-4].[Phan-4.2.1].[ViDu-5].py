# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 5
Chương, mục : Chương 4, Mục 4.2.1
Đề bài      : Hàm đếm của bộ bốn hàm và chương trình chính,
              tiếp nối ba hàm nhỏ của Ví dụ 4.
Đầu vào     : dãy số đo cố định trong mã
Đầu ra      : bốn số đếm trạng thái và số số đo lỗi
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

NGUONG = (60.0, 80.0, 100.0)
KET_THUC = -1.0


def la_ket_thuc(so_do):
    """So do co phai gia tri ket thuc hay khong."""
    return so_do == KET_THUC


def la_so_do_loi(so_do):
    """So do co phai loi cam bien hay khong."""
    return so_do < 0 and not la_ket_thuc(so_do)


def phan_loai(nhiet_do):
    """Trang thai theo bon mien cua Muc 3.1.1."""
    if nhiet_do < NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    return "dung may"


# --- in-sach ---
def dem_trang_thai(cac_so_do):
    """Dem so lan cua tung trang thai va so so do loi."""
    cac_dem = {"binh thuong": 0, "canh bao": 0,
               "nguy hiem": 0, "dung may": 0}
    so_loi = 0
    for thu_tu in range(len(cac_so_do)):
        so_do = cac_so_do[thu_tu]
        if la_ket_thuc(so_do):
            break
        if la_so_do_loi(so_do):
            so_loi = so_loi + 1
            continue
        cac_dem[phan_loai(so_do)] += 1
    return cac_dem, so_loi


day_so_do = (45.0, 72.5, 85.0, -5.0, 120.0, KET_THUC)
cac_dem, so_loi = dem_trang_thai(day_so_do)
for ten in ("binh thuong", "canh bao", "nguy hiem", "dung may"):
    print(f"{ten:<14}{cac_dem[ten]}")
print(f"{'so do loi':<14}{so_loi}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert cac_dem["binh thuong"] == 1
    assert cac_dem["dung may"] == 1
    assert so_loi == 1

    # --- Trường hợp biên ---------------------------------------
    # Ba ham nho kiem rieng duoc, khong can chay ham thu tu.
    assert la_ket_thuc(-1.0) is True
    assert la_ket_thuc(-1.1) is False
    assert la_so_do_loi(-5.0) is True
    assert la_so_do_loi(-1.0) is False
    assert la_so_do_loi(0.0) is False
    assert phan_loai(59.9) == "binh thuong"
    assert phan_loai(60.0) == "canh bao"
    assert phan_loai(100.0) == "dung may"
    # Day rong cho bon so dem bang 0.
    dem_rong, loi_rong = dem_trang_thai(())
    assert sum(dem_rong.values()) == 0 and loi_rong == 0
    # Day chi co gia tri ket thuc cung cho bon so dem bang 0.
    assert dem_trang_thai((KET_THUC,))[1] == 0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ham phan_loai khong chan nhiet do ngoai mien do duoc; day
    # la gioi han da biet, xem Khoi 8.
    assert phan_loai(1000.0) == "dung may"
    # Goi dem_trang_thai voi doi so khong duyet duoc phai bao loi.
    da_chan = False
    try:
        dem_trang_thai(5)
    except TypeError:
        da_chan = True
    assert da_chan, "doi so khong duyet duoc ma van chay"
