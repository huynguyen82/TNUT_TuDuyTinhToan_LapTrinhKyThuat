# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.5
Chương, mục : Chương 4, Mục 4.1.1
Đề bài      : Chuyển chương trình tra tiết diện dây của Bài tập
              3.4 thành một hàm, rồi tra ba dòng điện trong một
              lần chạy.
Đầu vào     : ba dòng điện (A), miền từ 0 đến 1 000
Đầu ra      : ba tiết diện (mm²), một chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Số liệu bảng tra là giả
định của đề bài, lấy từ Mục 3.1.1.
"""

MIEN_DONG = (0.0, 1000.0)
VUOT_BANG_TRA = -1.0


def tiet_dien(dong_dien):
    """Tiết diện dây nhỏ nhất đủ chịu dòng, mm².

    Trả về VUOT_BANG_TRA bằng −1,0 khi dòng điện vượt mốc cuối
    của bảng; giá trị này nói được điều đó, khác với None.
    Phát sinh ValueError khi dòng điện nằm ngoài miền.
    """
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


def mo_ta(dong_dien):
    """Một dòng kết quả đã định dạng cho một dòng điện."""
    gia_tri = tiet_dien(dong_dien)
    if gia_tri == VUOT_BANG_TRA:
        return f"{dong_dien:>6.1f} A  vuot bang tra"
    return f"{dong_dien:>6.1f} A  {gia_tri:.1f} mm2"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Dap so trung Bai tap 3.4 tren cung du lieu.
    assert tiet_dien(30.0) == 4.0
    assert tiet_dien(20.0) == 2.5
    assert tiet_dien(50.0) == 10.0

    # --- Trường hợp biên ---------------------------------------
    # Dong dung bang moc nhan tiet dien cua moc do, ca nam moc.
    assert tiet_dien(16.0) == 1.5
    assert tiet_dien(25.0) == 2.5
    assert tiet_dien(32.0) == 4.0
    assert tiet_dien(40.0) == 6.0
    assert tiet_dien(63.0) == 10.0
    # Nhich qua moc thi sang moc tiep theo.
    assert tiet_dien(16.1) == 2.5
    # Dong bang 0 va dong bang can tren cua mien.
    assert tiet_dien(0.0) == 1.5
    assert tiet_dien(1000.0) == VUOT_BANG_TRA

    # --- Trường hợp ngoại lệ -----------------------------------
    # Vuot moc cuoi: tra ve gia tri noi duoc dieu do, khong None.
    assert tiet_dien(100.0) == VUOT_BANG_TRA
    assert tiet_dien(100.0) is not None
    assert mo_ta(100.0).endswith("vuot bang tra")
    # Dong dien ngoai mien phat sinh ValueError.
    da_chan = 0
    for thu_tu in range(2):
        gia_tri = (-1.0, 1001.0)[thu_tu]
        try:
            tiet_dien(gia_tri)
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 2, "dong dien ngoai mien ma khong chan"

    for thu_tu in range(3):
        print(mo_ta((30.0, 16.0, 100.0)[thu_tu]))
