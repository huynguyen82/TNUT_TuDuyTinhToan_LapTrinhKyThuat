# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 6
Chương, mục : Chương 5, Mục 5.4.1
Đề bài      : Mảng NumPy cho chuỗi số đo một ngày, và đồ thị
              nồng độ theo giờ có tên trục, đơn vị, chú giải và
              đường ngưỡng.
Đầu vào     : 04_DuLieu/pm25_ngay.txt
Đầu ra      : 02_GiaoTrinh/Hinh/Hinh_5_4.png và vài dòng số
Python      : 3.12
Thư viện    : numpy==2.1.3, matplotlib==3.9.2
Cài đặt     : pip install numpy==2.1.3 matplotlib==3.9.2
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

GOC = Path(__file__).resolve().parents[2]
TEP_VAO = GOC / "04_DuLieu" / "pm25_ngay.txt"
THU_MUC_HINH = GOC / "02_GiaoTrinh" / "Hinh"
NGUONG = 50.0


def doc_so_do(duong_dan):
    """Đọc mỗi dòng của tệp thành một số thực."""
    day = []
    with open(duong_dan, encoding="utf-8") as tep:
        for dong in tep:
            day.append(float(dong.strip()))
    return day


# --- in-sach ---
def ve_do_thi(gio, nong_do, nguong, duong_dan):
    """Ve do thi nong do theo gio, co ten truc va don vi."""
    hinh, truc = plt.subplots(figsize=(6.0, 3.2))
    truc.plot(gio, nong_do, marker="o", markersize=3,
              color="black", label="PM2.5 do duoc")
    truc.axhline(nguong, color="black", linestyle="--",
                 linewidth=1.0,
                 label=f"Nguong canh bao {nguong:.0f}")
    truc.set_xlabel("Gio trong ngay (h)")
    truc.set_ylabel("Nong do PM2.5 (microgram/m3)")
    truc.set_xticks(range(0, 24, 3))
    truc.legend(loc="upper left", fontsize=8)
    truc.grid(True, linewidth=0.3)
    hinh.savefig(duong_dan, dpi=300, bbox_inches="tight")
    plt.close(hinh)
    return duong_dan


mang = np.array(doc_so_do(TEP_VAO))
print(f"so phan tu     : {mang.size}")
print(f"trung binh     : {np.mean(mang):.2f}")
print(f"cao nhat       : {np.max(mang):.1f}")
print(f"so gio vuot    : {int(np.sum(mang > NGUONG))}")
print(f"nhan ca mang   : {(mang * 1.5)[8]:.2f}")
# --- het-in-sach ---


if __name__ == "__main__":
    THU_MUC_HINH.mkdir(parents=True, exist_ok=True)
    duong_dan = ve_do_thi(list(range(24)), mang, NGUONG,
                          THU_MUC_HINH / "Hinh_5_4.png")

    # --- Trường hợp thường -------------------------------------
    assert mang.size == 24
    assert f"{np.mean(mang):.4f}" == "43.6667"
    assert np.max(mang) == 71.5
    assert int(np.sum(mang > NGUONG)) == 7
    # NumPy cho cung ket qua voi ham co san cua Python.
    assert float(np.mean(mang)) == sum(mang.tolist()) / 24
    # Hinh da ve va du lon.
    assert duong_dan.exists()
    assert duong_dan.stat().st_size > 10_000

    # --- Trường hợp biên ---------------------------------------
    # Hinh hep hon be ngang vung chu cua kho A4.
    from PIL import Image

    with Image.open(duong_dan) as anh:
        assert anh.size[0] / 300.0 < 6.3, anh.size
    # So do dung bang nguong KHONG dem la vuot.
    assert int(np.sum(np.array([NGUONG]) > NGUONG)) == 0
    # Mang rong: size bang 0, va mean bao canh bao chu khong loi.
    assert np.array([]).size == 0
    # numpy.trapezoid trung voi vong lap hinh thang tu viet.
    x = np.arange(24.0)
    tu_viet = 0.0
    for thu_tu in range(23):
        tu_viet = tu_viet + (mang[thu_tu] + mang[thu_tu + 1]) / 2
    assert float(np.trapezoid(mang, x)) == tu_viet

    # --- Trường hợp ngoại lệ -----------------------------------
    # Cong hai mang khac do dai bao loi ve hinh dang.
    da_chan = False
    try:
        np.array([1.0, 2.0, 3.0]) + np.array([1.0, 2.0])
    except ValueError:
        da_chan = True
    assert da_chan, "hai mang khac do dai ma cong duoc"
    # mean tren mang con so do loi am cho ket qua SAI, khong bao gi.
    co_loi = np.array([45.0, -5.0, 72.5])
    assert float(np.mean(co_loi)) == 37.5
    assert float(np.mean(co_loi[co_loi > 0])) == 58.75

    print(f"da ve {duong_dan.name}: "
          f"{duong_dan.stat().st_size // 1024} kB")
    print(f"numpy {np.__version__}, "
          f"matplotlib {matplotlib.__version__}")
