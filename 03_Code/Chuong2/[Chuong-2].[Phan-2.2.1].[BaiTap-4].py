# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.4
Chương, mục : Chương 2, Mục 2.2.1
Đề bài      : Nhận kích thước đo được dưới dạng chuỗi, ép kiểu,
              kiểm dung sai của chi tiết trục danh nghĩa 50,00 mm
              với dung sai ±0,05 mm, và in kết luận. Phân biệt
              ba tình huống: đạt, không đạt, chuỗi không ép được.
Đầu vào     : chuỗi kích thước đo được, mm
Đầu ra      : một trong ba câu kết luận
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

DANH_NGHIA_MM = 50.00
DUNG_SAI_MM = 0.05
DAT = "dat"
KHONG_DAT = "khong dat"
KHONG_HOP_LE = "du lieu khong hop le"


def ep_kieu_kich_thuoc(chuoi_do):
    """Ép chuỗi kích thước sang số thực.

    Trả về None khi chuỗi không ép kiểu được, thay vì để lỗi
    thoát ra ngoài: đề bài yêu cầu phân biệt ba tình huống chứ
    không yêu cầu dừng chương trình.
    """
    try:
        return float(chuoi_do)
    except ValueError:
        return None


def ket_luan_dung_sai(chuoi_do):
    """Trả về một trong ba câu kết luận."""
    kich_thuoc_mm = ep_kieu_kich_thuoc(chuoi_do)
    if kich_thuoc_mm is None:
        return KHONG_HOP_LE
    can_duoi = DANH_NGHIA_MM - DUNG_SAI_MM
    can_tren = DANH_NGHIA_MM + DUNG_SAI_MM
    if can_duoi <= kich_thuoc_mm <= can_tren:
        return DAT
    return KHONG_DAT


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert ket_luan_dung_sai("50.03") == DAT
    assert ket_luan_dung_sai("49.98") == DAT
    assert ket_luan_dung_sai("50.20") == KHONG_DAT
    assert ket_luan_dung_sai("49.80") == KHONG_DAT

    # --- Trường hợp biên ---------------------------------------
    # Hai cận của miền dung sai thuộc miền hợp lệ, vì phép so
    # sánh dùng dấu nhỏ hơn hoặc bằng.
    assert ket_luan_dung_sai("50.05") == DAT
    assert ket_luan_dung_sai("49.95") == DAT
    # Ngay ngoài hai cận thì không đạt.
    assert ket_luan_dung_sai("50.06") == KHONG_DAT
    assert ket_luan_dung_sai("49.94") == KHONG_DAT
    # Chuỗi có khoảng trắng thừa vẫn ép kiểu được.
    assert ket_luan_dung_sai("  50.03  ") == DAT
    # Chuỗi viết theo ký hiệu khoa học cũng ép kiểu được.
    assert ket_luan_dung_sai("5.003e1") == DAT

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dấu phẩy thập phân và chữ đều không ép kiểu được.
    assert ket_luan_dung_sai("50,03") == KHONG_HOP_LE
    assert ket_luan_dung_sai("nam muoi") == KHONG_HOP_LE
    assert ket_luan_dung_sai("") == KHONG_HOP_LE
    # Hàm ép kiểu trả None chứ không ném lỗi ra ngoài.
    assert ep_kieu_kich_thuoc("50,03") is None
    assert ep_kieu_kich_thuoc("50.03") == 50.03

    print("BT 2.4")
    for chuoi in ("50.03", "50.05", "50.06", "50,03"):
        print(f"  {chuoi:<10} -> {ket_luan_dung_sai(chuoi)}")
