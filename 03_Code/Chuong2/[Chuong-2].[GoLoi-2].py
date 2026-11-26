# -*- coding: utf-8 -*-
"""
Mã bài      : GL 2
Chương, mục : Chương 2, Bài gỡ lỗi GL2
Đề bài      : Chương trình 24 dòng kiểm dung sai một chi tiết chứa
              đúng ba lỗi: một cú pháp, một thực thi, một logic.
              Tìm ba lỗi, nêu loại và thông báo nguyên văn, sửa cả
              ba, kiểm lại bằng ba bộ dữ liệu.
Đầu vào     : chuỗi kích thước đo được, đơn vị mm
Đầu ra      : ba lỗi đã phân loại, và phiếu kết quả của bản đã sửa
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math

DANH_NGHIA = 50.00
DUNG_SAI = 0.05

BA_LOI = (
    (4, "cu phap", "DUNG_SAI = 0,05",
     "SyntaxError: leading zeros in decimal integer literals "
     "are not permitted",
     "Python dung dau cham thap phan: DUNG_SAI = 0.05"),
    (7, "thuc thi", "kich_thuoc = int(dong_nhap)",
     "ValueError: invalid literal for int() with base 10: '50.03'",
     "ep sang so thuc: kich_thuoc = float(dong_nhap)"),
    (13, "logic", "math.isclose(kich_thuoc, DANH_NGHIA)",
     "khong bao gi; nguong mac dinh la nguong tuong doi rat nho "
     "nen 50,03 bi ket luan khong dat",
     "truyen nguong lay tu dung sai: abs_tol=DUNG_SAI"),
)


def kiem_mot_chi_tiet(dong_nhap):
    """Ban da sua du ba loi. Tra ve (kich thuoc, lech, ket luan).

    Phat sinh ValueError khi chuoi khong ep kieu duoc, dung nhu ca
    du lieu khong hop le cua de bai.
    """
    kich_thuoc = float(dong_nhap)
    lech = kich_thuoc - DANH_NGHIA
    dat = math.isclose(kich_thuoc, DANH_NGHIA, abs_tol=DUNG_SAI)
    return kich_thuoc, lech, "dat" if dat else "khong dat"


def kiem_ban_con_loi_dong_13(dong_nhap):
    """Ban chi con loi dong 13: goi isclose khong truyen nguong."""
    kich_thuoc = float(dong_nhap)
    dat = math.isclose(kich_thuoc, DANH_NGHIA)
    return "dat" if dat else "khong dat"


def in_ket_qua():
    """In bang ba loi va phieu ket qua cua ban da sua."""
    print("Dong | Loai     | Thong bao hoac bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    kich_thuoc, lech, ket_luan = kiem_mot_chi_tiet("50.03")
    can_duoi = DANH_NGHIA - DUNG_SAI
    can_tren = DANH_NGHIA + DUNG_SAI
    print(f"{'Mien hop le':<16}{can_duoi:>8.2f}{can_tren:>8.2f}")
    print(f"{'Do duoc':<16}{kich_thuoc:>8.2f}")
    print(f"{'Do lech':<16}{lech:>8.2f}")
    print(f"{'Ket luan':<16}{ket_luan:>8}")
    print()
    print(f"Ban con loi dong 13 voi 50.03: "
          f"{kiem_ban_con_loi_dong_13('50.03')}")


if __name__ == "__main__":
    in_ket_qua()

    # Ba lỗi thuộc ba loại khác nhau.
    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    # Ca thường: 50,03 mm cho độ lệch 0,03 và kết luận đạt.
    _kt, _lech, _ket = kiem_mot_chi_tiet("50.03")
    assert abs(_lech - 0.03) < 1e-9 and _ket == "dat", \
        "ca thuong phai cho lech 0,03 va ket luan dat"

    # Ca biên: cận trên thuộc miền hợp lệ.
    assert kiem_mot_chi_tiet("50.05")[2] == "dat", \
        "can tren phai thuoc mien hop le"

    # Ca không hợp lệ: dấu phẩy thập phân bị chặn ở bước ép kiểu.
    _da_chan = False
    try:
        kiem_mot_chi_tiet("50,03")
    except ValueError:
        _da_chan = True
    assert _da_chan, "dau phay thap phan phai bi chan"

    # Lỗi dòng 13 là lỗi im lặng: cùng dữ liệu 50,03 mm, bản còn
    # lỗi kết luận **ngược** mà không báo gì.
    assert kiem_ban_con_loi_dong_13("50.03") == "khong dat", \
        "ban con loi phai ket luan nguoc"
    assert _ket == "dat", "ban da sua phai ket luan dat"

    print()
    print("Moi khang dinh dat.")
