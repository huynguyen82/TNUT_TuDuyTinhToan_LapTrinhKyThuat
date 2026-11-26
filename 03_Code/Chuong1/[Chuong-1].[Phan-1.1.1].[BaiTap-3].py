# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.3
Chương, mục : Chương 1, Mục 1.1.1
Đề bài      : Lập bảng đặc tả ba phần cho bài toán tính tổn thất
              công suất trên một đoạn đường dây tải điện, theo
              công thức tổn thất bằng bình phương dòng điện nhân
              điện trở một kilômét nhân chiều dài.
Đầu vào     : dòng điện (A), điện trở một kilômét (Ω/km), chiều
              dài đoạn dây (km)
Đầu ra      : tổn thất công suất (W), hai chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên.
"""

MIEN_DONG_DIEN = (0.0, 1000.0)
MIEN_DIEN_TRO = (0.01, 5.00)
MIEN_CHIEU_DAI = (0.0, 100.0)
SO_CHU_SO_THAP_PHAN = 2


def trong_mien(gia_tri, mien):
    """Giá trị có nằm trong miền đóng đã khai báo hay không."""
    can_duoi, can_tren = mien
    return can_duoi <= gia_tri <= can_tren


def kiem_dau_vao(dong_dien, dien_tro, chieu_dai):
    """Kiểm ba đầu vào theo miền giá trị của bảng đặc tả.

    Phát sinh ValueError kèm tên đại lượng sai, theo đúng ô
    `ngoài miền thì báo dữ liệu không hợp lệ` của bảng đặc tả.
    """
    cac_kiem = (
        ("dong_dien", dong_dien, MIEN_DONG_DIEN),
        ("dien_tro", dien_tro, MIEN_DIEN_TRO),
        ("chieu_dai", chieu_dai, MIEN_CHIEU_DAI),
    )
    for ten, gia_tri, mien in cac_kiem:
        if not trong_mien(gia_tri, mien):
            raise ValueError(
                f"du lieu khong hop le: {ten} = {gia_tri}, "
                f"mien cho phep {mien}"
            )


def ton_that_cong_suat(dong_dien, dien_tro, chieu_dai):
    """Tổn thất công suất trên đoạn dây, W.

    Bước 1 của bảng đặc tả kiểm ba đầu vào; bước 2 tính tổn
    thất. Thứ tự này bắt buộc: kiểm trước khi tính.
    """
    kiem_dau_vao(dong_dien, dien_tro, chieu_dai)
    return dong_dien ** 2 * dien_tro * chieu_dai


def dinh_dang(ton_that):
    """Trình bày tổn thất theo đúng định dạng của đầu ra."""
    return f"{ton_that:.{SO_CHU_SO_THAP_PHAN}f}"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert ton_that_cong_suat(50.0, 0.25, 1.2) == 750.0
    assert dinh_dang(ton_that_cong_suat(50.0, 0.25, 1.2)) == "750.00"
    # Tổn thất tỉ lệ với bình phương dòng điện: dòng tăng gấp đôi
    # thì tổn thất tăng gấp bốn.
    assert (ton_that_cong_suat(100.0, 0.25, 1.2)
            == 4 * ton_that_cong_suat(50.0, 0.25, 1.2))
    # Tổn thất tỉ lệ bậc nhất với chiều dài.
    assert (ton_that_cong_suat(50.0, 0.25, 2.4)
            == 2 * ton_that_cong_suat(50.0, 0.25, 1.2))

    # --- Trường hợp biên ---------------------------------------
    # Chiều dài bằng 0 cho tổn thất bằng 0.
    assert ton_that_cong_suat(50.0, 0.25, 0.0) == 0.0
    assert dinh_dang(ton_that_cong_suat(50.0, 0.25, 0.0)) == "0.00"
    # Dòng điện bằng 0 cũng cho tổn thất bằng 0.
    assert ton_that_cong_suat(0.0, 0.25, 1.2) == 0.0
    # Ba cận trên của miền đều hợp lệ.
    assert trong_mien(1000.0, MIEN_DONG_DIEN)
    assert trong_mien(5.00, MIEN_DIEN_TRO)
    assert trong_mien(100.0, MIEN_CHIEU_DAI)
    # Cận dưới của điện trở là 0,01 chứ không phải 0.
    assert trong_mien(0.01, MIEN_DIEN_TRO)
    assert not trong_mien(0.0, MIEN_DIEN_TRO)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dòng điện âm nằm ngoài miền, phải báo dữ liệu không hợp lệ.
    da_chan = False
    try:
        ton_that_cong_suat(-10.0, 0.25, 1.2)
    except ValueError as loi:
        da_chan = "dong_dien" in str(loi)
    assert da_chan, "dong dien am ma van tinh duoc"
    # Chiều dài vượt cận trên cũng bị chặn.
    da_chan_2 = False
    try:
        ton_that_cong_suat(50.0, 0.25, 101.0)
    except ValueError as loi:
        da_chan_2 = "chieu_dai" in str(loi)
    assert da_chan_2, "chieu dai vuot mien ma van tinh duoc"

    print("BT 1.3")
    for i, r, l in ((50.0, 0.25, 1.2), (50.0, 0.25, 0.0)):
        print(f"  I={i} A, R={r} Ohm/km, L={l} km -> "
              f"{dinh_dang(ton_that_cong_suat(i, r, l))} W")
