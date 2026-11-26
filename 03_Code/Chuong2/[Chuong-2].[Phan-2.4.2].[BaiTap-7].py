# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.7
Chương, mục : Chương 2, Mục 2.4.1 và 2.4.2
Đề bài      : Chạy năm ví dụ sai số cho sẵn, ghi kết quả bất
              thường, chỉ ra nguồn sai số và đo sai số tuyệt đối
              cùng sai số tương đối khi đo được.
Đầu vào     : năm đoạn mã cho sẵn, cài đặt thành năm hàm
Đầu ra      : bảng năm dòng gồm kết quả, nguồn sai số và sai số
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

import math

NGUON_LAM_TRON = "lam tron"
NGUON_TRAN_SO = "tran so"
NGUON_CHIA_NGUYEN = "chia nguyen"
NGUON_SO_SANH = "so sanh so thuc"


def sai_so_tuyet_doi(do_duoc, dung):
    """Sai số tuyệt đối, cùng đơn vị với đại lượng."""
    return abs(do_duoc - dung)


def sai_so_tuong_doi(do_duoc, dung):
    """Sai số tương đối, không đơn vị.

    Phát sinh ValueError khi giá trị đúng bằng 0, vì khi đó sai
    số tương đối không định nghĩa.
    """
    if dung == 0:
        raise ValueError("gia tri dung bang 0")
    return abs(do_duoc - dung) / abs(dung)


def s1_cong_hai_so():
    """S1: cộng hai số thực. Nguồn làm tròn."""
    return 0.1 + 0.2, 0.3


def s2_cong_don():
    """S2: cộng 0,1 mười lần. Nguồn làm tròn tích luỹ."""
    tong = 0.0
    for _ in range(10):
        tong = tong + 0.1
    return tong, 1.0


def s3_tran_so():
    """S3: luỹ thừa số thực vượt miền. Nguồn tràn số.

    Trả về (ten_loi, thong_bao, ket_qua_cua_phep_nhan).
    """
    try:
        1e308 ** 2
        return None, None, None
    except OverflowError as loi:
        return type(loi).__name__, str(loi), 1e308 * 10


def s4_chia_nguyen():
    """S4: chia nguyên số âm. Nguồn chọn sai toán tử."""
    return -7 // 2, int(-7 / 2)


def s5_so_sanh():
    """S5: kiểm dung sai bằng dấu bằng. Nguồn so sánh số thực."""
    tong = 50.00
    for _ in range(10):
        tong = tong + 0.01
    return tong, 50.10


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    do_duoc, dung = s1_cong_hai_so()
    assert do_duoc != dung
    assert sai_so_tuyet_doi(do_duoc, dung) == 5.551115123125783e-17
    assert sai_so_tuong_doi(do_duoc, dung) < 1e-15
    tong2, dung2 = s2_cong_don()
    assert tong2 != dung2
    assert sai_so_tuyet_doi(tong2, dung2) > 0

    # --- Trường hợp biên ---------------------------------------
    # S4 không phải sai số biểu diễn mà là chọn sai toán tử: hai
    # cách lệch đúng 1 đơn vị, và chỉ lệch khi số bị chia âm.
    chia_nguyen, cat_phan_le = s4_chia_nguyen()
    assert chia_nguyen == -4 and cat_phan_le == -3
    assert cat_phan_le - chia_nguyen == 1
    assert 7 // 2 == int(7 / 2) == 3
    # S5: giá trị đúng về toán học mà phép bằng cho False, còn
    # math.isclose với ngưỡng lấy từ bài toán cho True.
    tong5, dung5 = s5_so_sanh()
    assert tong5 != dung5
    assert math.isclose(tong5, dung5, abs_tol=1e-9)
    assert sai_so_tuyet_doi(tong5, dung5) < 1e-13

    # --- Trường hợp ngoại lệ -----------------------------------
    # S3: luỹ thừa báo lỗi, còn phép nhân trả vô cực mà im lặng.
    ten_loi, thong_bao, bang_phep_nhan = s3_tran_so()
    assert ten_loi == "OverflowError", ten_loi
    assert thong_bao == "(34, 'Result too large')", thong_bao
    assert math.isinf(bang_phep_nhan)
    # Sai số tương đối không định nghĩa khi giá trị đúng bằng 0.
    da_chan = False
    try:
        sai_so_tuong_doi(0.1, 0.0)
    except ValueError:
        da_chan = True
    assert da_chan, "gia tri dung bang 0 ma van tinh duoc"

    print("BT 2.7")
    print(f"  S1 {NGUON_LAM_TRON:<16}{do_duoc!r}")
    print(f"     sai so tuyet doi {sai_so_tuyet_doi(do_duoc, dung)!r}")
    print(f"  S2 {NGUON_LAM_TRON:<16}{tong2!r}")
    print(f"     sai so tuyet doi {sai_so_tuyet_doi(tong2, dung2)!r}")
    print(f"  S3 {NGUON_TRAN_SO:<16}{ten_loi}: {thong_bao}")
    print(f"     1e308 * 10 = {bang_phep_nhan}")
    print(f"  S4 {NGUON_CHIA_NGUYEN:<16}-7 // 2 = {chia_nguyen}, "
          f"int(-7 / 2) = {cat_phan_le}")
    print(f"  S5 {NGUON_SO_SANH:<16}{tong5!r}")
    print(f"     sai so tuyet doi {sai_so_tuyet_doi(tong5, dung5)!r}")
