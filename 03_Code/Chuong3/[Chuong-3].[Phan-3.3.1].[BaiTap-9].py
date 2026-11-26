# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.9
Chương, mục : Chương 3, Mục 2.3.1 và cả sáu tiểu mục Chương 3
Đề bài      : Theo dõi nhiệt độ một ca trực: đọc số đo tới khi
              gặp giá trị kết thúc, phân loại theo bốn miền,
              đếm từng trạng thái, bỏ qua số đo lỗi, và dừng
              ngay khi gặp trạng thái dừng máy.
Đầu vào     : các số đo (°C); giá trị kết thúc −1
Đầu ra      : bốn số đếm, số số đo lỗi, và lý do dừng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

GIA_TRI_KET_THUC = -1.0
NGUONG = (60.0, 80.0, 100.0)
LY_DO_HET = "het so do"
LY_DO_DUNG_MAY = "gap trang thai dung may"


def phan_loai(nhiet_do):
    """Trạng thái theo bốn miền của Mục 3.1.1."""
    if nhiet_do < NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    else:
        return "dung may"


def theo_doi_ca(cac_so_do):
    """Trả về (cac_dem, so_do_loi, ly_do_dung).

    Thứ tự kiểm trong thân vòng lặp quyết định kết quả: kiểm
    giá trị kết thúc trước, rồi số đo lỗi, rồi mới phân loại.
    """
    cac_dem = {
        "binh thuong": 0, "canh bao": 0,
        "nguy hiem": 0, "dung may": 0,
    }
    so_do_loi = 0
    ly_do_dung = LY_DO_HET
    thu_tu = 0
    while thu_tu < len(cac_so_do):
        so_do = cac_so_do[thu_tu]
        thu_tu = thu_tu + 1
        if so_do == GIA_TRI_KET_THUC:
            break
        if so_do < 0:
            so_do_loi = so_do_loi + 1
            continue
        trang_thai = phan_loai(so_do)
        cac_dem[trang_thai] = cac_dem[trang_thai] + 1
        if trang_thai == "dung may":
            ly_do_dung = LY_DO_DUNG_MAY
            break
    return cac_dem, so_do_loi, ly_do_dung


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    cac_dem, so_do_loi, ly_do = theo_doi_ca(
        (45.0, 72.5, 85.0, GIA_TRI_KET_THUC))
    assert cac_dem["binh thuong"] == 1
    assert cac_dem["canh bao"] == 1
    assert cac_dem["nguy hiem"] == 1
    assert cac_dem["dung may"] == 0
    assert so_do_loi == 0
    assert ly_do == LY_DO_HET

    # --- Trường hợp biên ---------------------------------------
    # Gap trang thai dung may thi dung ngay, so do sau khong doc.
    dem_dung, loi_dung, ly_do_dung = theo_doi_ca(
        (45.0, 120.0, 50.0, GIA_TRI_KET_THUC))
    assert dem_dung["dung may"] == 1
    assert dem_dung["binh thuong"] == 1
    assert ly_do_dung == LY_DO_DUNG_MAY
    # So do 50.0 nam sau 120.0 nen khong duoc dem.
    assert dem_dung["binh thuong"] != 2
    # Day rong va day chi co gia tri ket thuc cho ket qua giong
    # nhau: khong dem gi, dung vi het so do.
    assert theo_doi_ca(())[0]["binh thuong"] == 0
    assert theo_doi_ca((GIA_TRI_KET_THUC,))[2] == LY_DO_HET
    # Nhiet do dung bang nguong thuoc mien phia tren.
    assert phan_loai(60.0) == "canh bao"
    assert phan_loai(100.0) == "dung may"

    # --- Trường hợp ngoại lệ -----------------------------------
    # So do am khac gia tri ket thuc bi bo qua, cac so do sau
    # van duoc xu ly.
    dem_loi, so_loi, _ = theo_doi_ca(
        (45.0, -5.0, 72.5, GIA_TRI_KET_THUC))
    assert so_loi == 1
    assert dem_loi["binh thuong"] == 1
    assert dem_loi["canh bao"] == 1
    # Gia tri ket thuc phai duoc kiem truoc kiem so do loi, neu
    # khong thi -1 bi dem nham vao so do loi.
    assert theo_doi_ca((GIA_TRI_KET_THUC,))[1] == 0

    print("BT 3.9")
    for ten, day in (
            ("binh thuong", (45.0, 72.5, 85.0, GIA_TRI_KET_THUC)),
            ("co dung may", (45.0, 120.0, 50.0,
                             GIA_TRI_KET_THUC)),
            ("co so do loi", (45.0, -5.0, 72.5,
                              GIA_TRI_KET_THUC))):
        dem, loi, ly = theo_doi_ca(day)
        print(f"  {ten:<14}{dem} loi={loi} ly_do={ly}")
