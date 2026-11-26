# -*- coding: utf-8 -*-
"""
Mã bài      : GL 5
Chương, mục : Chương 5, Bài gỡ lỗi GL5
Đề bài      : Chương trình 23 dòng đọc tệp số đo một ngày rồi tính
              nồng độ trung bình và số giờ vượt ngưỡng, chứa đúng
              ba lỗi: một cú pháp, một thực thi, một logic.
Đầu vào     : tệp 04_DuLieu/pm25_ngay.txt, 24 dòng
Đầu ra      : nồng độ trung bình và số giờ vượt ngưỡng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

from pathlib import Path

NGUONG = 50.0
GOC = Path(__file__).resolve().parents[2]
TEP_NGAY = GOC / "04_DuLieu" / "pm25_ngay.txt"

BA_LOI = (
    (3, "cu phap", "def doc_so_do(duong_dan) khong co dau hai cham",
     "SyntaxError: expected ':'",
     "them dau hai cham cuoi dong def"),
    (12, "thuc thi",
     "doc_so_do('pm25_ngay.txt') dung duong dan tuong doi",
     "FileNotFoundError khi chay tu mot thu muc khac",
     "dung duong dan dung tu vi tri tep ma nguon, qua __file__"),
    (16, "logic", "for chi_so in range(1, len(ngay))",
     "khong bao gi; bo so do gio 0 ma van chia cho len(ngay), "
     "nen trung binh ra 42,37 thay vi 43,67",
     "dung range(len(ngay)), hoac duyet truc tiep for so_do in ngay"),
)


def doc_so_do(duong_dan):
    """Doc moi dong cua tep thanh mot so thuc."""
    day = []
    with open(duong_dan, encoding="utf-8") as tep:
        for dong in tep:
            day.append(float(dong.strip()))
    return day


def tinh(day, loi_dong_16=False):
    """Tra ve (trung binh, so gio vuot nguong).

    Phat sinh ValueError khi day rong, vi phep chia khong thuc
    hien duoc.
    """
    if not day:
        raise ValueError("day rong, khong tinh duoc trung binh")
    bat_dau = 1 if loi_dong_16 else 0
    tong = 0.0
    vuot = 0
    for chi_so in range(bat_dau, len(day)):
        so_do = day[chi_so]
        tong = tong + so_do
        if so_do > NGUONG:
            vuot = vuot + 1
    # Lỗi dòng 16 nằm ở đây: mẫu số vẫn là cả dãy dù đã bỏ một số.
    return tong / len(day), vuot


def in_ket_qua():
    """In bang ba loi va ket qua hai ban tren tep that."""
    print("Dong | Loai     | Bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    ngay = doc_so_do(TEP_NGAY)
    tb_dung, vuot_dung = tinh(ngay)
    tb_sai, vuot_sai = tinh(ngay, loi_dong_16=True)
    print(f"Tep {TEP_NGAY.name}, {len(ngay)} dong")
    print(f"  Ban da sua : trung binh {tb_dung:.2f}, "
          f"{vuot_dung} gio vuot nguong")
    print(f"  Ban con loi: trung binh {tb_sai:.2f}, "
          f"{vuot_sai} gio vuot nguong")


if __name__ == "__main__":
    in_ket_qua()

    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    _ngay = doc_so_do(TEP_NGAY)
    assert len(_ngay) == 24, "tep mot ngay phai co 24 dong"

    # Ca thường: trung bình 43,67 và 7 giờ vượt ngưỡng.
    _tb, _vuot = tinh(_ngay)
    assert abs(_tb - 43.67) < 0.01, \
        f"trung binh phai 43,67, nhan duoc {_tb:.2f}"
    assert _vuot == 7, f"phai 7 gio vuot, nhan duoc {_vuot}"

    # Bản lỗi dòng 16 cho 42,37 — lệch 1,3 trên 43,67, tức 3 %.
    # Số giờ vượt vẫn đúng 7, nên **chỉ một trong hai** con số
    # bộc lộ lỗi. Đây là lý do báo cáo phải in cả hai.
    _tb2, _vuot2 = tinh(_ngay, loi_dong_16=True)
    assert abs(_tb2 - 42.37) < 0.01, \
        f"ban loi phai cho 42,37, nhan duoc {_tb2:.2f}"
    assert _vuot2 == _vuot, "so gio vuot cua hai ban van bang nhau"

    # Ca biên: tệp một dòng. Bản lỗi bỏ đúng dòng duy nhất nên cho
    # 0,0 — ca bộc lộ lỗi rõ nhất.
    assert tinh([42.0])[0] == 42.0, "mot dong cho chinh so do do"
    assert tinh([42.0], loi_dong_16=True)[0] == 0.0, \
        "ban loi cho 0,0 voi tep mot dong"

    # Ca không hợp lệ: dãy rỗng bị chặn trước phép chia.
    _da_chan = False
    try:
        tinh([])
    except ValueError:
        _da_chan = True
    assert _da_chan, "day rong phai bi chan truoc phep chia"

    print()
    print("Moi khang dinh dat.")
