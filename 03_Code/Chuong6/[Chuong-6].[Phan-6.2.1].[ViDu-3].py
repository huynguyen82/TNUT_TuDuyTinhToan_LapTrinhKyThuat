# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.3
Chương, mục : Chương 6, Mục 6.2.1
Đề bài      : Bộ ba loại ca kiểm thử cho hàm chia đôi của bài toán
              A6, và số dòng của hàm mà bộ ca đi qua, so với một ca
              thường duy nhất.
Đầu vào     : không có
Đầu ra      : kết quả ba ca, và ba số đếm dòng đã đi qua
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
Ghi chú §7  : tệp này đứng trước Mục 6.3.1 nên không dùng `try`.
              Dữ liệu không hợp lệ bị chặn trước bằng `if` và hàm
              trả về giá trị quy ước, đúng công cụ của Mục 3.1.1.
"""

import sys

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200
# Giá trị quy ước cho trường hợp không tính được nghiệm.
KHONG_TINH_DUOC = -1.0


def chia_doi(ham, a, b):
    """Nghiem cua ham tren doan [a, b]. Tra ve (nghiem, so luot).

    Tra ve (KHONG_TINH_DUOC, -1) khi doan khong hop le hoac khi ham
    khong doi dau tren doan.
    """
    if a >= b:
        return KHONG_TINH_DUOC, -1
    f_a = ham(a)
    f_b = ham(b)
    if f_a == 0.0:
        return a, 0
    if f_b == 0.0:
        return b, 0
    if f_a * f_b > 0.0:
        return KHONG_TINH_DUOC, -1
    so_luot = 0
    while b - a > SAI_SO and so_luot < SO_LAN_TOI_DA:
        giua = (a + b) / 2.0
        f_giua = ham(giua)
        so_luot += 1
        if f_giua == 0.0:
            return giua, so_luot
        if f_a * f_giua < 0.0:
            b = giua
        else:
            a = giua
            f_a = f_giua
    return (a + b) / 2.0, so_luot


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


# --- in-sach ---
def ca_thuong():
    """Ca thuong: doan [2, 3], ham doi dau tren doan."""
    nghiem, so_luot = chia_doi(f, 2.0, 3.0)
    assert abs(nghiem - 2.094551) < 1e-5, "nghiem sai"
    return f"nghiem {nghiem:.6f} sau {so_luot} luot"


def ca_bien():
    """Ca bien: nghiem nam dung tai can duoi cua doan."""
    nghiem, so_luot = chia_doi(lambda x: x - 2.0, 2.0, 3.0)
    assert nghiem == 2.0, "nghiem tai moc phai bang dung can duoi"
    assert so_luot == 0, "khong can luot lap nao"
    return f"nghiem {nghiem} sau {so_luot} luot"


def ca_khong_hop_le():
    """Ca du lieu khong hop le: ham khong doi dau tren doan."""
    nghiem, so_luot = chia_doi(f, 0.0, 1.0)
    assert nghiem == KHONG_TINH_DUOC, "phai bao khong tinh duoc"
    assert so_luot == -1, "so luot phai la gia tri quy uoc"
    return f"gia tri quy uoc {nghiem} va {so_luot}"


# --- het-in-sach ---

for _ten, _ca in (("Ca thuong       ", ca_thuong),
                  ("Ca bien         ", ca_bien),
                  ("Ca khong hop le ", ca_khong_hop_le)):
    print(f"{_ten}: {_ca()}")


def dong_than_ham(ham):
    """Tap so dong cua than ham, bo dong `def`."""
    ma = ham.__code__
    cac_dong = {dong for _, _, dong in ma.co_lines()
                if dong is not None}
    return cac_dong - {ma.co_firstlineno}


def dong_da_chay(cac_ca):
    """Tap so dong cua chia_doi ma cac ca di qua."""
    ten_tep = chia_doi.__code__.co_filename
    da_chay = set()

    def theo_dau(khung, su_kien, doi_so):
        if (khung.f_code.co_filename == ten_tep
                and khung.f_code.co_name == "chia_doi"):
            if su_kien == "line":
                da_chay.add(khung.f_lineno)
            return theo_dau
        return None

    sys.settrace(theo_dau)
    try:
        for ca in cac_ca:
            ca()
    finally:
        sys.settrace(None)
    return da_chay


def ca_tai_can_tren():
    """Ca tai moc: nghiem nam dung tai can tren."""
    return chia_doi(lambda x: x - 3.0, 2.0, 3.0)


def ca_tai_trung_diem():
    """Ca tai moc: nghiem nam dung tai trung diem dau tien."""
    return chia_doi(lambda x: x - 2.5, 2.0, 3.0)


def ca_can_nguoc():
    """Ca thu tu: hai can viet nguoc nhau."""
    return chia_doi(f, 3.0, 2.0)


TONG = len(dong_than_ham(chia_doi))
MOT_CA = len(dong_da_chay([ca_thuong]))
BO_BA = len(dong_da_chay([ca_thuong, ca_bien, ca_khong_hop_le]))
BO_SAU = len(dong_da_chay([ca_thuong, ca_bien, ca_khong_hop_le,
                           ca_tai_can_tren, ca_tai_trung_diem,
                           ca_can_nguoc]))

print()
print(f"Tong so dong cua than ham chia_doi : {TONG}")
print(f"Mot ca thuong di qua               : {MOT_CA}")
print(f"Bo ba loai ca di qua               : {BO_BA}")
print(f"Bo sau ca thiet ke truoc di qua    : {BO_SAU}")

if __name__ == "__main__":
    # Bộ ba loại ca đi qua nhiều dòng hơn một ca thường.
    assert BO_BA > MOT_CA, "bo ba phai di qua nhieu dong hon"

    # Ngay cả bộ ba loại ca cũng chưa phủ hết thân hàm; ba dòng còn
    # thiếu là ba nhánh tại mốc, nội dung của Mục 6.2.2.
    assert BO_BA < TONG, "bo ba chua the phu het than ham"

    # Bộ sáu ca thiết kế trước phủ hết thân hàm.
    assert BO_SAU == TONG, "bo sau ca phai phu het than ham"

    print()
    print("Moi khang dinh dat.")
