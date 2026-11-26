# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.7
Chương, mục : Chương 5, Mục 5.3.2
Đề bài      : Xử lý tệp 720 dòng theo cả ba cách xử lý ô trống,
              lập bảng ba giá trị trung bình, và nêu cách nào
              nên dùng.
Đầu vào     : 04_DuLieu/pm25_thang.csv
Đầu ra      : ba giá trị trung bình và ba số dòng bỏ qua
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

from pathlib import Path

GOC = Path(__file__).resolve().parents[2]
TEP_VAO = GOC / "04_DuLieu" / "pm25_thang.csv"
SO_COT = 3
NGUONG = 50.0


def doc_bang(duong_dan):
    """Đọc tệp bảng, trả về dãy và ba số đếm dòng bỏ qua.

    Ô trống và dòng hỏng đều cho None trong dãy, để ba cách xử
    lý sau đó biết chỗ nào thiếu số đo.
    """
    day = []
    thieu_cot = 0
    khong_phai_so = 0
    o_trong = 0
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()
        for dong in tep:
            o = dong.strip().split(",")
            if len(o) < SO_COT:
                thieu_cot = thieu_cot + 1
                day.append(None)
            elif o[2] == "":
                o_trong = o_trong + 1
                day.append(None)
            else:
                try:
                    day.append(float(o[2]))
                except ValueError:
                    khong_phai_so = khong_phai_so + 1
                    day.append(None)
    return day, thieu_cot, khong_phai_so, o_trong


def cach_bo_dong(day):
    """Cách 1: bỏ mọi chỗ thiếu số đo."""
    sach = []
    for gia_tri in day:
        if gia_tri is not None:
            sach.append(gia_tri)
    if len(sach) == 0:
        raise ValueError("du lieu khong hop le: khong con dong nao")
    return sum(sach) / len(sach), len(sach)


def cach_dien_truoc(day):
    """Cách 2: điền giá trị của giờ liền trước.

    Chỗ thiếu ở đầu dãy không có giá trị nào để điền, nên bị bỏ.
    """
    sach = []
    truoc = None
    for gia_tri in day:
        if gia_tri is None:
            if truoc is not None:
                sach.append(truoc)
        else:
            sach.append(gia_tri)
            truoc = gia_tri
    if len(sach) == 0:
        raise ValueError("du lieu khong hop le: khong con dong nao")
    return sum(sach) / len(sach), len(sach)


def gia_tri_ke(day, thu_tu):
    """Giá trị gần nhất trước và sau một vị trí, hoặc None."""
    truoc = None
    sau = None
    for lui in range(thu_tu - 1, -1, -1):
        if day[lui] is not None:
            truoc = day[lui]
            break
    for tien in range(thu_tu + 1, len(day)):
        if day[tien] is not None:
            sau = day[tien]
            break
    return truoc, sau


def cach_noi_suy(day):
    """Cách 3: nội suy trung bình hai giá trị kề."""
    sach = []
    for thu_tu in range(len(day)):
        gia_tri = day[thu_tu]
        if gia_tri is not None:
            sach.append(gia_tri)
            continue
        truoc, sau = gia_tri_ke(day, thu_tu)
        if truoc is not None and sau is not None:
            sach.append((truoc + sau) / 2)
        elif truoc is not None:
            sach.append(truoc)
        elif sau is not None:
            sach.append(sau)
    if len(sach) == 0:
        raise ValueError("du lieu khong hop le: khong con dong nao")
    return sum(sach) / len(sach), len(sach)


def cach_coi_la_0(day):
    """Cách KHÔNG được dùng: coi chỗ thiếu là số 0."""
    sach = []
    for gia_tri in day:
        sach.append(0.0 if gia_tri is None else gia_tri)
    return sum(sach) / len(sach), len(sach)


if __name__ == "__main__":
    day, thieu_cot, khong_phai_so, o_trong = doc_bang(TEP_VAO)
    bo_qua = thieu_cot + khong_phai_so + o_trong
    tb_bo, n_bo = cach_bo_dong(day)
    tb_dien, n_dien = cach_dien_truoc(day)
    tb_noi, n_noi = cach_noi_suy(day)

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 720
    assert (thieu_cot, khong_phai_so, o_trong) == (1, 1, 3)
    assert bo_qua == 5
    assert (f"{tb_bo:.4f}", n_bo) == ("49.4964", 715)
    assert (f"{tb_dien:.4f}", n_dien) == ("49.4764", 720)
    assert (f"{tb_noi:.4f}", n_noi) == ("49.4708", 720)

    # --- Trường hợp biên ---------------------------------------
    # Ba cach cho ba so KHAC nhau, chenh lech lon nhat 0,05 %.
    assert tb_bo != tb_dien != tb_noi
    chenh = (max(tb_bo, tb_dien, tb_noi)
             - min(tb_bo, tb_dien, tb_noi))
    assert f"{chenh:.3f}" == "0.026"
    assert chenh / tb_bo < 0.001
    # Nhung ca ba deu SAT DUOI nguong 50, trong khoang 49,47 den 49,50.
    for tb in (tb_bo, tb_dien, tb_noi):
        assert 49.47 < tb < NGUONG
    # O trong o dong DAU tien: cach dien truoc khong co gi de dien,
    # nen no bo dong do, va KHONG bao loi.
    dau_trong = [None] + day[1:]
    assert cach_dien_truoc(dau_trong)[1] == 719
    assert cach_noi_suy(dau_trong)[1] == 720

    # --- Trường hợp ngoại lệ -----------------------------------
    # Coi o trong la 0 keo trung binh xuong DUOI ca ba gia tri tren,
    # va khong bao gi: day la cach khong duoc dung.
    tb_0, n_0 = cach_coi_la_0(day)
    assert tb_0 < min(tb_bo, tb_dien, tb_noi)
    assert n_0 == 720
    # Day khong con dong nao dung duoc: ca ba cach bao ValueError.
    da_chan = 0
    for ham in (cach_bo_dong, cach_dien_truoc, cach_noi_suy):
        try:
            ham([None, None])
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 3, "co cach khong chan day toan None"

    print(f"dong du lieu       : {len(day)}")
    print(f"bo qua             : {bo_qua} "
          f"({thieu_cot} thieu cot, {khong_phai_so} ghi chu, "
          f"{o_trong} o trong)")
    print()
    print("cach xu ly      n     trung binh")
    print(f"bo dong      {n_bo:>5}     {tb_bo:.4f}")
    print(f"dien truoc   {n_dien:>5}     {tb_dien:.4f}")
    print(f"noi suy      {n_noi:>5}     {tb_noi:.4f}")
    print(f"coi la 0     {n_0:>5}     {tb_0:.4f}  <- khong dung")
