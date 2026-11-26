# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 4
Chương, mục : Chương 5, Mục 5.3.1
Đề bài      : Đọc 24 số đo từ tệp pm25_ngay.txt, tính bốn đại
              lượng, rồi ghi báo cáo ra một tệp mới.
Đầu vào     : 04_DuLieu/pm25_ngay.txt
Đầu ra      : 04_DuLieu/bao_cao_ngay.txt và vài dòng ra màn hình
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

from pathlib import Path

THU_MUC = Path(__file__).resolve().parents[2] / "04_DuLieu"
TEP_VAO = THU_MUC / "pm25_ngay.txt"
TEP_RA = THU_MUC / "bao_cao_ngay.txt"
NGUONG = 50.0


# --- in-sach ---
def doc_so_do(duong_dan):
    """Doc moi dong cua tep thanh mot so thuc."""
    day = []
    with open(duong_dan, encoding="utf-8") as tep:
        for dong in tep:
            day.append(float(dong.strip()))
    return day


def ghi_bao_cao(duong_dan, day, nguong):
    """Ghi bao cao bon dai luong ra mot tep moi."""
    vuot = 0
    for so_do in day:
        if so_do > nguong:
            vuot = vuot + 1
    with open(duong_dan, "w", encoding="utf-8") as tep:
        tep.write(f"So gio do duoc : {len(day)}\n")
        tep.write(f"Cao nhat       : {max(day):.1f}\n")
        tep.write(f"Thap nhat      : {min(day):.1f}\n")
        tep.write(f"Trung binh     : {sum(day) / len(day):.2f}\n")
        tep.write(f"So gio vuot    : {vuot}\n")
    return vuot
# --- het-in-sach ---


if __name__ == "__main__":
    day = doc_so_do(TEP_VAO)
    so_gio_vuot = ghi_bao_cao(TEP_RA, day, NGUONG)

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 24
    assert day[0] == 31.2
    assert max(day) == 71.5
    assert so_gio_vuot == 7
    noi_dung = TEP_RA.read_text(encoding="utf-8")
    assert "Trung binh     : 43.67" in noi_dung
    assert noi_dung.count("\n") == 5

    # --- Trường hợp biên ---------------------------------------
    # Quen strip KHONG lam float hong: float tu bo khoang trang.
    assert float("31.2\n") == 31.2
    # Nhung no lam so sanh chuoi sai, va day la loi im lang.
    assert ("31.2\n" == "31.2") is False
    assert len("31.2\n") == 5 and len("31.2") == 4
    # Mo lai bang che do w thi tep cu bi xoa trang, khong bao gi.
    ghi_bao_cao(TEP_RA, day[:1], NGUONG)
    assert TEP_RA.read_text(encoding="utf-8").count("\n") == 5
    assert "So gio do duoc : 1" in TEP_RA.read_text(
        encoding="utf-8")
    # Ghi lai ban dung de tep du lieu khong ket thuc o trang thai sai.
    ghi_bao_cao(TEP_RA, day, NGUONG)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ten tep khong co thi bao loi ngay o lenh open.
    da_chan = False
    try:
        doc_so_do(THU_MUC / "khong_co_tep.txt")
    except FileNotFoundError:
        da_chan = True
    assert da_chan, "tep khong ton tai ma van doc duoc"
    # float tren mot o trong bao loi.
    da_chan2 = False
    try:
        float("")
    except ValueError:
        da_chan2 = True
    assert da_chan2, "chuoi rong ma float chuyen duoc"

    print(f"doc {len(day)} so do tu {TEP_VAO.name}")
    print(f"ghi bao cao ra {TEP_RA.name}")
    print(TEP_RA.read_text(encoding="utf-8").rstrip())
