# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.8
Chương, mục : Chương 4, Mục 4.3.1
Đề bài      : Bộ bốn hàm theo dõi ca trực, đúng một hàm sai;
              khoanh vùng hàm sai bằng ca kiểm thử từng hàm.
Đầu vào     : không có, mọi số liệu cố định trong mã
Đầu ra      : tên hàm sai và hai con số so sánh công soát
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

NGUONG = (60.0, 80.0, 100.0)
KET_THUC = -1.0
DAY_THUONG = (45.0, 72.5, 85.0, KET_THUC)


def la_ket_thuc(so_do):
    """Hàm 1, viết ĐÚNG."""
    return so_do == KET_THUC


def la_so_do_loi(so_do):
    """Hàm 2, viết ĐÚNG."""
    return so_do < 0 and not la_ket_thuc(so_do)


def phan_loai_sai(nhiet_do):
    """Hàm 3, viết SAI: nhánh đầu dùng dấu nhỏ hơn hoặc bằng."""
    if nhiet_do <= NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    return "dung may"


def phan_loai(nhiet_do):
    """Hàm 3, bản ĐÚNG sau khi sửa."""
    if nhiet_do < NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    return "dung may"


def dem_trang_thai(cac_so_do, ham_phan_loai):
    """Hàm 4, viết ĐÚNG; nhận hàm phân loại qua tham số."""
    binh_thuong = 0
    canh_bao = 0
    nguy_hiem = 0
    dung_may = 0
    so_loi = 0
    for thu_tu in range(len(cac_so_do)):
        so_do = cac_so_do[thu_tu]
        if la_ket_thuc(so_do):
            break
        if la_so_do_loi(so_do):
            so_loi = so_loi + 1
            continue
        trang_thai = ham_phan_loai(so_do)
        if trang_thai == "binh thuong":
            binh_thuong = binh_thuong + 1
        elif trang_thai == "canh bao":
            canh_bao = canh_bao + 1
        elif trang_thai == "nguy hiem":
            nguy_hiem = nguy_hiem + 1
        else:
            dung_may = dung_may + 1
    return binh_thuong, canh_bao, nguy_hiem, dung_may, so_loi


def bo_ca_ham_1_dat():
    """Ba ca cho hàm 1."""
    return (la_ket_thuc(-1.0) is True
            and la_ket_thuc(-1.1) is False
            and la_ket_thuc(45.0) is False)


def bo_ca_ham_2_dat():
    """Ba ca cho hàm 2."""
    return (la_so_do_loi(-5.0) is True
            and la_so_do_loi(-1.0) is False
            and la_so_do_loi(0.0) is False)


def bo_ca_ham_3_dat(ham_phan_loai):
    """Ba ca cho hàm 3; ca biên là số đo đúng bằng ngưỡng 60."""
    return (ham_phan_loai(45.0) == "binh thuong"
            and ham_phan_loai(60.0) == "canh bao"
            and ham_phan_loai(120.0) == "dung may")


def bo_ca_ham_4_dat(ham_phan_loai):
    """Ba ca cho hàm 4, dùng hàm phân loại đã cho."""
    day_loi = (45.0, -5.0, 72.5, KET_THUC)
    return (dem_trang_thai((), ham_phan_loai) == (0, 0, 0, 0, 0)
            and dem_trang_thai((KET_THUC,),
                               ham_phan_loai)[4] == 0
            and dem_trang_thai(day_loi, ham_phan_loai)[4] == 1)


def ham_sai(ham_phan_loai):
    """Tên hàm đầu tiên có bộ ca không đạt."""
    if not bo_ca_ham_1_dat():
        return "la_ket_thuc"
    if not bo_ca_ham_2_dat():
        return "la_so_do_loi"
    if not bo_ca_ham_3_dat(ham_phan_loai):
        return "phan_loai"
    if not bo_ca_ham_4_dat(ham_phan_loai):
        return "dem_trang_thai"
    return "khong ham nao"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Ba bo ca kia dat, bo ca ham 3 khong dat, nen khoanh vung
    # ham sai con dung mot ham.
    assert bo_ca_ham_1_dat() is True
    assert bo_ca_ham_2_dat() is True
    assert bo_ca_ham_3_dat(phan_loai_sai) is False
    assert bo_ca_ham_4_dat(phan_loai_sai) is True
    assert ham_sai(phan_loai_sai) == "phan_loai"
    # Sau khi sua, ca bon bo ca deu dat.
    assert ham_sai(phan_loai) == "khong ham nao"

    # --- Trường hợp biên ---------------------------------------
    # Chi so do dung bang nguong 60 phan biet hai ban cua ham 3.
    assert phan_loai_sai(60.0) == "binh thuong"
    assert phan_loai(60.0) == "canh bao"
    # So do 59,9 va 60,1 KHONG phan biet duoc hai ban.
    assert phan_loai_sai(59.9) == phan_loai(59.9)
    assert phan_loai_sai(60.1) == phan_loai(60.1)
    # Hai nguong con lai khong bi anh huong.
    assert phan_loai_sai(80.0) == phan_loai(80.0) == "nguy hiem"
    assert phan_loai_sai(100.0) == phan_loai(100.0) == "dung may"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Chi kiem ket qua cuoi: voi day thuong, hai ban cho CUNG mot
    # ket qua, nen cach do khong phat hien duoc loi.
    assert (dem_trang_thai(DAY_THUONG, phan_loai_sai)
            == dem_trang_thai(DAY_THUONG, phan_loai))
    # Phai doi day co so do 60,0 thi ket qua cuoi moi khac nhau.
    day_60 = (45.0, 60.0, 85.0, KET_THUC)
    assert (dem_trang_thai(day_60, phan_loai_sai)
            != dem_trang_thai(day_60, phan_loai))
    # Cong soat: kiem tung ham con 1 ham, kiem ket qua cuoi con 4.
    SO_HAM_PHAI_SOAT_KHI_KIEM_TUNG_HAM = 1
    SO_HAM_PHAI_SOAT_KHI_KIEM_KET_QUA_CUOI = 4
    assert (SO_HAM_PHAI_SOAT_KHI_KIEM_KET_QUA_CUOI
            // SO_HAM_PHAI_SOAT_KHI_KIEM_TUNG_HAM == 4)

    print("ham sai           :", ham_sai(phan_loai_sai))
    print("ban sai  o 60,0 C :", phan_loai_sai(60.0))
    print("ban dung o 60,0 C :", phan_loai(60.0))
    print("day thuong, ban sai :",
          dem_trang_thai(DAY_THUONG, phan_loai_sai))
    print("day co 60,0, ban sai:",
          dem_trang_thai(day_60, phan_loai_sai))
    print("day co 60,0, ban dung:",
          dem_trang_thai(day_60, phan_loai))
