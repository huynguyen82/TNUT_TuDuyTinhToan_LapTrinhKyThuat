# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.9
Chương, mục : Chương 4, cả năm tiểu mục
Đề bài      : Chương trình tư vấn khoản vay thiết bị: số tháng
              trả hết, tổng lãi cộng dồn, và giá trị hiện tại
              của khoản trả tháng cuối.
Đầu vào     : tiền vay, lãi suất tháng, tiền trả tháng
Đầu ra      : số tháng; tổng lãi và giá trị hiện tại, hai chữ
              số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Số liệu khoản vay là giả
định của đề bài.
"""

MIEN_TIEN_VAY = (1_000.0, 10_000_000.0)
MIEN_LAI_SUAT = (0.0, 0.05)


def kiem_du_lieu_vao(tien_vay, lai_suat, tien_tra):
    """Hàm 1: chặn mọi dữ liệu vào không hợp lệ.

    Phát sinh ValueError khi tiền vay hoặc lãi suất ngoài miền,
    khi tiền trả không dương, hoặc khi tiền trả không đủ bù lãi
    tháng đầu, vì khi ấy nợ không bao giờ hết.
    """
    if not MIEN_TIEN_VAY[0] <= tien_vay <= MIEN_TIEN_VAY[1]:
        raise ValueError(
            f"du lieu khong hop le: tien vay = {tien_vay}")
    if not MIEN_LAI_SUAT[0] <= lai_suat <= MIEN_LAI_SUAT[1]:
        raise ValueError(
            f"du lieu khong hop le: lai suat = {lai_suat}")
    if tien_tra <= 0.0 or tien_tra > tien_vay:
        raise ValueError(
            f"du lieu khong hop le: tien tra = {tien_tra}")
    if tien_tra <= tien_vay * lai_suat:
        raise ValueError(
            "du lieu khong hop le: tien tra khong du bu lai "
            f"thang dau = {tien_vay * lai_suat}")
    return True


def so_du_sau_mot_thang(so_du, lai_suat, tien_tra):
    """Hàm 2: số dư sau một tháng trả nợ, nghìn đồng."""
    return so_du * (1 + lai_suat) - tien_tra


def ky_han_va_tong_lai(tien_vay, lai_suat, tien_tra):
    """Hàm 3: số tháng trả hết nợ và tổng lãi cộng dồn.

    Trả về hai giá trị: số tháng kiểu số nguyên, và tổng lãi
    kiểu số thực, đơn vị nghìn đồng.
    """
    kiem_du_lieu_vao(tien_vay, lai_suat, tien_tra)
    so_du = tien_vay
    so_thang = 0
    tong_lai = 0.0
    while so_du > 0.0:
        tong_lai = tong_lai + so_du * lai_suat
        so_du = so_du_sau_mot_thang(so_du, lai_suat, tien_tra)
        so_thang = so_thang + 1
    return so_thang, tong_lai


def gia_tri_hien_tai(gia_tri_tuong_lai, so_ky,
                     lai_suat=0.008):
    """Hàm 4: giá trị hiện tại của một dòng tiền tương lai."""
    if so_ky < 0:
        raise ValueError(f"du lieu khong hop le: so ky = {so_ky}")
    return gia_tri_tuong_lai / (1 + lai_suat) ** so_ky


def tien_tra_thang_cuoi(tien_vay, lai_suat, tien_tra):
    """Hàm 5: khoản phải trả ở tháng cuối, nghìn đồng.

    Tháng cuối chỉ phải trả phần nợ còn lại, nên nhỏ hơn hoặc
    bằng tiền trả hằng tháng.
    """
    kiem_du_lieu_vao(tien_vay, lai_suat, tien_tra)
    so_du = tien_vay
    truoc_do = so_du
    while so_du > 0.0:
        truoc_do = so_du
        so_du = so_du_sau_mot_thang(so_du, lai_suat, tien_tra)
    return truoc_do * (1 + lai_suat)


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    so_thang, tong_lai = ky_han_va_tong_lai(
        500000.0, 0.008, 25000.0)
    assert so_thang == 22
    assert f"{tong_lai:.2f}" == "47041.27"
    cuoi = tien_tra_thang_cuoi(500000.0, 0.008, 25000.0)
    assert f"{cuoi:.2f}" == "22041.27"
    # Thang cuoi tra it hon hoac bang tien tra hang thang.
    assert cuoi <= 25000.0

    # --- Trường hợp biên ---------------------------------------
    # Lai suat 0: so thang bang tien vay chia tien tra, lam tron len.
    so_thang0, tong_lai0 = ky_han_va_tong_lai(
        500000.0, 0.0, 25000.0)
    assert so_thang0 == 20
    assert f"{tong_lai0:.2f}" == "0.00"
    # Lai suat 0 thi thang cuoi tra dung tien tra hang thang.
    assert tien_tra_thang_cuoi(500000.0, 0.0, 25000.0) == 25000.0
    # Tra het trong dung mot thang.
    assert ky_han_va_tong_lai(1000.0, 0.0, 1000.0)[0] == 1
    # So ky bang 0: gia tri hien tai bang gia tri tuong lai.
    assert gia_tri_hien_tai(100000.0, 0) == 100000.0
    # Lai suat cao hon lam ky han dai hon va tong lai lon hon.
    dai, lai_nhieu = ky_han_va_tong_lai(500000.0, 0.015, 25000.0)
    assert dai > so_thang
    assert lai_nhieu > tong_lai

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tien tra khong du bu lai thang dau: lai thang dau 4 000
    # nghin dong, lon hon tien tra 1 000 nghin dong.
    da_chan = 0
    for thu_tu in range(4):
        bo = ((500000.0, 0.008, 1000.0), (500.0, 0.008, 100.0),
              (500000.0, 0.5, 25000.0),
              (500000.0, 0.008, 600000.0))[thu_tu]
        try:
            ky_han_va_tong_lai(bo[0], bo[1], bo[2])
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 4, "co bo du lieu khong hop le ma khong chan"
    # So ky am bi chan o ham gia tri hien tai.
    da_chan2 = False
    try:
        gia_tri_hien_tai(100000.0, -3)
    except ValueError:
        da_chan2 = True
    assert da_chan2, "so ky am ma van tinh duoc"

    hien_tai = gia_tri_hien_tai(cuoi, so_thang, 0.008)
    print(f"So thang tra het      : {so_thang}")
    print(f"Tong lai cong don     : {tong_lai:.2f}")
    print(f"Tien tra thang cuoi   : {cuoi:.2f}")
    print(f"Gia tri hien tai thang cuoi: {hien_tai:.2f}")
