# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.7
Chương, mục : Chương 6, Mục 6.2.1
Đề bài      : Thiết kế bộ ca cho hàm Newton trước khi viết hàm, rồi
              viết hàm, rồi gieo ba lỗi cài sẵn khác ba lỗi của Ví
              dụ 6.4 và đếm số lỗi bộ ca bắt được. So với bộ ca viết
              sau mã.
Đầu vào     : bài toán A6, f(x) = x**3 - 2x - 5
Đầu ra      : bảng bốn bản nhân hai bộ ca
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
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
    """Nguon doc lap: nghiem bang phep chia doi."""
    while b - a > SAI_SO:
        giua = (a + b) / 2.0
        if f(a) * f(giua) < 0.0:
            b = giua
        else:
            a = giua
    return (a + b) / 2.0


NGHIEM_DOC_LAP = chia_doi(2.0, 3.0)
X0_DAO_HAM_BANG_0 = math.sqrt(2.0 / 3.0)

# Bảng đặc tả ba phần, lập trước khi viết hàm.
DAC_TA = (
    ("Dau vao", "diem dau x0 kieu so thuc"),
    ("Xu ly", "lap x = x - f(x)/f'(x) toi khi buoc nho hon sai so; "
              "chan truoc khi f'(x) bang 0"),
    ("Dau ra", "(nghiem, so luot lap), hoac gia tri quy uoc khi "
               "khong tinh duoc"),
)


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


def ban_loi_a(x0):
    """Loi A: dung f_dao_ham(x_moi) thay vi f_dao_ham(x_cu)."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        x_moi = x_cu - f(x_cu) / f_dao_ham(x_cu + 1.0)
        if abs(x_moi - x_cu) <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def ban_loi_b(x0):
    """Loi B: chan dao ham bang 0 nhung van tra ve mot con so."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            return x_cu, so_luot
        x_moi = x_cu - f(x_cu) / d
        if abs(x_moi - x_cu) <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def ban_loi_c(x0):
    """Loi C: sai so so sanh voi f(x) thay vi voi buoc nhay."""
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            return KHONG_TINH_DUOC, -1
        x_moi = x_cu - f(x_cu) / d
        if abs(f(x_moi)) <= 1.0:
            return x_moi, so_luot
        x_cu = x_moi
    return KHONG_TINH_DUOC, -1


def bo_ca_thiet_ke_truoc(ham):
    """Ba ca dung tu bang dac ta, truoc khi viet dong ma nao."""
    nghiem, so_luot = ham(3.0)
    assert abs(nghiem - NGHIEM_DOC_LAP) < 1e-8, "nghiem sai"
    assert 1 <= so_luot <= 10, f"so luot bat thuong: {so_luot}"

    nghiem, _ = ham(X0_DAO_HAM_BANG_0)
    assert nghiem == KHONG_TINH_DUOC, "phai bao khong tinh duoc"

    _, so_luot = ham(NGHIEM_DOC_LAP)
    assert so_luot == 1, f"phai dung sau 1 luot: {so_luot}"


def bo_ca_viet_sau(ham):
    """Mot ca, ket qua mong doi lay tu chinh dau ra cua ham."""
    nghiem, _ = ham(3.0)
    assert nghiem == nghiem, "nghiem sai"


def chay(bo_ca, ham):
    """Tra ve True khi bo ca bat duoc loi cua ham."""
    try:
        bo_ca(ham)
    except (AssertionError, ZeroDivisionError, OverflowError):
        return True
    return False


CAC_BAN = (
    ("ban dung          ", newton),
    ("loi A sai doi so  ", ban_loi_a),
    ("loi B chan hong   ", ban_loi_b),
    ("loi C sai tieu chi", ban_loi_c),
)


def in_ket_qua():
    """In bang dac ta va bang bon ban nhan hai bo ca."""
    for phan, noi_dung in DAC_TA:
        print(f"{phan:<8}: {noi_dung}")
    print()
    print("Ban                | Viet sau | Thiet ke truoc")
    for ten, ham in CAC_BAN:
        sau = "bat duoc " if chay(bo_ca_viet_sau, ham) else "khong    "
        bat = chay(bo_ca_thiet_ke_truoc, ham)
        truoc = "bat duoc" if bat else "khong"
        print(f"{ten} | {sau}| {truoc}")


SO_SAU = sum(chay(bo_ca_viet_sau, h) for _, h in CAC_BAN[1:])
SO_TRUOC = sum(chay(bo_ca_thiet_ke_truoc, h) for _, h in CAC_BAN[1:])

if __name__ == "__main__":
    in_ket_qua()
    print()
    print(f"Bo ca viet sau bat duoc      : {SO_SAU} / 3")
    print(f"Bo ca thiet ke truoc bat duoc: {SO_TRUOC} / 3")

    # Bộ ca thiết kế trước bắt được cả ba bản lỗi.
    assert SO_TRUOC == 3, "bo ca thiet ke truoc phai bat du ba loi"

    # Bộ ca viết sau không bắt được bản nào, vì kết quả mong đợi
    # của nó lấy từ chính đầu ra — đúng lỗi L4.3-3.
    assert SO_SAU == 0, "bo ca viet sau khong bat duoc gi"

    # Không bộ ca nào báo động giả trên bản đúng.
    assert not chay(bo_ca_thiet_ke_truoc, newton), \
        "ban dung phai dat bo ca thiet ke truoc"

    print()
    print("Moi khang dinh dat.")
