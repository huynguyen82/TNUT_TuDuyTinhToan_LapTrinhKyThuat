# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 5
Chương, mục : Chương 5, Mục 5.3.2
Đề bài      : Đọc tệp số liệu dạng bảng 720 dòng có dòng thiếu
              cột, dòng ghi chữ và ô trống; báo số dòng đã bỏ.
Đầu vào     : 04_DuLieu/pm25_thang.csv
Đầu ra      : số dòng dùng được, số dòng bỏ qua theo từng loại
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

from pathlib import Path

THU_MUC = Path(__file__).resolve().parents[2] / "04_DuLieu"
TEP_VAO = THU_MUC / "pm25_thang.csv"
SO_COT = 3


# --- in-sach ---
def doc_bang(duong_dan):
    """Doc tep bang, tra ve so do dung duoc va ba so dem."""
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
# --- het-in-sach ---


if __name__ == "__main__":
    day, thieu_cot, khong_phai_so, o_trong = doc_bang(TEP_VAO)
    bo_qua = thieu_cot + khong_phai_so + o_trong

    # --- Trường hợp thường -------------------------------------
    assert len(day) == 715
    assert thieu_cot == 1
    assert khong_phai_so == 1
    assert o_trong == 3
    # Tong phai khop 720 dong du lieu cua tep.
    assert len(day) + bo_qua == 720
    assert f"{sum(day) / len(day):.4f}" == "49.4964"

    # --- Trường hợp biên ---------------------------------------
    # Dong thieu cot: split cho it cot hon, lay cot thu ba bao loi.
    o = "5,12".split(",")
    assert len(o) == 2
    da_chan = False
    try:
        o[2]
    except IndexError:
        da_chan = True
    assert da_chan, "dong thieu cot ma lay duoc cot thu ba"
    # O trong khac han so 0: coi o trong la 0 keo trung binh xuong.
    assert float("0") == 0.0
    coi_la_0 = (sum(day) + 0.0 * o_trong) / (len(day) + o_trong)
    assert coi_la_0 < sum(day) / len(day)
    # Dong ghi chu co du ba cot nhung cot thu ba khong phai so.
    assert len("5,12,cam bien bao tri".split(",")) == 3

    # --- Trường hợp ngoại lệ -----------------------------------
    # float tren ca dong chua tach cot bao loi.
    da_chan2 = False
    try:
        float("1,0,31.2")
    except ValueError:
        da_chan2 = True
    assert da_chan2, "ca dong csv ma float chuyen duoc"
    # Tep khong ton tai bao loi ngay o lenh open.
    da_chan3 = False
    try:
        doc_bang(THU_MUC / "khong_co_tep.csv")
    except FileNotFoundError:
        da_chan3 = True
    assert da_chan3, "tep khong ton tai ma van doc duoc"

    print(f"dong du lieu       : 720")
    print(f"dung duoc          : {len(day)}")
    print(f"bo qua             : {bo_qua}")
    print(f"  thieu cot        : {thieu_cot}")
    print(f"  khong phai so    : {khong_phai_so}")
    print(f"  o trong          : {o_trong}")
    print(f"trung binh         : {sum(day) / len(day):.4f}")
