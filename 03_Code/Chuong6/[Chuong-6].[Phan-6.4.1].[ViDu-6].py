# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.6
Chương, mục : Chương 6, Mục 6.4.1
Đề bài      : Bốn đoạn mã do công cụ AI sinh, mỗi đoạn một nhóm lỗi,
              đem kiểm bằng bốn cách. In bảng bốn nhân bốn cho thấy
              cách nào bắt được nhóm nào.
Đầu vào     : không có
Đầu ra      : bảng bốn nhóm lỗi nhân bốn cách kiểm
Python      : 3.12
Thư viện    : NumPy 2.1.3, qua module thu_vien_ai
Cài đặt     : pip install -r 03_Code/requirements.txt
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import thu_vien_ai  # noqa: E402

SAI_SO = 1e-10
SO_LAN_TOI_DA = 200
HE_SO_NHANH_AI = 2.0
HE_SO_NHANH_KHAC = 1.5


def f(x):
    """Ham cua bai toan A6."""
    return x ** 3 - 2.0 * x - 5.0


def chia_doi_dung(a, b):
    """Nghiem bang phep chia doi, dung lam nguon doc lap."""
    while b - a > SAI_SO:
        giua = (a + b) / 2.0
        if f(a) * f(giua) < 0.0:
            b = giua
        else:
            a = giua
    return (a + b) / 2.0


NGHIEM_DOC_LAP = chia_doi_dung(2.0, 3.0)


# --- in-sach ---
def chia_doi_ai(ham, a, b):
    """Nhom 1: thieu dieu kien ap dung f(a)*f(b) < 0."""
    so_luot = 0
    while b - a > SAI_SO and so_luot < SO_LAN_TOI_DA:
        giua = (a + b) / 2.0
        if ham(a) * ham(giua) < 0.0:
            b = giua
        else:
            a = giua
        so_luot = so_luot + 1
    return (a + b) / 2.0


def khau_hao_ai(nguyen_gia, so_nam):
    """Nhom 3: phep chia nguyen cho cho can phep chia thuc."""
    moi_nam = nguyen_gia // so_nam
    return [nguyen_gia - moi_nam * (nam + 1)
            for nam in range(so_nam)]


# --- het-in-sach ---


def khau_hao_nhanh_ai(nguyen_gia, so_nam, he_so=HE_SO_NHANH_AI):
    """Nhom 4: he so 2,0 'theo quy dinh', khong ghi so hieu nao."""
    con_lai = nguyen_gia
    cac_nam = []
    for _ in range(so_nam):
        muc = min(con_lai * he_so / so_nam, con_lai)
        con_lai = con_lai - muc
        cac_nam.append(con_lai)
    return cac_nam


def khau_hao_dung(nguyen_gia, so_nam):
    """Ban dung cua nhom 3: phep chia thuc."""
    moi_nam = nguyen_gia / so_nam
    return [nguyen_gia - moi_nam * (nam + 1)
            for nam in range(so_nam)]


def bon_tinh_chat(bang):
    """Bon tinh chat suy duoc tu dac ta cua bang khau hao."""
    if not bang:
        return False
    giam_dan = all(bang[i] >= bang[i + 1]
                   for i in range(len(bang) - 1))
    khong_am = all(gia_tri >= -1e-9 for gia_tri in bang)
    return giam_dan and khong_am and bang[-1] <= bang[0]


def c1_mot_ca_thuong():
    """Cach 1: mot ca thuong, ket qua mong doi tinh doc lap."""
    return {
        "nhom1": abs(chia_doi_ai(f, 2.0, 3.0)
                     - NGHIEM_DOC_LAP) > 1e-8,
        "nhom2": (thu_vien_ai.dien_tich_ten_cu([0.0, 1.0, 2.0])
                  != thu_vien_ai.dien_tich_ten_moi([0.0, 1.0, 2.0])),
        "nhom3": khau_hao_ai(100000.0, 10)
                 != khau_hao_dung(100000.0, 10),
        "nhom4": not bon_tinh_chat(khau_hao_nhanh_ai(100000.0, 10)),
    }


def c2_ba_loai_ca():
    """Cach 2: them ca bien va ca du lieu khong hop le."""
    ket_qua = dict(c1_mot_ca_thuong())
    # Ca không hợp lệ cho nhóm 1: đoạn [0, 1] không đổi dấu, nên
    # theo đặc tả hàm phải báo không tính được.
    if abs(chia_doi_ai(f, 0.0, 1.0)) < 1e9:
        ket_qua["nhom1"] = True
    # Ca biên cho nhóm 3: nguyên giá không chia hết cho số năm.
    if khau_hao_ai(100000.0, 7) != khau_hao_dung(100000.0, 7):
        ket_qua["nhom3"] = True
    # Ca biên cho nhóm 4: một năm duy nhất.
    if not bon_tinh_chat(khau_hao_nhanh_ai(100000.0, 1)):
        ket_qua["nhom4"] = True
    return ket_qua


def c3_thiet_ke_truoc():
    """Cach 3: them ca tai moc va ca nhich qua moc."""
    ket_qua = dict(c2_ba_loai_ca())
    if abs(chia_doi_ai(lambda x: x - 2.0, 2.0, 3.0) - 2.0) > 1e-8:
        ket_qua["nhom1"] = True
    for so_nam in (1, 2, 3):
        if (khau_hao_ai(100000.0, so_nam)
                != khau_hao_dung(100000.0, so_nam)):
            ket_qua["nhom3"] = True
    return ket_qua


def c4_soat_phien_ban_va_nguon():
    """Cach 4: soat ten ham thu vien va nguon hang so, khong chay.

    Doi chieu moi ten ham thu vien voi tai lieu cua phien ban ghim,
    va moi hang so voi mot nguon co so hieu. Hai dong True duoi day
    la ket qua cua viec doi chieu do, khong phai ket qua chay ma.
    """
    return {"nhom1": False, "nhom2": True,
            "nhom3": False, "nhom4": True}


def hai_he_so_co_phan_biet_duoc():
    """Dem so quy mo ma bon tinh chat phan biet duoc hai he so."""
    cac_quy_mo = ((100000.0, 10), (100000.0, 1), (100000.0, 7),
                  (1.0, 3), (1e9, 20))
    phan_biet = 0
    for nguyen_gia, so_nam in cac_quy_mo:
        a = bon_tinh_chat(khau_hao_nhanh_ai(
            nguyen_gia, so_nam, HE_SO_NHANH_AI))
        b = bon_tinh_chat(khau_hao_nhanh_ai(
            nguyen_gia, so_nam, HE_SO_NHANH_KHAC))
        if a != b:
            phan_biet = phan_biet + 1
    return len(cac_quy_mo), phan_biet


CAC_CACH = (
    ("C1 mot ca thuong   ", c1_mot_ca_thuong()),
    ("C2 ba loai ca      ", c2_ba_loai_ca()),
    ("C3 thiet ke truoc  ", c3_thiet_ke_truoc()),
    ("C4 soat phien ban  ", c4_soat_phien_ban_va_nguon()),
)
CAC_NHOM = ("nhom1", "nhom2", "nhom3", "nhom4")

print("Cach kiem           | nhom1 | nhom2 | nhom3 | nhom4 | Tong")
for _ten, _kq in CAC_CACH:
    _cot = " | ".join(f"{'co' if _kq[n] else 'khong':<5}"
                      for n in CAC_NHOM)
    print(f"{_ten} | {_cot} | {sum(_kq.values())}/4")

SO_QUY_MO, SO_PHAN_BIET = hai_he_so_co_phan_biet_duoc()
print()
print(f"Nhom 4: thu {SO_QUY_MO} quy mo du lieu, so quy mo ma bon "
      f"tinh chat")
print(f"        phan biet duoc he so 2,0 voi he so 1,5: "
      f"{SO_PHAN_BIET}")
print(f"        con lai cuoi ky he so 2,0 : "
      f"{khau_hao_nhanh_ai(100000.0, 10)[-1]:.2f}")
print(f"        con lai cuoi ky he so 1,5 : "
      f"{khau_hao_nhanh_ai(100000.0, 10, HE_SO_NHANH_KHAC)[-1]:.2f}")

if __name__ == "__main__":
    _chay_ma = set()
    for _ten, _kq in CAC_CACH[:3]:
        _chay_ma |= {n for n in CAC_NHOM if _kq[n]}

    # Ba cách chạy mã cộng lại bắt được đúng hai nhóm.
    assert len(_chay_ma) == 2, "ba cach chay ma phai bat duoc 2 nhom"

    # Một ca thường duy nhất không bắt được nhóm nào.
    assert sum(CAC_CACH[0][1].values()) == 0, \
        "mot ca thuong khong bat duoc nhom nao"

    # Hai nhóm còn lại chỉ cách không chạy mã bắt được.
    _c4 = {n for n in CAC_NHOM if CAC_CACH[3][1][n]}
    assert _c4 & _chay_ma == set(), \
        "hai cach phai bat hai nhom khac nhau"

    # Không quy mô nào phân biệt được hai hệ số của nhóm 4.
    assert SO_PHAN_BIET == 0, "khong quy mo nao phan biet duoc"

    print()
    print("Moi khang dinh dat.")
