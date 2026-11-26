# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.7
Chương, mục : Chương 4, Mục 4.2.1
Đề bài      : Tách chương trình kiểm dung sai của Bài tập 3.5
              thành bộ bốn hàm, mỗi hàm kiểm riêng được.
Đầu vào     : số chi tiết (1 đến 100) và các kích thước đo
Đầu ra      : số chi tiết đạt và kích thước trung bình
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Số liệu dung sai là giả
định của đề bài, lấy từ Bài tập 2.9 và Bài tập 3.5.
"""

KICH_THUOC_DANH_NGHIA = 50.00
DUNG_SAI = 0.05
MIEN_SO_CHI_TIET = (1, 100)


def doc_kich_thuoc(chuoi_vao):
    """Hàm 1: chuyển một kích thước đo từ chuỗi sang số thực.

    Phát sinh ValueError khi chuỗi không phải một số thực.
    """
    return float(chuoi_vao)


def dat_dung_sai(kich_thuoc):
    """Hàm 2: kích thước có nằm trong dung sai hay không."""
    return abs(kich_thuoc - KICH_THUOC_DANH_NGHIA) <= DUNG_SAI


def kich_thuoc_trung_binh(tong, so_chi_tiet):
    """Hàm 3: kích thước trung bình, mm.

    Phát sinh ValueError khi số chi tiết ngoài miền từ 1 đến
    100, để phép chia không bao giờ gặp số 0.
    """
    if not (MIEN_SO_CHI_TIET[0] <= so_chi_tiet
            <= MIEN_SO_CHI_TIET[1]):
        raise ValueError(
            f"du lieu khong hop le: so chi tiet = {so_chi_tiet}")
    return tong / so_chi_tiet


def gom_ket_qua(so_chi_tiet, doc_mot_dong):
    """Hàm 4: gom ba hàm trên thành kết quả của cả bài.

    Tham số doc_mot_dong là hàm cấp một kích thước cho mỗi lượt,
    nên hàm này kiểm được không cần bàn phím.
    """
    so_dat = 0
    tong = 0.0
    for thu_tu in range(so_chi_tiet):
        kich_thuoc = doc_kich_thuoc(doc_mot_dong(thu_tu))
        tong = tong + kich_thuoc
        if dat_dung_sai(kich_thuoc):
            so_dat = so_dat + 1
    return so_dat, kich_thuoc_trung_binh(tong, so_chi_tiet)


def nguon_ba_kich_thuoc(thu_tu):
    """Nguồn dữ liệu kiểm thử: ba kích thước của Bài tập 3.5."""
    return ("50.03", "49.97", "50.01")[thu_tu]


def nguon_mot_kich_thuoc(thu_tu):
    """Nguồn dữ liệu kiểm thử: một kích thước duy nhất."""
    return ("50.05",)[thu_tu]


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Dap so trung Bai tap 3.5 tren cung bo du lieu.
    so_dat, trung_binh = gom_ket_qua(3, nguon_ba_kich_thuoc)
    assert so_dat == 3
    assert f"{trung_binh:.2f}" == "50.00"
    # Bon ham kiem rieng duoc, moi ham mot bo du lieu nho.
    assert doc_kich_thuoc("50.03") == 50.03
    assert dat_dung_sai(50.03) is True
    assert kich_thuoc_trung_binh(150.01, 3) == 150.01 / 3

    # --- Trường hợp biên ---------------------------------------
    # Mot chi tiet: ham tinh trung binh phai chay dung voi n = 1.
    so_dat1, trung_binh1 = gom_ket_qua(1, nguon_mot_kich_thuoc)
    assert so_dat1 == 1
    assert f"{trung_binh1:.2f}" == "50.05"
    assert kich_thuoc_trung_binh(50.05, 1) == 50.05
    # Kich thuoc dung bang hai can cua dung sai van dat.
    assert dat_dung_sai(50.05) is True
    assert dat_dung_sai(49.95) is True
    # Nhich qua can thi khong dat.
    assert dat_dung_sai(50.06) is False
    assert dat_dung_sai(49.94) is False
    # Can tren cua mien so chi tiet van hop le.
    assert kich_thuoc_trung_binh(5000.0, 100) == 50.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # 0 chi tiet: ham tinh trung binh chan truoc khi chia.
    da_chan = False
    try:
        kich_thuoc_trung_binh(0.0, 0)
    except ValueError:
        da_chan = True
    assert da_chan, "0 chi tiet ma van chia duoc"
    # Chuoi khong phai so: ham doc kich thuoc chan.
    da_chan2 = False
    try:
        doc_kich_thuoc("50,03")
    except ValueError:
        da_chan2 = True
    assert da_chan2, "chuoi dung dau phay ma van chuyen duoc"
    # Hai loi tren thuoc hai ham khac nhau, nen khoanh vung duoc.

    print(f"So chi tiet dat : {so_dat}")
    print(f"Trung binh      : {trung_binh:.2f} mm")
    print(f"Mot chi tiet    : {so_dat1} dat, "
          f"{trung_binh1:.2f} mm")
