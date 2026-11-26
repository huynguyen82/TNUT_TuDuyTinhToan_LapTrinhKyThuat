# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.5
Chương, mục : Chương 5, Mục 5.3.1
Đề bài      : Chuyển chương trình Bài tập 5.3 sang đọc số đo từ
              tệp và ghi báo cáo ra tệp mới; xác nhận hai lần
              chạy cho cùng kết quả.
Đầu vào     : 04_DuLieu/pm25_ngay.txt
Đầu ra      : 04_DuLieu/bao_cao_bt55.txt
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

from pathlib import Path

GOC = Path(__file__).resolve().parents[2]
THU_MUC = GOC / "04_DuLieu"
TEP_VAO = THU_MUC / "pm25_ngay.txt"
TEP_RA = THU_MUC / "bao_cao_bt55.txt"
TEP_MOT_DONG = THU_MUC / "pm25_mot_dong.txt"
NGUONG = 50.0
CAO_DIEM_SANG = (6, 9)


def doc_so_do(duong_dan):
    """Đọc mỗi dòng của tệp thành một số thực.

    Phát sinh FileNotFoundError kèm tên tệp đang tìm khi tệp
    không có trong thư mục.
    """
    if not duong_dan.exists():
        raise FileNotFoundError(
            f"khong tim thay tep: {duong_dan}")
    day = []
    with open(duong_dan, encoding="utf-8") as tep:
        for dong in tep:
            day.append(float(dong.strip()))
    return day


def nam_dai_luong(day):
    """Năm đại lượng của Bài tập 5.3, tính từ một danh sách."""
    if len(day) == 0:
        raise ValueError("du lieu khong hop le: danh sach rong")
    vuot = 0
    for so_do in day:
        if so_do > NGUONG:
            vuot = vuot + 1
    doan = day[CAO_DIEM_SANG[0]:CAO_DIEM_SANG[1]]
    if len(doan) == 0:
        doan = day
    return (day.index(max(day)), day.index(min(day)),
            sum(day) / len(day), vuot, sum(doan) / len(doan))


def ghi_bao_cao(duong_dan, day):
    """Ghi báo cáo năm dòng ra một tệp mới."""
    cao, thap, tb, vuot, cao_diem = nam_dai_luong(day)
    with open(duong_dan, "w", encoding="utf-8") as tep:
        tep.write(f"Gio cao nhat        : {cao}\n")
        tep.write(f"Gio thap nhat       : {thap}\n")
        tep.write(f"Trung binh ngay     : {tb:.2f}\n")
        tep.write(f"So gio vuot nguong  : {vuot}\n")
        tep.write(f"Trung binh cao diem : {cao_diem:.2f}\n")
    return duong_dan


if __name__ == "__main__":
    day = doc_so_do(TEP_VAO)
    ghi_bao_cao(TEP_RA, day)
    lan_mot = TEP_RA.read_text(encoding="utf-8")

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 24
    # Dap so trung Bai tap 5.3 tren cung du lieu.
    assert nam_dai_luong(day)[0] == 8
    assert nam_dai_luong(day)[1] == 3
    assert f"{nam_dai_luong(day)[2]:.2f}" == "43.67"
    assert nam_dai_luong(day)[3] == 7
    assert f"{nam_dai_luong(day)[4]:.2f}" == "60.80"
    assert "Trung binh ngay     : 43.67" in lan_mot
    assert lan_mot.count("\n") == 5

    # --- Trường hợp biên ---------------------------------------
    # Hai lan chay cho DUNG cung ket qua, tung ky tu.
    ghi_bao_cao(TEP_RA, doc_so_do(TEP_VAO))
    assert TEP_RA.read_text(encoding="utf-8") == lan_mot
    # Tep chi co mot dong: bao cao van du nam dong.
    TEP_MOT_DONG.write_text("42.6\n", encoding="utf-8")
    mot = doc_so_do(TEP_MOT_DONG)
    assert len(mot) == 1
    assert f"{nam_dai_luong(mot)[2]:.2f}" == "42.60"
    # Voi mot dong, doan cao diem rong nen lay ca danh sach.
    assert f"{nam_dai_luong(mot)[4]:.2f}" == "42.60"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ten tep khong co: thong bao phai noi ro tep dang tim.
    da_chan = False
    try:
        doc_so_do(THU_MUC / "khong_co_tep.txt")
    except FileNotFoundError as loi:
        da_chan = "khong_co_tep.txt" in str(loi)
    assert da_chan, "thong bao loi khong noi ro tep dang tim"
    # Tep rong: danh sach rong nen ham tinh phat sinh ValueError.
    tep_rong = THU_MUC / "pm25_rong.txt"
    tep_rong.write_text("", encoding="utf-8")
    da_chan2 = False
    try:
        nam_dai_luong(doc_so_do(tep_rong))
    except ValueError:
        da_chan2 = True
    assert da_chan2, "tep rong ma van tinh duoc"
    tep_rong.unlink()
    TEP_MOT_DONG.unlink()

    print(f"doc {len(day)} so do tu {TEP_VAO.name}")
    print(f"ghi bao cao ra {TEP_RA.name}")
    print(lan_mot.rstrip())
    print("hai lan chay cho dung cung ket qua: True")
