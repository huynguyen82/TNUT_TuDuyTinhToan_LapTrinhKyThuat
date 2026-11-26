# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.5
Chương, mục : Chương 6, Mục 6.3.1
Đề bài      : Thêm try và except theo loại cụ thể vào bộ đọc tệp
              bảng của Mục 5.3.2, rồi so số dòng xử lý được trước
              và sau. Bắt riêng ba loại dòng hỏng.
Đầu vào     : 04_DuLieu/pm25_thang.csv
Đầu ra      : hai số dòng dùng được, ba số đếm dòng hỏng, tỉ lệ
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

from pathlib import Path

GOC = Path(__file__).resolve().parents[2]
TEP = GOC / "04_DuLieu" / "pm25_thang.csv"
TEP_KHONG_CO = GOC / "04_DuLieu" / "khong_he_co_tep_nay.csv"
SO_DONG_DU_LIEU = 720


def doc_khong_bat(duong_dan):
    """Doc tep, khong bat gi. Tra ve (so dong dung, mo ta loi).

    Vong lap dung o dong hong dau tien. Ham dem lai phan viec da
    lam duoc truoc khi dung, de do duoc phan bi mat.
    """
    so_dung = 0
    mo_ta = "khong co loi"
    with open(duong_dan, encoding="utf-8") as tep:
        tep.readline()
        for dong in tep:
            cac_o = dong.strip().split(",")
            try:
                float(cac_o[2])
            except (IndexError, ValueError) as loi:
                mo_ta = f"{type(loi).__name__}: {loi}"
                break
            so_dung = so_dung + 1
    return so_dung, mo_ta


def doc_co_bat(duong_dan):
    """Doc tep, bat ngoai le theo tung loai. Tra ve bon so.

    Ba loai dong hong bat o ba cho khac nhau: thieu cot bat bang
    IndexError khi lay cot thu ba, o trong kiem bang phep so chuoi
    rong, va ghi chu thay so bat bang ValueError cua float.
    """
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


def doc_an_toan(duong_dan):
    """Bat FileNotFoundError **ngoai** vong lap doc dong.

    Ten tep khong co la loi xay ra truoc khi doc dong nao, nen bat
    no trong vong lap la sai cho: vong lap chua bao gio chay.
    """
    try:
        return doc_co_bat(duong_dan)
    except FileNotFoundError:
        return [], 0, 0, 0


KHONG_BAT, MO_TA = doc_khong_bat(TEP)
DAY, THIEU_COT, GHI_CHU, O_TRONG = doc_co_bat(TEP)


def in_ket_qua():
    """In hai cach doc tep canh nhau."""
    print(f"Khong bat : {KHONG_BAT} dong dung duoc")
    print(f"            roi dung vi {MO_TA}")
    print(f"Co bat    : {len(DAY)} dong dung duoc")
    print(f"  thieu cot       : {THIEU_COT}")
    print(f"  ghi chu thay so : {GHI_CHU}")
    print(f"  o trong         : {O_TRONG}")
    print(f"Ti le     : {len(DAY) / KHONG_BAT:.1f} lan")


if __name__ == "__main__":
    in_ket_qua()

    # Bắt ngoại lệ giữ lại nhiều dòng hơn hẳn là không bắt.
    assert len(DAY) > KHONG_BAT, \
        "bat ngoai le phai giu duoc nhieu dong hon"

    # Tổng dòng dùng được và ba loại dòng hỏng bằng 720.
    assert (len(DAY) + THIEU_COT + GHI_CHU + O_TRONG
            == SO_DONG_DU_LIEU), "tong so dong phai bang 720"

    # Ba loại dòng hỏng bắt ở ba chỗ khác nhau, nên cả ba đều
    # đếm được riêng chứ không gộp thành một số.
    assert THIEU_COT > 0 and GHI_CHU > 0 and O_TRONG > 0, \
        "ca ba loai dong hong deu phai dem duoc rieng"

    # Tên tệp không có là lỗi phải bắt ngoài vòng lặp.
    assert doc_an_toan(TEP_KHONG_CO) == ([], 0, 0, 0), \
        "ten tep khong co phai bat ngoai vong lap"

    print()
    print("Moi khang dinh dat.")
