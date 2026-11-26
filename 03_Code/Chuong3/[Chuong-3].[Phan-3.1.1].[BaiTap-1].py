# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.1
Chương, mục : Chương 3, Mục 3.1.1
Đề bài      : Dự đoán đầu ra của đoạn mã dùng bốn lệnh if
              độc lập có hai miền chồng lấn, rồi chạy đối
              chiếu.
Đầu vào     : nhiệt độ (°C)
Đầu ra      : trạng thái theo đoạn mã sai và theo đáp án đúng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

NGUONG = (60.0, 80.0, 100.0)


def bon_if_chong_lan(nhiet_do):
    """Đoạn mã của đề bài: nhánh ba viết thiếu cận trên nên
    miền của nó chồng lấn miền của nhánh bốn."""
    trang_thai = "binh thuong"
    if nhiet_do < NGUONG[0]:
        trang_thai = "binh thuong"
    if NGUONG[0] <= nhiet_do < NGUONG[1]:
        trang_thai = "canh bao"
    if nhiet_do >= NGUONG[1]:
        trang_thai = "nguy hiem"
    if nhiet_do >= NGUONG[2]:
        trang_thai = "dung may"
    return trang_thai


def chuoi_elif_dung(nhiet_do):
    """Đáp án đúng, viết bằng chuỗi elif."""
    if nhiet_do < NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    else:
        return "dung may"


def so_nhanh_khop(nhiet_do):
    """Số nhánh của đoạn mã sai mà điều kiện cùng đúng."""
    dem = 0
    if nhiet_do < NGUONG[0]:
        dem = dem + 1
    if NGUONG[0] <= nhiet_do < NGUONG[1]:
        dem = dem + 1
    if nhiet_do >= NGUONG[1]:
        dem = dem + 1
    if nhiet_do >= NGUONG[2]:
        dem = dem + 1
    return dem


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # 45 do C: dung mot nhanh khop, hai cach cho cung ket qua.
    assert bon_if_chong_lan(45.0) == "binh thuong"
    assert chuoi_elif_dung(45.0) == "binh thuong"
    assert so_nhanh_khop(45.0) == 1

    # --- Trường hợp biên ---------------------------------------
    # 85 do C: van mot nhanh khop, ket qua van dung, nen loi
    # khong lo ra voi so do nay.
    assert bon_if_chong_lan(85.0) == chuoi_elif_dung(85.0)
    assert so_nhanh_khop(85.0) == 1
    # 120 do C: hai nhanh cung khop. Nhanh bon gan de nhanh ba
    # nen ket qua van dung, nhung dung vi ly do sai.
    assert so_nhanh_khop(120.0) == 2
    assert bon_if_chong_lan(120.0) == "dung may"
    assert chuoi_elif_dung(120.0) == "dung may"
    # Dao thu tu hai lenh if cuoi thi ket qua lat sang sai.
    nhiet = 120.0
    trang_thai = "binh thuong"
    if nhiet >= NGUONG[2]:
        trang_thai = "dung may"
    if nhiet >= NGUONG[1]:
        trang_thai = "nguy hiem"
    assert trang_thai == "nguy hiem"
    assert trang_thai != chuoi_elif_dung(nhiet)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Chuoi elif khong bao gio co hai nhanh cung chay, ke ca
    # khi mien chong lan, vi no dung o nhanh dung dau tien.
    for nhiet_thu in (45.0, 60.0, 85.0, 100.0, 120.0):
        assert chuoi_elif_dung(nhiet_thu) in (
            "binh thuong", "canh bao", "nguy hiem", "dung may")

    print("BT 3.1")
    for nhiet_thu in (45.0, 85.0, 120.0):
        print(f"  {nhiet_thu:>6} C: doan sai "
              f"{bon_if_chong_lan(nhiet_thu):<12}"
              f"dap an {chuoi_elif_dung(nhiet_thu):<12}"
              f"so nhanh khop {so_nhanh_khop(nhiet_thu)}")
