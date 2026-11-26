# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.6
Chương, mục : Chương 5, Mục 5.4.1
Đề bài      : Vẽ đồ thị PM2.5 theo giờ đủ năm phép bắt buộc, rồi
              vẽ lại bản thiếu tên trục để so.
Đầu vào     : 04_DuLieu/pm25_ngay.txt
Đầu ra      : hai tệp hình trong 04_DuLieu
Python      : 3.12
Thư viện    : matplotlib==3.9.2
Cài đặt     : pip install matplotlib==3.9.2

Lời giải trình bày ở tệp .md cùng tên. Hai hình của bài này
không in vào giáo trình; Hình 5.4 mới là hình in.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

GOC = Path(__file__).resolve().parents[2]
THU_MUC = GOC / "04_DuLieu"
TEP_VAO = THU_MUC / "pm25_ngay.txt"
TEP_DU = THU_MUC / "bt56_du_nam_phep.png"
TEP_THIEU = THU_MUC / "bt56_thieu_ten_truc.png"
NGUONG = 50.0


def doc_so_do(duong_dan):
    """Đọc mỗi dòng của tệp thành một số thực."""
    day = []
    with open(duong_dan, encoding="utf-8") as tep:
        for dong in tep:
            day.append(float(dong.strip()))
    return day


def ve_du_nam_phep(day, duong_dan):
    """Vẽ đủ năm phép bắt buộc của Khối 4 Mục 5.4.1."""
    hinh, truc = plt.subplots(figsize=(6.0, 3.2))
    truc.plot(range(len(day)), day, marker="o", markersize=3,
              color="black", label="PM2.5 do duoc")
    truc.axhline(NGUONG, color="black", linestyle="--",
                 linewidth=1.0,
                 label=f"Nguong canh bao {NGUONG:.0f}")
    truc.set_xlabel("Gio trong ngay (h)")
    truc.set_ylabel("Nong do PM2.5 (microgram/m3)")
    truc.legend(loc="upper left", fontsize=8)
    hinh.savefig(duong_dan, dpi=300, bbox_inches="tight")
    plt.close(hinh)
    return duong_dan


def ve_thieu_ten_truc(day, duong_dan):
    """Bản SAI: bỏ set_xlabel, set_ylabel và legend."""
    hinh, truc = plt.subplots(figsize=(6.0, 3.2))
    truc.plot(range(len(day)), day, marker="o", markersize=3,
              color="black")
    truc.axhline(NGUONG, color="black", linestyle="--",
                 linewidth=1.0)
    hinh.savefig(duong_dan, dpi=300, bbox_inches="tight")
    plt.close(hinh)
    return duong_dan


def so_phep_bat_buoc_thieu(truc_co_ten_x, truc_co_ten_y,
                           co_chu_giai):
    """Số phép bắt buộc còn thiếu trong năm phép."""
    thieu = 0
    for co in (truc_co_ten_x, truc_co_ten_y, co_chu_giai):
        if not co:
            thieu = thieu + 1
    return thieu


if __name__ == "__main__":
    day = doc_so_do(TEP_VAO)
    du = ve_du_nam_phep(day, TEP_DU)
    thieu = ve_thieu_ten_truc(day, TEP_THIEU)

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 24
    assert du.exists() and thieu.exists()
    assert du.stat().st_size > 10_000, du.stat().st_size
    # Ban du nam phep lon hon ban thieu, vi no co them chu.
    assert du.stat().st_size > thieu.stat().st_size
    assert so_phep_bat_buoc_thieu(True, True, True) == 0

    # --- Trường hợp biên ---------------------------------------
    # Ca hai hinh hep hon be ngang vung chu cua kho A4.
    from PIL import Image

    for duong_dan in (du, thieu):
        with Image.open(duong_dan) as anh:
            assert anh.size[0] / 300.0 < 6.3, duong_dan
    # Mot so do duy nhat: hinh ve ra duoc nhung chi co mot diem.
    mot = ve_du_nam_phep([42.6], THU_MUC / "bt56_mot_diem.png")
    assert mot.exists() and mot.stat().st_size > 10_000
    mot.unlink()
    # Duong nguong nam giua cuc tri cua chuoi, nen no nhin thay duoc.
    assert min(day) < NGUONG < max(day)
    # Voi chuoi toan duoi nguong, axhline MO RONG truc doc de chua
    # duong nguong, nen chuoi so do bi ep xuong day hinh.
    hinh, truc = plt.subplots()
    truc.plot(range(5), [10.0, 12.0, 11.0, 13.0, 9.0])
    truoc = truc.get_ylim()
    truc.axhline(NGUONG)
    sau = truc.get_ylim()
    plt.close(hinh)
    assert (round(truoc[0], 2), round(truoc[1], 2)) == (8.8, 13.2)
    assert (round(sau[0], 2), round(sau[1], 2)) == (6.95, 52.05)
    assert sau[1] - sau[0] > 10 * (truoc[1] - truoc[0])

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ban thieu ten truc KHONG bao loi: hinh van ve ra.
    assert thieu.exists()
    assert so_phep_bat_buoc_thieu(False, False, False) == 3
    # Danh sach rong: ve ra mot hinh trong, cung khong bao loi.
    rong = ve_du_nam_phep([], THU_MUC / "bt56_rong.png")
    assert rong.exists()
    rong.unlink()

    print(f"du nam phep  : {du.name}, "
          f"{du.stat().st_size // 1024} kB")
    print(f"thieu ten truc: {thieu.name}, "
          f"{thieu.stat().st_size // 1024} kB")
    print(f"so phep bat buoc con thieu o ban sai: "
          f"{so_phep_bat_buoc_thieu(False, False, False)}")
    print(f"matplotlib {matplotlib.__version__}")
