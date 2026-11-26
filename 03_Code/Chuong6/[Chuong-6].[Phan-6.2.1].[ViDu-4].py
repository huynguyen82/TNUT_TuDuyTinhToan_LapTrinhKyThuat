# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.4
Chương, mục : Chương 6, Mục 6.2.2
Đề bài      : Bộ ca kiểm thử của hàm Newton, thiết kế từ bảng đặc
              tả trước khi viết hàm, chạy trên ba bản lỗi cài sẵn
              và trên bản đúng. So với bộ ca viết sau mã.
Đầu vào     : không có
Đầu ra      : bảng bốn bản nhân hai bộ ca
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
Ghi chú §7  : tệp này đứng trước Mục 6.3.1 nên vùng in sách không
              dùng `try`. Hàm trả về giá trị quy ước khi không tính
              được, đúng cách của Mục 6.2.1.
"""

import math

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200
KHONG_TINH_DUOC = -1.0


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


def f_dao_ham(x):
    """Dao ham cua f."""
    return 3.0 * x ** 2 - 2.0


def chia_doi(a, b):
    """Nghiem bang phep chia doi, dung lam nguon doc lap."""
    while b - a > SAI_SO:
        giua = (a + b) / 2.0
        if f(a) * f(giua) < 0.0:
            b = giua
        else:
            a = giua
    return (a + b) / 2.0


# Kết quả mong đợi lấy từ một nguồn độc lập với hàm Newton.
NGHIEM_DOC_LAP = chia_doi(2.0, 3.0)
# Điểm đầu làm đạo hàm bằng 0: 3*x**2 - 2 = 0 cho x = can(2/3).
X0_DAO_HAM_BANG_0 = math.sqrt(2.0 / 3.0)


def newton(x0):
    """Nghiem bang phuong phap Newton. Tra ve (nghiem, so luot)."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            return KHONG_TINH_DUOC, -1
        x_moi = x_cu - f(x_cu) / d
        if abs(x_moi - x_cu) <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def newton_loi_1(x0):
    """Ban loi 1: khong kiem dao ham bang 0."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        x_moi = x_cu - f(x_cu) / f_dao_ham(x_cu)
        if abs(x_moi - x_cu) <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def newton_loi_2(x0):
    """Ban loi 2: thieu abs trong dieu kien dung."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            return KHONG_TINH_DUOC, -1
        x_moi = x_cu - f(x_cu) / d
        if x_moi - x_cu <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def newton_loi_3(x0):
    """Ban loi 3: lech mot o so luot tra ve."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            return KHONG_TINH_DUOC, -1
        x_moi = x_cu - f(x_cu) / d
        if abs(x_moi - x_cu) <= SAI_SO:
            return x_moi, so_luot - 1
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


# --- in-sach ---
def bo_ca_thiet_ke_truoc(ham_newton):
    """Ba ca dung tu bang dac ta, truoc khi viet dong ma nao."""
    # Ca thuong: nghiem trung nguon doc lap; Newton hoi tu binh
    # phuong nen so luot phai nam trong khoang 1 toi 10.
    nghiem, so_luot = ham_newton(3.0)
    assert abs(nghiem - NGHIEM_DOC_LAP) < 1e-8, "nghiem sai"
    assert 1 <= so_luot <= 10, f"so luot bat thuong: {so_luot}"

    # Ca bien: dao ham bang 0 tai diem dau, phai bao khong tinh
    # duoc chu khong duoc tra ve mot con so.
    nghiem, so_luot = ham_newton(X0_DAO_HAM_BANG_0)
    assert nghiem == KHONG_TINH_DUOC, "phai bao khong tinh duoc"

    # Ca bien: diem dau dung bang nghiem, phai dung sau 1 luot.
    nghiem, so_luot = ham_newton(NGHIEM_DOC_LAP)
    assert so_luot == 1, f"phai dung sau 1 luot: {so_luot}"


def bo_ca_viet_sau(ham_newton):
    """Mot ca, ket qua mong doi lay tu chinh dau ra cua ham."""
    nghiem, so_luot = ham_newton(3.0)
    mong_doi = nghiem
    assert nghiem == mong_doi, "nghiem sai"
# --- het-in-sach ---


def chay_bo_ca(bo_ca, ham_newton):
    """Tra ve True khi bo ca bat duoc loi cua ham_newton."""
    try:
        bo_ca(ham_newton)
    except (AssertionError, ZeroDivisionError):
        return True
    return False


CAC_BAN = (
    ("ban dung                 ", newton),
    ("loi 1 khong kiem dao ham ", newton_loi_1),
    ("loi 2 thieu abs          ", newton_loi_2),
    ("loi 3 lech mot so luot   ", newton_loi_3),
)

print("Ban                       | Viet sau | Thiet ke truoc")
for _ten, _ban in CAC_BAN:
    _sau = chay_bo_ca(bo_ca_viet_sau, _ban)
    _truoc = chay_bo_ca(bo_ca_thiet_ke_truoc, _ban)
    _c1 = "bat duoc " if _sau else "khong    "
    _c2 = "bat duoc" if _truoc else "khong"
    print(f"{_ten} | {_c1}| {_c2}")

SO_BAT_SAU = sum(chay_bo_ca(bo_ca_viet_sau, ban)
                 for _, ban in CAC_BAN[1:])
SO_BAT_TRUOC = sum(chay_bo_ca(bo_ca_thiet_ke_truoc, ban)
                   for _, ban in CAC_BAN[1:])
print()
print(f"Bo ca viet sau bat duoc      : {SO_BAT_SAU} / 3")
print(f"Bo ca thiet ke truoc bat duoc: {SO_BAT_TRUOC} / 3")

if __name__ == "__main__":
    # Bộ ca thiết kế trước bắt được nhiều lỗi hơn bộ ca viết sau.
    assert SO_BAT_TRUOC > SO_BAT_SAU, \
        "bo ca thiet ke truoc phai bat duoc nhieu hon"

    # Bộ ca viết sau không bắt được bản lỗi nào, vì kết quả mong
    # đợi của nó lấy từ chính đầu ra — đúng lỗi L4.3-3.
    assert SO_BAT_SAU == 0, "bo ca viet sau khong bat duoc gi"

    # Không bộ ca nào báo động giả trên bản đúng.
    assert not chay_bo_ca(bo_ca_thiet_ke_truoc, newton), \
        "ban dung phai dat bo ca thiet ke truoc"

    print()
    print("Moi khang dinh dat.")
