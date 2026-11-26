# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.5
Chương, mục : Chương 2, Mục 2.2.2
Đề bài      : Một dây chuyền vận hành tong_gio giờ liên tục,
              chia thành các ca do_dai_ca giờ. Tính số ca đầy và
              số giờ dư, rồi in dòng kiểm tra xác nhận quan hệ
              giữa ba đại lượng.
Đầu vào     : hai số nguyên, đơn vị giờ, miền từ 1 đến 168
Đầu ra      : số ca đầy, số giờ dư, và một dòng kiểm tra
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

MIEN_GIO = (1, 168)


def chia_ca(tong_gio, do_dai_ca):
    """Trả về (so_ca_day, gio_du).

    Phát sinh ValueError khi một đầu vào nằm ngoài miền, và
    ZeroDivisionError không bao giờ xảy ra vì miền bắt đầu từ 1.
    """
    for gia_tri, ten in ((tong_gio, "tong_gio"),
                         (do_dai_ca, "do_dai_ca")):
        if not MIEN_GIO[0] <= gia_tri <= MIEN_GIO[1]:
            raise ValueError(
                f"du lieu khong hop le: {ten} = {gia_tri}")
    return tong_gio // do_dai_ca, tong_gio % do_dai_ca


def dong_kiem_tra(tong_gio, do_dai_ca):
    """Dòng xác nhận quan hệ so_ca * do_dai + du == tong_gio."""
    so_ca_day, gio_du = chia_ca(tong_gio, do_dai_ca)
    tinh_lai = so_ca_day * do_dai_ca + gio_du
    return f"{so_ca_day} x {do_dai_ca} + {gio_du} = {tinh_lai}"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert chia_ca(24, 7) == (3, 3)
    assert dong_kiem_tra(24, 7) == "3 x 7 + 3 = 24"
    assert chia_ca(40, 8) == (5, 0)

    # --- Trường hợp biên ---------------------------------------
    # Chia hết thì phần dư bằng 0.
    assert chia_ca(21, 7) == (3, 0)
    # Độ dài ca lớn hơn tổng giờ: không ca nào đầy, dư tất cả.
    assert chia_ca(5, 7) == (0, 5)
    # Độ dài ca bằng đúng tổng giờ: một ca đầy, không dư.
    assert chia_ca(7, 7) == (1, 0)
    # Quan hệ giữa ba đại lượng đúng với mọi cặp trong miền.
    for tong in (1, 24, 100, 168):
        for do_dai in (1, 7, 8, 168):
            so_ca, du = chia_ca(tong, do_dai)
            assert so_ca * do_dai + du == tong, (tong, do_dai)
            assert 0 <= du < do_dai, (tong, do_dai)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Độ dài ca bằng 0 nằm ngoài miền nên bị chặn trước khi chia,
    # đúng nguyên tắc kiểm trước khi tính của Mục 1.1.1.
    da_chan = False
    try:
        chia_ca(24, 0)
    except ValueError as loi:
        da_chan = "do_dai_ca" in str(loi)
    assert da_chan, "do dai ca bang 0 ma van chia duoc"
    # Không kiểm trước thì phép chia nguyên ném ZeroDivisionError.
    da_chan_2 = False
    try:
        24 // 0
    except ZeroDivisionError:
        da_chan_2 = True
    assert da_chan_2, "chia nguyen cho 0 ma van chay"

    print("BT 2.5")
    for tong, do_dai in ((24, 7), (21, 7), (5, 7)):
        so_ca, du = chia_ca(tong, do_dai)
        print(f"  {tong} gio, ca {do_dai} gio -> {so_ca} ca day, "
              f"du {du} gio | {dong_kiem_tra(tong, do_dai)}")
