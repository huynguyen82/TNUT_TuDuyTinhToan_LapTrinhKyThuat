# -*- coding: utf-8 -*-
"""
Mã bài      : GL 3
Chương, mục : Chương 3, Bài gỡ lỗi GL3
Đề bài      : Chương trình 28 dòng đếm số lần của ba trạng thái
              nhiệt độ chứa đúng ba lỗi: một cú pháp, một thực thi,
              một logic. Tìm ba lỗi, nêu loại, sửa, kiểm lại.
Đầu vào     : số lượng số đo và dãy số đo nhiệt độ, đơn vị độ C
Đầu ra      : ba số đếm trạng thái, số đo lỗi, và nhiệt độ trung
              bình của các số đo hợp lệ
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

NGUONG_CANH_BAO = 60.0
NGUONG_NGUY_HIEM = 80.0

BA_LOI = (
    (21, "cu phap", "if so_do < NGUONG_CANH_BAO khong co dau hai cham",
     "SyntaxError: expected ':'",
     "them dau hai cham cuoi dong mo khoi"),
    (28, "thuc thi", "tong / (so_luong - dem_loi) khong kiem mau so",
     "ZeroDivisionError: float division by zero khi moi so do deu loi",
     "kiem so do hop le lon hon 0 truoc phep chia"),
    (12, "logic", "for chi_so in range(1, so_luong)",
     "khong bao gi; doc thieu dung mot so do, va voi so_luong = 1 "
     "thi doc 0 so do",
     "dung range(so_luong), vi can so_luong luot"),
)


def dem_trang_thai(cac_so_do, loi_dong_12=False):
    """Tra ve (dem binh thuong, canh bao, nguy hiem, loi, trung binh).

    Phat sinh ValueError khi khong con so do hop le nao, dung nhu
    loi thuc thi o dong 28 sau khi da duoc chan lai.
    """
    if loi_dong_12:
        # Bản lỗi: bỏ phần tử đầu, đúng như range(1, so_luong).
        cac_so_do = cac_so_do[1:]
    binh_thuong = canh_bao = nguy_hiem = loi = 0
    tong = 0.0
    for so_do in cac_so_do:
        if so_do < 0:
            loi = loi + 1
            continue
        tong = tong + so_do
        if so_do < NGUONG_CANH_BAO:
            binh_thuong = binh_thuong + 1
        elif so_do < NGUONG_NGUY_HIEM:
            canh_bao = canh_bao + 1
        else:
            nguy_hiem = nguy_hiem + 1
    hop_le = binh_thuong + canh_bao + nguy_hiem
    if hop_le == 0:
        raise ValueError("khong co so do hop le nao de tinh trung binh")
    return binh_thuong, canh_bao, nguy_hiem, loi, tong / hop_le


BO_THUONG = (45.0, 72.5, 85.0)


def in_ket_qua():
    """In bang ba loi va ket qua hai ban tren ba bo du lieu."""
    print("Dong | Loai     | Bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    dung = dem_trang_thai(BO_THUONG)
    sai = dem_trang_thai(BO_THUONG, loi_dong_12=True)
    print(f"Bo thuong 45 | 72,5 | 85 do C")
    print(f"  Ban da sua : {dung[0]} binh thuong, {dung[1]} canh bao, "
          f"{dung[2]} nguy hiem, trung binh {dung[4]:.1f} do C")
    print(f"  Ban con loi: {sai[0]} binh thuong, {sai[1]} canh bao, "
          f"{sai[2]} nguy hiem, trung binh {sai[4]:.2f} do C")


if __name__ == "__main__":
    in_ket_qua()

    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    # Ca thường: 1 bình thường, 1 cảnh báo, 1 nguy hiểm, 67,5 độ C.
    _d = dem_trang_thai(BO_THUONG)
    assert _d[:4] == (1, 1, 1, 0), "ba trang thai moi loai mot lan"
    assert abs(_d[4] - 67.5) < 1e-9, "trung binh phai 67,5 do C"

    # Ca biên: một số đo duy nhất. Bản lỗi dòng 12 đọc **0** số đo
    # nên nó không tính được trung bình — ca bộc lộ lỗi rõ nhất.
    assert dem_trang_thai((45.0,))[:4] == (1, 0, 0, 0), \
        "mot so do 45 phai cho mot binh thuong"
    _da_no = False
    try:
        dem_trang_thai((45.0,), loi_dong_12=True)
    except ValueError:
        _da_no = True
    assert _da_no, "ban loi doc 0 so do nen khong tinh duoc"

    # Ca không hợp lệ: hai số đo đều âm, không còn số đo hợp lệ.
    _da_chan = False
    try:
        dem_trang_thai((-5.0, -2.0))
    except ValueError:
        _da_chan = True
    assert _da_chan, "moi so do loi thi phai chan truoc phep chia"

    print()
    print("Moi khang dinh dat.")
