# -*- coding: utf-8 -*-
"""
Mã bài      : GL 6
Chương, mục : Chương 6, Bài gỡ lỗi GL6
Đề bài      : Chương trình 24 dòng tìm nghiệm bằng phương pháp
              Newton chứa đúng ba lỗi: một cú pháp, một thực thi,
              một logic. Tìm ba lỗi, nêu loại, sửa, và nộp kèm
              bảng năm bước cho lỗi logic.
Đầu vào     : điểm đầu x0 kiểu số thực
Đầu ra      : nghiệm và số lượt lặp
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200

BA_LOI = (
    (9, "cu phap", "def f_dao_ham(x) khong co dau hai cham",
     "SyntaxError: expected ':'",
     "them dau hai cham cuoi dong def"),
    (18, "thuc thi", "khong kiem f_dao_ham(x_cu) khac 0 truoc khi chia",
     "ZeroDivisionError: float division by zero voi x0 = 0,8165",
     "chan dao ham bang 0 truoc phep chia va bao loi ro rang"),
    (19, "logic", "if x_moi - x_cu <= SAI_SO, thieu abs",
     "khong bao gi; voi x0 = 3,0 ham dung ngay luot dau va tra ve "
     "2,36 thay vi 2,0945514815",
     "dung abs(x_moi - x_cu) <= SAI_SO"),
)

# Bảng năm bước cho lỗi logic ở dòng 19.
NAM_BUOC = (
    ("Buoc 1 tai lap",
     "x0 = 3,0 la bo du lieu nho nhat tai lap duoc: mot lan goi"),
    ("Buoc 2 doc thong bao",
     "khong co thong bao nao; buoc nay khong giup gi"),
    ("Buoc 3 khoanh vung",
     "in x_cu va x_moi moi luot; thay ham dung ngay sau luot 1"),
    ("Buoc 4 bang vet",
     "luot 1 cho x_moi - x_cu = -0,64, am, nen dieu kien <= 1e-10 "
     "dung ngay du buoc nhay con rat lon"),
    ("Buoc 5 sua",
     "them abs vao dieu kien dung, roi chay lai ca ba bo ca"),
)


def f(x):
    """Ham can tim nghiem: x**3 - 2x - 5."""
    return x ** 3 - 2.0 * x - 5.0


def f_dao_ham(x):
    """Dao ham cua f."""
    return 3.0 * x ** 2 - 2.0


def newton(x0, thieu_abs=False):
    """Tra ve (nghiem, so luot). Ban da sua du ba loi.

    Phat sinh ValueError khi dao ham bang 0 tai mot diem lap.
    """
    x_cu = x0
    for so_luot in range(1, SO_LAN_TOI_DA + 1):
        d = f_dao_ham(x_cu)
        if d == 0.0:
            raise ValueError(f"dao ham bang 0 tai x = {x_cu}")
        x_moi = x_cu - f(x_cu) / d
        buoc = x_moi - x_cu if thieu_abs else abs(x_moi - x_cu)
        if buoc <= SAI_SO:
            return x_moi, so_luot
        x_cu = x_moi
    raise ValueError("khong hoi tu sau so luot toi da")


X0_DAO_HAM_BANG_0 = math.sqrt(2.0 / 3.0)


def in_ket_qua():
    """In bang ba loi, bang nam buoc, va ket qua ba bo ca."""
    print("Dong | Loai     | Bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    print("Bang nam buoc cho loi logic dong 19:")
    for ten, noi_dung in NAM_BUOC:
        print(f"  {ten:<22}: {noi_dung}")
    print()
    for x0 in (3.0, 2.0):
        dung = newton(x0)
        sai = newton(x0, thieu_abs=True)
        print(f"x0 = {x0}: ban da sua {dung[0]:.10f} sau "
              f"{dung[1]} luot | ban con loi {sai[0]:.10f} sau "
              f"{sai[1]} luot")


if __name__ == "__main__":
    in_ket_qua()

    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"
    assert len(NAM_BUOC) == 5, "bang nam buoc phai du nam dong"

    # Ca thường: x0 = 3,0 cho nghiệm 2,0945514815 sau 6 lượt.
    _n, _l = newton(3.0)
    assert abs(_n - 2.0945514815) < 1e-9, "nghiem sai"
    assert _l == 6, f"phai 6 luot, nhan duoc {_l}"

    # Bản lỗi dòng 19 với x0 = 3,0 dừng ngay lượt đầu và cho 2,36.
    _ns, _ls = newton(3.0, thieu_abs=True)
    assert _ls == 1, "ban loi dung ngay luot dau"
    assert abs(_ns - 2.36) < 1e-9, f"ban loi cho {_ns}"

    # Ca biên x0 = 2,0: các bước Newton đi **lên** nên hiệu dương,
    # bản lỗi chạy thêm một lượt và cho 2,0945681211 — trùng bản
    # đúng tới bốn chữ số thập phân, nên ca này gần như che lỗi.
    _nb, _lb = newton(2.0)
    _nbs, _ = newton(2.0, thieu_abs=True)
    assert _lb == 5, f"ca bien phai 5 luot, nhan duoc {_lb}"
    assert abs(_nbs - 2.0945681211) < 1e-9, "ban loi cho 2,0945681211"
    assert abs(_nbs - _nb) < 1e-4, \
        "hai ban trung nhau toi bon chu so thap phan"

    # Ca không hợp lệ: đạo hàm bằng 0 phải bị chặn thành ValueError
    # có thông điệp rõ, không để ZeroDivisionError nổ ra.
    _da_chan = False
    try:
        newton(X0_DAO_HAM_BANG_0)
    except ValueError as _loi:
        _da_chan = "dao ham bang 0" in str(_loi)
    assert _da_chan, "dao ham bang 0 phai bi chan ro rang"

    print()
    print("Moi khang dinh dat.")
