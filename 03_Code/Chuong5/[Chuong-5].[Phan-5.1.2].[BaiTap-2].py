# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.2
Chương, mục : Chương 5, Mục 5.1.2
Đề bài      : Chỉ ra bộ dữ liệu làm đoạn mã khởi tạo biến cực
              đại bằng 0 cho kết quả sai; nối với Bài tập 1.8.
Đầu vào     : không có, ba bộ dữ liệu cố định trong mã
Đầu ra      : hai kết quả cho từng bộ dữ liệu
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

CO_DUONG_VA_AM = [45.0, -5.0, 72.5, -12.0, 38.0]
TOAN_SO_AM = [-5.0, -12.0, -3.0]
RONG = []


def cuc_dai_sai(day):
    """Bản SAI của đề bài: khởi tạo biến cực đại bằng 0."""
    lon_nhat = 0.0
    for gia_tri in day:
        if gia_tri > lon_nhat:
            lon_nhat = gia_tri
    return lon_nhat


def cuc_dai_dung(day):
    """Bản đúng: khởi tạo bằng phần tử đầu của danh sách.

    Phát sinh ValueError khi danh sách rỗng, vì danh sách rỗng
    không có cực đại.
    """
    if len(day) == 0:
        raise ValueError("du lieu khong hop le: danh sach rong")
    lon_nhat = day[0]
    for gia_tri in day:
        if gia_tri > lon_nhat:
            lon_nhat = gia_tri
    return lon_nhat


def lo_ra(day):
    """Lỗi có lộ ra với bộ dữ liệu này hay không."""
    try:
        return cuc_dai_sai(day) != cuc_dai_dung(day)
    except ValueError:
        return True


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Chuoi co ca so duong lan so am: hai ban cho CUNG ket qua,
    # nen loi KHONG lo ra.
    assert cuc_dai_sai(CO_DUONG_VA_AM) == 72.5
    assert cuc_dai_dung(CO_DUONG_VA_AM) == 72.5
    assert lo_ra(CO_DUONG_VA_AM) is False
    # Ban dung trung ham max co san tren moi bo du lieu khong rong.
    assert cuc_dai_dung(CO_DUONG_VA_AM) == max(CO_DUONG_VA_AM)

    # --- Trường hợp biên ---------------------------------------
    # Chuoi toan so am: day la bo du lieu phai chon.
    assert cuc_dai_sai(TOAN_SO_AM) == 0.0
    assert cuc_dai_dung(TOAN_SO_AM) == -3.0
    assert cuc_dai_dung(TOAN_SO_AM) == max(TOAN_SO_AM)
    assert lo_ra(TOAN_SO_AM) is True
    # Khong phan tu nao cua chuoi bang 0, nen ket qua 0 la vo ly.
    for gia_tri in TOAN_SO_AM:
        assert gia_tri != 0.0
    # Mot phan tu am duy nhat cung lo ra loi.
    assert cuc_dai_sai([-5.0]) == 0.0
    assert cuc_dai_dung([-5.0]) == -5.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Danh sach rong: ban sai cho 0 ma khong bao gi, ban dung bao
    # loi, tuc ban dung AN TOAN HON.
    assert cuc_dai_sai(RONG) == 0.0
    da_chan = False
    try:
        cuc_dai_dung(RONG)
    except ValueError:
        da_chan = True
    assert da_chan, "danh sach rong ma van tinh duoc cuc dai"
    # Ham max co san cung bao loi voi danh sach rong.
    da_chan2 = False
    try:
        max(RONG)
    except ValueError:
        da_chan2 = True
    assert da_chan2, "max cua danh sach rong ma chay"

    ten_bo = ("co duong va am", "toan so am", "rong")
    cac_bo = (CO_DUONG_VA_AM, TOAN_SO_AM, RONG)
    for thu_tu in range(3):
        day = cac_bo[thu_tu]
        sai = cuc_dai_sai(day)
        try:
            dung = f"{cuc_dai_dung(day)}"
        except ValueError as loi:
            dung = f"ValueError: {loi}"
        print(f"{ten_bo[thu_tu]:<16}sai {sai:<8} dung {dung}")
    print(f"bo du lieu lam loi lo ra: toan so am")
