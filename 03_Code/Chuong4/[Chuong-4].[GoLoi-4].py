# -*- coding: utf-8 -*-
"""
Mã bài      : GL 4
Chương, mục : Chương 4, Bài gỡ lỗi GL4
Đề bài      : Chương trình 22 dòng tính số tháng trả hết nợ và tổng
              lãi đã trả chứa đúng ba lỗi: một cú pháp, một thực
              thi, một logic. Tìm ba lỗi, nêu loại, sửa, kiểm lại.
Đầu vào     : tiền vay, đơn vị nghìn đồng
Đầu ra      : số tháng trả hết và tổng lãi đã trả
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

LAI_SUAT = 0.008
TIEN_TRA = 25000.0
SO_THANG_TOI_DA = 600

BA_LOI = (
    (4, "cu phap",
     "def so_du_sau_mot_thang(so_du, lai_suat, tien_tra) "
     "khong co dau hai cham",
     "SyntaxError: expected ':'",
     "them dau hai cham cuoi dong def"),
    (18, "thuc thi",
     "goi so_du_sau_mot_thang(so_du, LAI_SUAT) thieu doi so thu ba",
     "TypeError: so_du_sau_mot_thang() missing 1 required "
     "positional argument: 'tien_tra'",
     "truyen du ba doi so: them TIEN_TRA"),
    (11, "logic",
     "tong_lai tinh lai tren tien vay goc suot ca ky han",
     "khong bao gi; cho 88 000 thay vi 47 041,27 nghin dong",
     "cong don lai that cua tung thang trong chinh vong lap"),
)


def so_du_sau_mot_thang(so_du, lai_suat, tien_tra):
    """So du sau mot thang tra no, nghin dong."""
    return so_du * (1 + lai_suat) - tien_tra


def tra_no(tien_vay):
    """Tra ve (so thang tra het, tong lai da tra).

    Phat sinh ValueError khi tien tra moi thang khong du bu lai
    thang dau, vi khi do no khong bao gio het.
    """
    lai_thang_dau = tien_vay * LAI_SUAT
    if lai_thang_dau >= TIEN_TRA:
        raise ValueError(
            f"lai thang dau {lai_thang_dau:.2f} khong nho hon "
            f"tien tra {TIEN_TRA:.2f}; no khong bao gio het")
    so_du = tien_vay
    so_thang = 0
    tong_lai = 0.0
    while so_du > 0 and so_thang < SO_THANG_TOI_DA:
        tong_lai = tong_lai + so_du * LAI_SUAT
        so_du = so_du_sau_mot_thang(so_du, LAI_SUAT, TIEN_TRA)
        so_thang = so_thang + 1
    return so_thang, tong_lai


def tong_lai_ban_loi(tien_vay, so_thang):
    """Ban loi dong 11: lai tren tien vay goc suot ca ky han."""
    return tien_vay * LAI_SUAT * so_thang


def in_ket_qua():
    """In bang ba loi va ket qua ba bo du lieu."""
    print("Dong | Loai     | Bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    for tien_vay in (500000.0, 24000.0):
        so_thang, tong_lai = tra_no(tien_vay)
        sai = tong_lai_ban_loi(tien_vay, so_thang)
        print(f"Vay {tien_vay:>9.0f}: {so_thang:>2} thang, "
              f"tong lai dung {tong_lai:>9.2f}, "
              f"ban con loi {sai:>9.2f}")


if __name__ == "__main__":
    in_ket_qua()

    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    # Ca thường: vay 500 000 thì 22 tháng, tổng lãi 47 041,27.
    _thang, _lai = tra_no(500000.0)
    assert _thang == 22, f"phai la 22 thang, nhan duoc {_thang}"
    assert abs(_lai - 47041.27) < 0.01, \
        f"tong lai phai 47041,27, nhan duoc {_lai:.2f}"

    # Bản lỗi dòng 11 cho 88 000 — sai gần gấp đôi mà không báo gì.
    assert abs(tong_lai_ban_loi(500000.0, 22) - 88000.0) < 0.01, \
        "ban loi phai cho 88 000"

    # Ca biên: vay 24 000 trả hết sau đúng 1 tháng, lãi 192,00.
    _thang_b, _lai_b = tra_no(24000.0)
    assert _thang_b == 1, "ca bien phai la 1 thang"
    assert abs(_lai_b - 192.0) < 0.01, "ca bien phai cho lai 192,00"

    # Ca không hợp lệ: vay 5 000 000 thì lãi tháng đầu 40 000 lớn
    # hơn tiền trả 25 000, nên phải chặn trước vòng lặp.
    _da_chan = False
    try:
        tra_no(5000000.0)
    except ValueError:
        _da_chan = True
    assert _da_chan, "no khong bao gio het thi phai chan truoc"

    print()
    print("Moi khang dinh dat.")
