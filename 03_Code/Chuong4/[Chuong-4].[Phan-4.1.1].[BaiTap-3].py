# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.3
Chương, mục : Chương 4, Mục 4.1.1
Đề bài      : Viết hàm tính số dư sau một tháng trả nợ, có
              chuỗi tài liệu, rồi gọi ba lần cho ba tháng đầu.
Đầu vào     : số dư, lãi suất tháng, tiền trả tháng
Đầu ra      : ba số dư, hai chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Danh sách chưa được dạy
tới Chương 5, nên ba số dư trả về dưới dạng ba giá trị.
"""

MIEN_SO_DU = (0.0, 10_000_000.0)
MIEN_LAI_SUAT = (0.0, 0.05)


def so_du_sau_mot_thang(so_du, lai_suat, tien_tra):
    """Số dư sau một tháng trả nợ, nghìn đồng.

    Phát sinh ValueError khi số dư hoặc lãi suất ngoài miền,
    hoặc khi tiền trả không đủ bù lãi của tháng đó, vì khi ấy
    số dư tăng thay vì giảm.
    """
    if not MIEN_SO_DU[0] <= so_du <= MIEN_SO_DU[1]:
        raise ValueError(f"du lieu khong hop le: so du = {so_du}")
    if not MIEN_LAI_SUAT[0] <= lai_suat <= MIEN_LAI_SUAT[1]:
        raise ValueError(
            f"du lieu khong hop le: lai suat = {lai_suat}")
    if tien_tra <= so_du * lai_suat:
        raise ValueError(
            f"du lieu khong hop le: tien tra = {tien_tra}")
    return so_du * (1 + lai_suat) - tien_tra


def ba_thang_dau(so_du, lai_suat, tien_tra):
    """Ba số dư sau ba tháng đầu, gọi lại cùng một hàm."""
    thang_mot = so_du_sau_mot_thang(so_du, lai_suat, tien_tra)
    thang_hai = so_du_sau_mot_thang(thang_mot, lai_suat, tien_tra)
    thang_ba = so_du_sau_mot_thang(thang_hai, lai_suat, tien_tra)
    return thang_mot, thang_hai, thang_ba


def dinh_dang(gia_tri):
    """Một số dư đã định dạng hai chữ số thập phân."""
    return f"{gia_tri:.2f}"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_du_sau_mot_thang(500000.0, 0.008, 25000.0) == 479000.0
    mot, hai, ba = ba_thang_dau(500000.0, 0.008, 25000.0)
    assert dinh_dang(mot) == "479000.00"
    assert dinh_dang(hai) == "457832.00"
    assert dinh_dang(ba) == "436494.66"
    # Chuoi tai lieu cua ham ton tai va noi ro don vi.
    assert "nghìn đồng" in so_du_sau_mot_thang.__doc__

    # --- Trường hợp biên ---------------------------------------
    # Lai suat 0: so du giam dung tien tra moi thang.
    mot0, hai0, ba0 = ba_thang_dau(500000.0, 0.0, 25000.0)
    assert dinh_dang(mot0) == "475000.00"
    assert dinh_dang(hai0) == "450000.00"
    assert dinh_dang(ba0) == "425000.00"
    # Lai suat dung bang can tren cua mien van hop le.
    assert so_du_sau_mot_thang(1000.0, 0.05, 100.0) == 950.0
    # Tien tra lon hon so du: so du thanh am, da tra het.
    assert so_du_sau_mot_thang(1000.0, 0.0, 2000.0) == -1000.0

    # --- Trường hợp ngoại lệ -----------------------------------
    da_chan = 0
    for thu_tu in range(3):
        bo = ((500000.0, 0.008, 0.0), (-1.0, 0.008, 25000.0),
              (500000.0, 0.5, 25000.0))[thu_tu]
        try:
            so_du_sau_mot_thang(bo[0], bo[1], bo[2])
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 3, "co bo du lieu khong hop le ma khong chan"

    print(f"Thang 1: {dinh_dang(mot)}")
    print(f"Thang 2: {dinh_dang(hai)}")
    print(f"Thang 3: {dinh_dang(ba)}")
