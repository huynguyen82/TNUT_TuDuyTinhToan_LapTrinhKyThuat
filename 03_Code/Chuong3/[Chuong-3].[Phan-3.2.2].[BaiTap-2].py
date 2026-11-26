# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.2
Chương, mục : Chương 3, Mục 3.2.2
Đề bài      : Cho ba vòng lặp while, chỉ ra vòng nào chạy mãi,
              nêu dòng còn thiếu hoặc viết sai, và sửa.
Đầu vào     : ba đoạn mã, mô hình hoá bằng ba hàm có giới hạn
              số lượt để không treo khi kiểm
Đầu ra      : kết luận cho từng đoạn và bản sửa
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

GIOI_HAN_LUOT = 1000


def dem_luot(ham, *tham_so):
    """Chạy một vòng lặp có chặn số lượt.

    Trả về (so_luot, co_dung). co_dung là False khi vòng lặp
    chạm giới hạn, tức nó sẽ chạy mãi nếu không chặn.
    """
    so_luot = ham(*tham_so)
    return so_luot, so_luot < GIOI_HAN_LUOT


def doan_a_thieu_dong_tang():
    """Thân vòng lặp thiếu dòng tăng biến đếm."""
    chi_so = 0
    so_luot = 0
    while chi_so < 3 and so_luot < GIOI_HAN_LUOT:
        so_luot = so_luot + 1
    return so_luot


def doan_a_da_sua():
    """Bản sửa: thêm dòng tăng biến đếm vào cuối thân."""
    chi_so = 0
    so_luot = 0
    while chi_so < 3 and so_luot < GIOI_HAN_LUOT:
        so_luot = so_luot + 1
        chi_so = chi_so + 1
    return so_luot


def doan_b_phep_bang():
    """Điều kiện dùng phép bằng, biến đếm nhảy 3 nên bỏ qua."""
    chi_so = 0
    so_luot = 0
    while chi_so != 10 and so_luot < GIOI_HAN_LUOT:
        chi_so = chi_so + 3
        so_luot = so_luot + 1
    return so_luot


def doan_b_da_sua():
    """Bản sửa: đổi phép bằng thành phép nhỏ hơn."""
    chi_so = 0
    so_luot = 0
    while chi_so < 10 and so_luot < GIOI_HAN_LUOT:
        chi_so = chi_so + 3
        so_luot = so_luot + 1
    return so_luot


def doan_c_continue_truoc_dong_tang():
    """continue đặt trước dòng tăng biến đếm."""
    chi_so = 0
    so_luot = 0
    while chi_so < 5 and so_luot < GIOI_HAN_LUOT:
        so_luot = so_luot + 1
        if chi_so == 2:
            continue
        chi_so = chi_so + 1
    return so_luot


def doan_c_da_sua():
    """Bản sửa: dùng for với range, biến đếm tăng ngầm."""
    so_luot = 0
    for chi_so in range(5):
        so_luot = so_luot + 1
        if chi_so == 2:
            continue
    return so_luot


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Doan a chay mai vi dieu kien khong bao gio doi gia tri.
    so_luot, co_dung = dem_luot(doan_a_thieu_dong_tang)
    assert co_dung is False
    assert so_luot == GIOI_HAN_LUOT
    # Ban sua dung sau dung ba luot.
    so_luot_sua, co_dung_sua = dem_luot(doan_a_da_sua)
    assert co_dung_sua is True and so_luot_sua == 3

    # --- Trường hợp biên ---------------------------------------
    # Doan b chay mai vi bien dem nhay qua moc 10.
    assert dem_luot(doan_b_phep_bang)[1] is False
    # Ban sua dung sau bon luot: 0, 3, 6, 9 roi 12 vuot 10.
    assert dem_luot(doan_b_da_sua) == (4, True)
    # Doan c chay mai tu luot gap continue.
    assert dem_luot(doan_c_continue_truoc_dong_tang)[1] is False
    # Ban sua dung sau nam luot, ke ca luot bi continue.
    assert dem_luot(doan_c_da_sua) == (5, True)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Vong lap for voi range luon dung, ke ca khi than co
    # continue, vi dong tang bien dem nam ngam trong range.
    so_luot_rong = 0
    for _ in range(0):
        so_luot_rong = so_luot_rong + 1
    assert so_luot_rong == 0

    print("BT 3.2")
    for ten, ham, ham_sua in (
            ("a", doan_a_thieu_dong_tang, doan_a_da_sua),
            ("b", doan_b_phep_bang, doan_b_da_sua),
            ("c", doan_c_continue_truoc_dong_tang, doan_c_da_sua)):
        _, dung = dem_luot(ham)
        so_luot_sua, _ = dem_luot(ham_sua)
        print(f"  Doan {ten}: chay mai = {not dung}, "
              f"sau khi sua chay {so_luot_sua} luot")
