# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.9
Chương, mục : Chương 6, cả bốn tiểu mục
Đề bài      : Kiểm tra đầy đủ một chương trình do công cụ AI sinh
              giải bài toán tìm nghiệm phương trình: đặc tả, bộ ca
              thiết kế trước, bốn cách kiểm, năm bước gỡ từng lỗi,
              bắt ngoại lệ, và bản khai báo việc dùng AI.
Đầu vào     : chương trình do AI sinh, và tệp 04_DuLieu/doan_a6.txt
Đầu ra      : bảng đặc tả, bảng ca, bảng bốn cách kiểm, chương
              trình đã sửa, và bản khai báo ba thành phần
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math
from pathlib import Path

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200
GOC = Path(__file__).resolve().parents[2]
TEP_DOAN = GOC / "04_DuLieu" / "doan_a6.txt"
# Hệ số nới đoạn mà bản AI sinh dùng, không kèm nguồn nào.
HE_SO_NOI_KHONG_NGUON = 1.2


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


# ---- Bước 1: bảng đặc tả ba phần, lập trước khi đọc mã ----
DAC_TA = (
    ("Dau vao", "hai can a < b cua doan, doc tu tep van ban"),
    ("Xu ly", "kiem doan hop le va kiem f(a)*f(b) < 0, roi chia "
              "doi toi khi be rong doan nho hon sai so"),
    ("Dau ra", "(nghiem, so luot lap); phat sinh ValueError khi "
               "doan khong hop le hoac ham khong doi dau"),
)


# ---- Bản do công cụ AI sinh, giữ nguyên để kiểm ----
def nghiem_ai(ham, a, b):
    """Ban do AI sinh. Chua kiem dieu kien ap dung."""
    b = b * HE_SO_NOI_KHONG_NGUON
    so_luot = 0
    while b - a > SAI_SO and so_luot < SO_LAN_TOI_DA:
        giua = (a + b) / 2.0
        if ham(a) * ham(giua) < 0.0:
            b = giua
        else:
            a = giua
        so_luot = so_luot + 1
    return (a + b) / 2.0, so_luot


# ---- Bản đã sửa, có chặn và có bắt ngoại lệ ----
def nghiem(ham, a, b):
    """Nghiem tren doan [a, b]. Tra ve (nghiem, so luot)."""
    if a >= b:
        raise ValueError(f"can duoi {a} khong nho hon can tren {b}")
    f_a = ham(a)
    f_b = ham(b)
    if f_a == 0.0:
        return a, 0
    if f_b == 0.0:
        return b, 0
    if f_a * f_b > 0.0:
        raise ValueError(f"ham khong doi dau tren [{a}, {b}]")
    so_luot = 0
    while b - a > SAI_SO and so_luot < SO_LAN_TOI_DA:
        giua = (a + b) / 2.0
        f_giua = ham(giua)
        so_luot = so_luot + 1
        if f_giua == 0.0:
            return giua, so_luot
        if f_a * f_giua < 0.0:
            b = giua
        else:
            a = giua
            f_a = f_giua
    return (a + b) / 2.0, so_luot


def doc_doan(duong_dan):
    """Doc hai can tu tep. Bat ngoai le ngoai vong lap doc dong."""
    try:
        noi_dung = Path(duong_dan).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ValueError(f"khong co tep {duong_dan}")
    cac_o = noi_dung.split()
    if len(cac_o) < 2:
        raise ValueError("tep phai co hai so")
    try:
        return float(cac_o[0]), float(cac_o[1])
    except ValueError:
        raise ValueError(f"hai o dau khong phai so: {cac_o[:2]}")


# ---- Bộ ca thiết kế trước, kết quả mong đợi từ nguồn độc lập ----
# Nguồn: Newton, một phương pháp khác hẳn phép chia đôi.
def newton(x0):
    """Nguon doc lap cho ket qua mong doi."""
    x = x0
    for _ in range(SO_LAN_TOI_DA):
        d = 3.0 * x ** 2 - 2.0
        x_moi = x - f(x) / d
        if abs(x_moi - x) <= SAI_SO:
            return x_moi
        x = x_moi
    raise ValueError("khong hoi tu")


NGHIEM_DOC_LAP = newton(3.0)


def bo_ca(ham_nghiem):
    """Bo ca thiet ke truoc, bon ca tu bang dac ta."""
    # Ca thường: đoạn [2, 3], đổi dấu.
    gia_tri, _ = ham_nghiem(f, 2.0, 3.0)
    assert abs(gia_tri - NGHIEM_DOC_LAP) < 1e-8, "nghiem sai"

    # Ca biên: nghiệm nằm đúng tại cận dưới.
    gia_tri, so_luot = ham_nghiem(lambda x: x - 2.0, 2.0, 3.0)
    assert gia_tri == 2.0 and so_luot == 0, "ca tai moc sai"

    # Ca không hợp lệ: đoạn không đổi dấu, phải ValueError.
    try:
        ham_nghiem(f, 0.0, 1.0)
        raise AssertionError("phai bao doan khong doi dau")
    except ValueError:
        pass

    # Ca không hợp lệ: hai cận viết ngược, phải ValueError.
    try:
        ham_nghiem(f, 3.0, 2.0)
        raise AssertionError("phai bao can nguoc")
    except ValueError:
        pass


def chay(ham_nghiem):
    """Tra ve True khi bo ca bat duoc loi cua ham."""
    try:
        bo_ca(ham_nghiem)
    except AssertionError:
        return True
    return False


# ---- Bốn cách kiểm của Mục 6.4.1, áp lên bản AI sinh ----
def bon_cach_kiem():
    """Tra ve tu dien ten cach kiem -> co bat duoc loi hay khong."""
    mot_ca = abs(nghiem_ai(f, 2.0, 3.0)[0] - NGHIEM_DOC_LAP) > 1e-8
    ket_qua = {"C1 mot ca thuong": mot_ca}
    try:
        nghiem_ai(f, 0.0, 1.0)
        ba_loai = True
    except ValueError:
        ba_loai = False
    ket_qua["C2 ba loai ca"] = ba_loai or mot_ca
    ket_qua["C3 thiet ke truoc"] = chay(nghiem_ai)
    # Hệ số 1,2 không kèm nguồn nào, nên chỉ cách soát bắt được.
    ket_qua["C4 soat nguon hang so"] = True
    return ket_qua


KHAI_BAO = (
    ("1. Cong cu va phien ban",
     "mot cong cu sinh ma, phien ban ghi theo ngay dung"),
    ("2. Phan nao do no sinh",
     "ham nghiem_ai, toan bo"),
    ("3. Da kiem bang gi",
     "bo bon ca thiet ke truoc o ham bo_ca, cong bon cach kiem "
     "cua Muc 6.4.1; da soat nguon he so 1,2 va khong tim thay"),
)


def in_ket_qua():
    """In bang dac ta, bang bon cach kiem va ban khai bao."""
    for phan, noi_dung in DAC_TA:
        print(f"{phan:<8}: {noi_dung}")
    print()
    for ten, bat_duoc in bon_cach_kiem().items():
        co = "bat duoc" if bat_duoc else "khong"
        print(f"{ten:<22}: {co}")
    print()
    gia_tri, so_luot = nghiem(f, 2.0, 3.0)
    print(f"Ban da sua : {gia_tri:.10f} sau {so_luot} luot")
    print(f"Nguon doc lap (Newton): {NGHIEM_DOC_LAP:.10f}")
    print()
    for phan, noi_dung in KHAI_BAO:
        print(f"{phan:<26}: {noi_dung}")


if __name__ == "__main__":
    in_ket_qua()

    # Bản đã sửa đạt cả bốn ca của bộ ca thiết kế trước.
    assert not chay(nghiem), "ban da sua phai dat bo ca"

    # Bản AI sinh không đạt bộ ca thiết kế trước.
    assert chay(nghiem_ai), "bo ca phai bat duoc ban AI sinh"

    # Nhưng một ca thường **không** bắt được nó: hệ số nới 1,2 đưa
    # cận trên từ 3,0 lên 3,6, mà đoạn [2,0; 3,6] vẫn chứa nghiệm
    # và vẫn đổi dấu, nên phép chia đôi hội tụ về đúng nghiệm ấy.
    # Đúng kết quả đã đo của Mục 6.4.1: C1 bắt được 0 nhóm.
    _bon = bon_cach_kiem()
    assert not _bon["C1 mot ca thuong"], \
        "mot ca thuong khong bat duoc ban AI sinh"
    assert all(co for ten, co in _bon.items()
               if ten != "C1 mot ca thuong"), \
        "ba cach con lai deu phai bat duoc"

    # Tệp đoạn của đề bài đọc được và cho đúng hai cận.
    assert doc_doan(TEP_DOAN) == (2.0, 3.0), "doc tep doan sai"

    # Bản đã sửa cho cùng nghiệm với một phương pháp khác hẳn.
    assert math.isclose(nghiem(f, 2.0, 3.0)[0], NGHIEM_DOC_LAP,
                        abs_tol=1e-8), "hai phuong phap phai trung"

    # Tên tệp không có bị chặn thành ValueError có thông điệp rõ,
    # không để FileNotFoundError nổ ra giữa chương trình.
    _da_chan = False
    try:
        doc_doan(GOC / "04_DuLieu" / "khong_he_co.txt")
    except ValueError as _loi:
        _da_chan = "khong co tep" in str(_loi)
    assert _da_chan, "ten tep khong co phai bi chan"

    # Bản khai báo đủ ba thành phần.
    assert len(KHAI_BAO) == 3, "ban khai bao phai du ba thanh phan"

    print()
    print("Moi khang dinh dat.")
