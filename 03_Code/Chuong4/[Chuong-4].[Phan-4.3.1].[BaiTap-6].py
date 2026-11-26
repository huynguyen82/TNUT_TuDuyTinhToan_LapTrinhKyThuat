# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.6
Chương, mục : Chương 4, Mục 4.3.1
Đề bài      : Viết bộ ca kiểm thử bằng assert cho hàm tra tiết
              diện dây, rồi sửa cố ý một mốc để xác nhận bộ ca
              phát hiện được.
Đầu vào     : không có, mọi số liệu cố định trong mã
Đầu ra      : ca nào bắt được lỗi cố ý
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

MIEN_DONG = (0.0, 1000.0)
VUOT_BANG_TRA = -1.0


def tiet_dien(dong_dien):
    """Bản ĐÚNG: tiết diện dây nhỏ nhất đủ chịu dòng, mm²."""
    if not MIEN_DONG[0] <= dong_dien <= MIEN_DONG[1]:
        raise ValueError(
            f"du lieu khong hop le: dong dien = {dong_dien}")
    if dong_dien <= 16.0:
        return 1.5
    elif dong_dien <= 25.0:
        return 2.5
    elif dong_dien <= 32.0:
        return 4.0
    elif dong_dien <= 40.0:
        return 6.0
    elif dong_dien <= 63.0:
        return 10.0
    return VUOT_BANG_TRA


def tiet_dien_sua_coi_y(dong_dien):
    """Bản SAI cố ý: mốc thứ ba viết 33,0 thay vì 32,0."""
    if not MIEN_DONG[0] <= dong_dien <= MIEN_DONG[1]:
        raise ValueError(
            f"du lieu khong hop le: dong dien = {dong_dien}")
    if dong_dien <= 16.0:
        return 1.5
    elif dong_dien <= 25.0:
        return 2.5
    elif dong_dien <= 33.0:
        return 4.0
    elif dong_dien <= 40.0:
        return 6.0
    elif dong_dien <= 63.0:
        return 10.0
    return VUOT_BANG_TRA


def ca_thuong_dat(ham):
    """Nhóm ca thường có đạt với hàm đã cho hay không."""
    return (ham(30.0) == 4.0 and ham(20.0) == 2.5
            and ham(50.0) == 10.0)


def ca_tai_moc_dat(ham):
    """Nhóm biên thứ nhất: đúng tại năm mốc của bảng tra."""
    return (ham(16.0) == 1.5 and ham(25.0) == 2.5
            and ham(32.0) == 4.0 and ham(40.0) == 6.0
            and ham(63.0) == 10.0)


def ca_nhich_qua_moc_dat(ham):
    """Nhóm biên thứ hai: nhích qua từng mốc một phần mười."""
    return (ham(16.1) == 2.5 and ham(25.1) == 4.0
            and ham(32.1) == 6.0 and ham(40.1) == 10.0
            and ham(63.1) == VUOT_BANG_TRA)


def ca_ngoai_le_dat(ham):
    """Nhóm ca ngoại lệ: dòng điện âm phải phát sinh lỗi."""
    try:
        ham(-1.0)
    except ValueError:
        return True
    return False


def ca_bat_duoc_loi(ham_sai):
    """Tên nhóm ca đầu tiên không đạt với bản sai cố ý."""
    if not ca_thuong_dat(ham_sai):
        return "thuong"
    if not ca_tai_moc_dat(ham_sai):
        return "bien tai moc"
    if not ca_nhich_qua_moc_dat(ham_sai):
        return "bien nhich qua moc"
    if not ca_ngoai_le_dat(ham_sai):
        return "ngoai le"
    return "khong nhom nao"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Ba nhom ca deu dat voi ban dung.
    assert ca_thuong_dat(tiet_dien) is True
    assert ca_tai_moc_dat(tiet_dien) is True
    assert ca_nhich_qua_moc_dat(tiet_dien) is True
    assert ca_ngoai_le_dat(tiet_dien) is True

    # --- Trường hợp biên ---------------------------------------
    # Ban sai coi y day moc thu ba tu 32,0 ra 33,0.
    # Nhom thuong KHONG bat duoc: 30,0 va 20,0 va 50,0 khong roi
    # vao khoang tu 32,0 den 33,0.
    assert ca_thuong_dat(tiet_dien_sua_coi_y) is True
    # Nhom ca DUNG TAI nam moc cung KHONG bat duoc, vi moc bi day
    # ra ngoai nen 32,0 van thuoc nhanh 4,0 mm2 o ca hai ban.
    assert ca_tai_moc_dat(tiet_dien_sua_coi_y) is True
    # Chi nhom nhich qua moc bat duoc.
    assert ca_nhich_qua_moc_dat(tiet_dien_sua_coi_y) is False
    assert ca_bat_duoc_loi(
        tiet_dien_sua_coi_y) == "bien nhich qua moc"
    # Moi so do trong khoang tu 32,1 den 33,0 deu phan biet hai ban.
    assert tiet_dien(32.1) == 6.0
    assert tiet_dien_sua_coi_y(32.1) == 4.0
    assert tiet_dien(33.0) == 6.0
    assert tiet_dien_sua_coi_y(33.0) == 4.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ban sai coi y van chan dong dien ngoai mien, nen nhom ngoai
    # le mot minh khong phat hien duoc loi nay.
    assert ca_ngoai_le_dat(tiet_dien_sua_coi_y) is True
    da_chan = False
    try:
        tiet_dien_sua_coi_y(1001.0)
    except ValueError:
        da_chan = True
    assert da_chan, "dong dien ngoai mien ma khong chan"

    print("ban dung, ca thuong        :", ca_thuong_dat(tiet_dien))
    print("ban dung, tai moc          :",
          ca_tai_moc_dat(tiet_dien))
    print("ban dung, nhich qua moc    :",
          ca_nhich_qua_moc_dat(tiet_dien))
    print("ban sai, ca thuong         :",
          ca_thuong_dat(tiet_dien_sua_coi_y))
    print("ban sai, tai moc           :",
          ca_tai_moc_dat(tiet_dien_sua_coi_y))
    print("ban sai, nhich qua moc     :",
          ca_nhich_qua_moc_dat(tiet_dien_sua_coi_y))
    print("nhom ca bat duoc loi       :",
          ca_bat_duoc_loi(tiet_dien_sua_coi_y))
