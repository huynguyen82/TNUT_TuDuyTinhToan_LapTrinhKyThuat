# -*- coding: utf-8 -*-
"""
Mã bài      : Chương trình mẫu Chương 4
Chương, mục : Chương 4, mục Chương trình mẫu
Đề bài      : Chương trình phiếu ca trực của Chương 3, nay tách
              thành bộ hàm. Cùng một đề bài, cùng một kết quả; chỉ
              cấu trúc đổi. Mỗi hàm có chuỗi tài liệu và kiểm
              riêng được bằng một bộ dữ liệu nhỏ.
Đầu vào     : dãy số đo nhiệt độ gõ từ bàn phím, đơn vị độ C,
              kết thúc bằng -1; số đo âm khác -1 là lỗi cảm biến
Đầu ra      : phiếu ca trực, giống hệt bản Chương 3
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Chương 4 chưa có danh sách, nên bốn số đếm vẫn truyền qua lại
dưới dạng bốn giá trị riêng. Chương 5 thay chúng bằng một cấu
trúc dữ liệu.
"""

NGUONG_CANH_BAO = 60.0
NGUONG_NGUY_HIEM = 80.0
NGUONG_DUNG_MAY = 100.0
KET_THUC = -1.0
LOI_NHAC = "So do (do C), -1 de ket thuc: "


# --- in-sach ---
def la_so_do_loi(so_do):
    """So do co phai loi cam bien; -1 la dau hieu dung."""
    return so_do < 0.0 and so_do != KET_THUC


def phan_loai(nhiet_do, nguong_canh_bao=NGUONG_CANH_BAO):
    """Trang thai theo bon mien cua Muc 3.1.1.

    Nguong canh bao nhan qua tham so co gia tri mac dinh.
    """
    if nhiet_do < nguong_canh_bao:
        return "binh thuong"
    if nhiet_do < NGUONG_NGUY_HIEM:
        return "canh bao"
    if nhiet_do < NGUONG_DUNG_MAY:
        return "nguy hiem"
    return "dung may"


def trung_binh(tong, so_hop_le):
    """Nhiet do trung binh. Tra ve None khi khong co so do nao."""
    if so_hop_le == 0:
        return None
    return tong / so_hop_le
# --- het-in-sach ---


def in_phieu(binh_thuong, canh_bao, nguy_hiem, dung_may,
             so_loi, tb):
    """In phieu ca truc, mot dong cho moi dai luong."""
    print()
    print(f"{'PHIEU CA TRUC':<22}")
    print(f"{'Binh thuong':<22}{binh_thuong:>6}")
    print(f"{'Canh bao':<22}{canh_bao:>6}")
    print(f"{'Nguy hiem':<22}{nguy_hiem:>6}")
    print(f"{'Dung may':<22}{dung_may:>6}")
    print(f"{'So do loi':<22}{so_loi:>6}")
    if tb is None:
        print(f"{'Trung binh (do C)':<22}{'khong co':>6}")
    else:
        print(f"{'Trung binh (do C)':<22}{tb:>6.1f}")
    ket_luan = "DUNG MAY" if dung_may > 0 else "tiep tuc"
    print(f"{'Ket luan':<22}{ket_luan:>6}")


def chay_ca_truc():
    """Doc het mot ca truc. Tra ve nam so dem va tong."""
    binh_thuong = canh_bao = nguy_hiem = dung_may = so_loi = 0
    tong = 0.0
    so_do = float(input(LOI_NHAC))
    while so_do != KET_THUC:
        if la_so_do_loi(so_do):
            so_loi = so_loi + 1
            so_do = float(input(LOI_NHAC))
            continue
        tong = tong + so_do
        trang_thai = phan_loai(so_do)
        if trang_thai == "binh thuong":
            binh_thuong = binh_thuong + 1
        elif trang_thai == "canh bao":
            canh_bao = canh_bao + 1
        elif trang_thai == "nguy hiem":
            nguy_hiem = nguy_hiem + 1
        else:
            dung_may = dung_may + 1
            break
        so_do = float(input(LOI_NHAC))
    return binh_thuong, canh_bao, nguy_hiem, dung_may, so_loi, tong


BT, CB, NH, DM, SL, TONG = chay_ca_truc()
SO_HOP_LE = BT + CB + NH + DM
in_phieu(BT, CB, NH, DM, SL, trung_binh(TONG, SO_HOP_LE))


if __name__ == "__main__":
    # --- Kiểm riêng từng hàm, không cần chạy cả chương trình ----
    # Hàm phan_loai: ba ca thường, ba ca tại mốc.
    assert phan_loai(45.0) == "binh thuong"
    assert phan_loai(72.5) == "canh bao"
    assert phan_loai(85.0) == "nguy hiem"
    assert phan_loai(60.0) == "canh bao", "mốc dưới thuộc miền trên"
    assert phan_loai(80.0) == "nguy hiem"
    assert phan_loai(100.0) == "dung may"

    # Tham số mặc định cho phép đổi ngưỡng mà không sửa hàm.
    assert phan_loai(55.0, nguong_canh_bao=50.0) == "canh bao"

    # Hàm la_so_do_loi: giá trị kết thúc **không** phải lỗi.
    assert la_so_do_loi(-5.0) is True
    assert la_so_do_loi(KET_THUC) is False
    assert la_so_do_loi(0.0) is False

    # Hàm trung_binh: ca dãy rỗng trả về None, không chia cho 0.
    assert trung_binh(202.5, 3) == 67.5
    assert trung_binh(0.0, 0) is None

    # --- Kết quả cả chương trình trùng bản Chương 3 -------------
    assert (BT, CB, NH, DM, SL) == (1, 1, 1, 1, 1)
    assert TONG == 322.5, TONG
    assert abs(trung_binh(TONG, SO_HOP_LE) - 80.625) < 1e-9

    print()
    print("Moi khang dinh dat.")
