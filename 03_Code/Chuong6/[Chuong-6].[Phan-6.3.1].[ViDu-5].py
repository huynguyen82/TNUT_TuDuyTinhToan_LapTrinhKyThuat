# -*- coding: utf-8 -*-
"""
Mã bài      : Ví dụ 6.5
Chương, mục : Chương 6, Mục 6.3.1
Đề bài      : Đọc tệp số liệu một tháng theo hai cách, không bắt
              ngoại lệ và bắt ngoại lệ theo loại, rồi so số dòng
              xử lý được của hai cách.
Đầu vào     : 04_DuLieu/pm25_thang.csv, 720 dòng ba cột
Đầu ra      : số dòng dùng được của hai cách, và ba số đếm dòng
              hỏng theo loại
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

from pathlib import Path

GOC = Path(__file__).resolve().parents[2]
TEP = GOC / "04_DuLieu" / "pm25_thang.csv"


# --- in-sach ---
def doc_co_bat(duong_dan):
    """Doc tep, tra ve (day, thieu cot, ghi chu, o trong)."""
    day = []
    thieu_cot = 0
    ghi_chu = 0
    o_trong = 0
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()
        for dong in tep:
            cac_o = dong.strip().split(",")
            try:
                o = cac_o[2]
            except IndexError:
                thieu_cot = thieu_cot + 1
                continue
            if o == "":
                o_trong = o_trong + 1
                continue
            try:
                day.append(float(o))
            except ValueError:
                ghi_chu = ghi_chu + 1
    return day, thieu_cot, ghi_chu, o_trong
# --- het-in-sach ---


DAY, THIEU_COT, GHI_CHU, O_TRONG = doc_co_bat(TEP)

print(f"Co bat   : {len(DAY)} dong dung duoc")
print(f"  thieu cot       : {THIEU_COT}")
print(f"  ghi chu thay so : {GHI_CHU}")
print(f"  o trong         : {O_TRONG}")


def dem_den_khi_hong(duong_dan):
    """So dong dung duoc truoc dong hong dau tien.

    Day la so dong ma cach doc khong bat ngoai le xu ly duoc truoc
    khi chuong trinh dung. Vong lap duoi day chi dem, khong bat,
    nen no do dung phan viec bi mat.
    """
    so_dung = 0
    loai_loi = ""
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()
        for dong in tep:
            cac_o = dong.strip().split(",")
            try:
                float(cac_o[2])
            except (IndexError, ValueError) as loi:
                loai_loi = f"{type(loi).__name__}: {loi}"
                break
            so_dung = so_dung + 1
    return so_dung, loai_loi


KHONG_BAT, LOAI_LOI = dem_den_khi_hong(TEP)
print()
print(f"Khong bat: {KHONG_BAT} dong dung duoc, roi dung vi")
print(f"           {LOAI_LOI}")
print(f"Ti le    : {len(DAY) / KHONG_BAT:.1f} lan")

if __name__ == "__main__":
    # Bắt ngoại lệ giữ lại nhiều dòng hơn hẳn là không bắt.
    assert len(DAY) > KHONG_BAT, \
        "bat ngoai le phai giu duoc nhieu dong hon"

    # Tổng dòng dùng được và dòng bỏ qua phải bằng 720.
    assert len(DAY) + THIEU_COT + GHI_CHU + O_TRONG == 720, \
        "tong so dong phai bang 720"

    # Ba loại dòng hỏng đều có mặt trong tệp.
    assert THIEU_COT > 0 and GHI_CHU > 0 and O_TRONG > 0, \
        "ca ba loai dong hong deu phai co"

    print()
    print("Moi khang dinh dat.")
