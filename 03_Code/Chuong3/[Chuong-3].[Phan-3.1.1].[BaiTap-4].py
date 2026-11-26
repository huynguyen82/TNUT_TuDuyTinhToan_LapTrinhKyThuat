# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.4
Chương, mục : Chương 3, Mục 3.1.1
Đề bài      : Tra bảng tiết diện dây theo dòng điện bằng chuỗi
              elif năm nhánh cộng một nhánh báo vượt bảng.
Đầu vào     : dòng điện (A), miền từ 0 đến 1 000
Đầu ra      : tiết diện (mm²) một chữ số thập phân, hoặc câu
              báo vượt bảng tra
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

MIEN_DONG = (0.0, 1000.0)
VUOT_BANG = "vuot bang tra"


def tra_tiet_dien(dong_dien):
    """Tiết diện nhỏ nhất chịu được dòng điện cho trước, mm2.

    Trả về chuỗi VUOT_BANG khi dòng vượt mốc cuối của bảng.
    Phát sinh ValueError khi dòng nằm ngoài miền đo được.
    """
    if not MIEN_DONG[0] <= dong_dien <= MIEN_DONG[1]:
        raise ValueError(
            f"du lieu khong hop le: dong dien = {dong_dien}")
    if dong_dien <= 16:
        return 1.5
    elif dong_dien <= 25:
        return 2.5
    elif dong_dien <= 32:
        return 4.0
    elif dong_dien <= 40:
        return 6.0
    elif dong_dien <= 63:
        return 10.0
    else:
        return VUOT_BANG


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert tra_tiet_dien(30.0) == 4.0
    assert tra_tiet_dien(10.0) == 1.5
    assert tra_tiet_dien(50.0) == 10.0

    # --- Trường hợp biên ---------------------------------------
    # Dong dung bang mot moc nhan tiet dien cua moc do, vi dieu
    # kien dung dau nho hon hoac bang.
    assert tra_tiet_dien(16.0) == 1.5
    assert tra_tiet_dien(16.1) == 2.5
    assert tra_tiet_dien(63.0) == 10.0
    assert tra_tiet_dien(63.1) == VUOT_BANG
    # Dong bang 0 la can duoi hop le cua mien.
    assert tra_tiet_dien(0.0) == 1.5
    # Tiet dien tang don dieu theo dong dien.
    truoc = 0.0
    for dong in (5.0, 20.0, 30.0, 35.0, 50.0):
        hien = tra_tiet_dien(dong)
        assert hien >= truoc, dong
        truoc = hien

    # --- Trường hợp ngoại lệ -----------------------------------
    assert tra_tiet_dien(100.0) == VUOT_BANG
    da_chan = False
    try:
        tra_tiet_dien(-5.0)
    except ValueError as loi:
        da_chan = "dong dien" in str(loi)
    assert da_chan, "dong am ma van tra duoc"

    print("BT 3.4")
    for dong in (10.0, 16.0, 30.0, 100.0):
        ket_qua = tra_tiet_dien(dong)
        if ket_qua == VUOT_BANG:
            print(f"  {dong:>6} A -> {ket_qua}")
        else:
            print(f"  {dong:>6} A -> {ket_qua:.1f} mm2")
