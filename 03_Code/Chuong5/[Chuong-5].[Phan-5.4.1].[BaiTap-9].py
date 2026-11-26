# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.9
Chương, mục : Chương 5, cả sáu tiểu mục
Đề bài      : Chương trình báo cáo chất lượng không khí một
              tháng: đọc tệp, xử lý dòng lỗi, tính đại lượng,
              tra mức, vẽ đồ thị, ghi báo cáo.
Đầu vào     : 04_DuLieu/pm25_thang.csv
Đầu ra      : 04_DuLieu/bao_cao_thang.txt và bt59_do_thi.png
Python      : 3.12
Thư viện    : numpy==2.1.3, matplotlib==3.9.2
Cài đặt     : pip install numpy==2.1.3 matplotlib==3.9.2

Lời giải trình bày ở tệp .md cùng tên.
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

GOC = Path(__file__).resolve().parents[2]
THU_MUC = GOC / "04_DuLieu"
TEP_VAO = THU_MUC / "pm25_thang.csv"
TEP_BAO_CAO = THU_MUC / "bao_cao_thang.txt"
TEP_HINH = THU_MUC / "bt59_do_thi.png"
SO_COT = 3
NGUONG = 50.0
CACH_XU_LY_O_TRONG = "bo dong"

CAN_DUOI = {
    "tot": 0.0,
    "trung binh": 12.1,
    "kem": 35.5,
    "xau": 55.5,
    "rat xau": 150.5,
    "nguy hai": 250.5,
}


def doc_bang(duong_dan):
    """Hàm 1: đọc tệp bảng, trả về dãy và ba số đếm dòng bỏ qua.

    Số dòng bỏ qua là một phần của kết quả, không phải thông tin
    phụ, nên hàm trả nó về cùng dữ liệu.

    Phát sinh FileNotFoundError kèm tên tệp khi tệp không có.
    """
    if not duong_dan.exists():
        raise FileNotFoundError(f"khong tim thay tep: {duong_dan}")
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
            elif o[2] == "":
                o_trong = o_trong + 1
            else:
                try:
                    day.append(float(o[2]))
                except ValueError:
                    khong_phai_so = khong_phai_so + 1
    return day, thieu_cot, khong_phai_so, o_trong


def bon_dai_luong(day, nguong=NGUONG):
    """Hàm 2: bốn đại lượng của dãy số đo.

    Phát sinh ValueError khi dãy rỗng, để phép chia không bao
    giờ gặp số 0.
    """
    if len(day) == 0:
        raise ValueError("du lieu khong hop le: khong co dong nao")
    mang = np.array(day)
    return (float(np.max(mang)), float(np.min(mang)),
            float(np.mean(mang)), int(np.sum(mang > nguong)))


def ten_muc(nong_do, bang=CAN_DUOI):
    """Hàm 3: tên mức chất lượng không khí của một nồng độ."""
    if nong_do < 0.0:
        raise ValueError(
            f"du lieu khong hop le: nong do = {nong_do}")
    ten = "tot"
    for khoa in bang:
        if nong_do >= bang[khoa]:
            ten = khoa
    return ten


def ve_do_thi(day, nguong, duong_dan):
    """Hàm 4: đồ thị nồng độ theo giờ, đủ năm phép bắt buộc."""
    hinh, truc = plt.subplots(figsize=(6.0, 3.0))
    truc.plot(range(len(day)), day, linewidth=0.6, color="black",
              label="PM2.5 do duoc")
    truc.axhline(nguong, color="black", linestyle="--",
                 linewidth=1.0,
                 label=f"Nguong canh bao {nguong:.0f}")
    truc.set_xlabel("Gio trong thang (h)")
    truc.set_ylabel("Nong do PM2.5 (microgram/m3)")
    truc.legend(loc="upper left", fontsize=8)
    hinh.savefig(duong_dan, dpi=300, bbox_inches="tight")
    plt.close(hinh)
    return duong_dan


def ghi_bao_cao(duong_dan, day, cac_dem, cach_xu_ly):
    """Hàm 5: ghi báo cáo, có cả cách xử lý và số dòng đã bỏ."""
    cao, thap, tb, vuot = bon_dai_luong(day)
    thieu_cot, khong_phai_so, o_trong = cac_dem
    bo_qua = thieu_cot + khong_phai_so + o_trong
    with open(duong_dan, "w", encoding="utf-8") as tep:
        tep.write("BAO CAO CHAT LUONG KHONG KHI MOT THANG\n")
        tep.write(f"So dong du lieu     : {len(day) + bo_qua}\n")
        tep.write(f"So dong dung duoc   : {len(day)}\n")
        tep.write(f"So dong bo qua      : {bo_qua}\n")
        tep.write(f"  thieu cot         : {thieu_cot}\n")
        tep.write(f"  ghi chu thay so   : {khong_phai_so}\n")
        tep.write(f"  o trong           : {o_trong}\n")
        tep.write(f"Cach xu ly o trong  : {cach_xu_ly}\n")
        tep.write(f"Cao nhat            : {cao:.1f}\n")
        tep.write(f"Thap nhat           : {thap:.1f}\n")
        tep.write(f"Trung binh thang    : {tb:.4f}\n")
        tep.write(f"Muc chat luong      : {ten_muc(tb)}\n")
        tep.write(f"So gio vuot nguong  : {vuot}\n")
    return duong_dan


if __name__ == "__main__":
    day, thieu_cot, khong_phai_so, o_trong = doc_bang(TEP_VAO)
    cac_dem = (thieu_cot, khong_phai_so, o_trong)
    ghi_bao_cao(TEP_BAO_CAO, day, cac_dem, CACH_XU_LY_O_TRONG)
    ve_do_thi(day, NGUONG, TEP_HINH)
    cao, thap, tb, vuot = bon_dai_luong(day)
    noi_dung = TEP_BAO_CAO.read_text(encoding="utf-8")

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 715
    assert cac_dem == (1, 1, 3)
    assert f"{tb:.4f}" == "49.4964"
    assert ten_muc(tb) == "kem"
    assert "Cach xu ly o trong  : bo dong" in noi_dung
    assert "So dong bo qua      : 5" in noi_dung
    assert TEP_HINH.exists() and TEP_HINH.stat().st_size > 10_000

    # --- Trường hợp biên ---------------------------------------
    # Trung binh thang KHONG vuot nguong, nhung sat duoi: bao cao
    # phai neu ca so gio vuot nguong chu khong chi trung binh.
    assert tb < NGUONG
    assert NGUONG - tb < 1.0
    assert vuot > 0
    assert "So gio vuot nguong" in noi_dung
    # Nong do dung bang can duoi thuoc muc do.
    assert ten_muc(35.5) == "kem"
    assert ten_muc(55.5) == "xau"
    assert ten_muc(35.4) == "trung binh"
    # Hinh hep hon be ngang vung chu cua kho A4.
    from PIL import Image

    with Image.open(TEP_HINH) as anh:
        assert anh.size[0] / 300.0 < 6.3, anh.size
    # NumPy cho cung trung binh voi ham co san cua Python.
    assert f"{sum(day) / len(day):.4f}" == f"{tb:.4f}"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tep chi co dong tieu de: ham tinh phat sinh ValueError
    # truoc khi chia, nen khoanh vung duoc ham nao gap du lieu rong.
    tep_chi_tieu_de = THU_MUC / "pm25_chi_tieu_de.csv"
    tep_chi_tieu_de.write_text("ngay,gio,pm25\n", encoding="utf-8")
    rong, a, b, c = doc_bang(tep_chi_tieu_de)
    assert rong == [] and (a, b, c) == (0, 0, 0)
    da_chan = False
    try:
        bon_dai_luong(rong)
    except ValueError:
        da_chan = True
    assert da_chan, "khong co dong nao ma van tinh duoc"
    tep_chi_tieu_de.unlink()
    # Ten tep khong co: thong bao noi ro tep dang tim.
    da_chan2 = False
    try:
        doc_bang(THU_MUC / "khong_co_tep.csv")
    except FileNotFoundError as loi:
        da_chan2 = "khong_co_tep.csv" in str(loi)
    assert da_chan2, "thong bao loi khong noi ro tep dang tim"
    # Nong do am bi chan o ham tra muc.
    da_chan3 = False
    try:
        ten_muc(-1.0)
    except ValueError:
        da_chan3 = True
    assert da_chan3, "nong do am ma van tra duoc muc"

    print(noi_dung.rstrip())
    print(f"do thi: {TEP_HINH.name}, "
          f"{TEP_HINH.stat().st_size // 1024} kB")
    print(f"numpy {np.__version__}, "
          f"matplotlib {matplotlib.__version__}")
