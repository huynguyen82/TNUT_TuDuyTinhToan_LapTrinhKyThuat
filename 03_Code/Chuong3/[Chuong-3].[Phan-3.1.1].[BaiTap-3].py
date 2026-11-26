# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.3
Chương, mục : Chương 3, Mục 3.1.1
Đề bài      : Phân loại trạng thái động cơ theo bốn miền nhiệt
              độ, dùng chuỗi elif.
Đầu vào     : nhiệt độ (°C), miền từ −40 đến 300
Đầu ra      : một trong bốn chuỗi trạng thái
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

NGUONG_CANH_BAO = 60.0
NGUONG_NGUY_HIEM = 80.0
NGUONG_DUNG_MAY = 100.0
MIEN_NHIET = (-40.0, 300.0)


def phan_loai(nhiet_do):
    """Trạng thái động cơ theo nhiệt độ vỏ máy.

    Phát sinh ValueError khi nhiệt độ nằm ngoài miền đo được
    của cảm biến.
    """
    if not MIEN_NHIET[0] <= nhiet_do <= MIEN_NHIET[1]:
        raise ValueError(
            f"du lieu khong hop le: nhiet do = {nhiet_do}")
    if nhiet_do < NGUONG_CANH_BAO:
        return "binh thuong"
    elif nhiet_do < NGUONG_NGUY_HIEM:
        return "canh bao"
    elif nhiet_do < NGUONG_DUNG_MAY:
        return "nguy hiem"
    else:
        return "dung may"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert phan_loai(45.0) == "binh thuong"
    assert phan_loai(72.5) == "canh bao"
    assert phan_loai(85.0) == "nguy hiem"
    assert phan_loai(120.0) == "dung may"

    # --- Trường hợp biên ---------------------------------------
    # Chin ca bien quanh ba nguong. Gia tri dung bang nguong
    # thuoc mien phia tren, vi dieu kien dung dau nho hon thuan.
    assert phan_loai(59.9) == "binh thuong"
    assert phan_loai(60.0) == "canh bao"
    assert phan_loai(60.1) == "canh bao"
    assert phan_loai(79.9) == "canh bao"
    assert phan_loai(80.0) == "nguy hiem"
    assert phan_loai(80.1) == "nguy hiem"
    assert phan_loai(99.9) == "nguy hiem"
    assert phan_loai(100.0) == "dung may"
    assert phan_loai(100.1) == "dung may"
    # Hai can cua mien do deu hop le.
    assert phan_loai(-40.0) == "binh thuong"
    assert phan_loai(300.0) == "dung may"

    # --- Trường hợp ngoại lệ -----------------------------------
    for ngoai_mien in (500.0, -41.0):
        da_chan = False
        try:
            phan_loai(ngoai_mien)
        except ValueError as loi:
            da_chan = "nhiet do" in str(loi)
        assert da_chan, f"{ngoai_mien} ngoai mien ma van chay"

    print("BT 3.3")
    for nhiet in (45.0, 60.0, 85.0, 120.0):
        print(f"  {nhiet:>6} C -> {phan_loai(nhiet)}")
