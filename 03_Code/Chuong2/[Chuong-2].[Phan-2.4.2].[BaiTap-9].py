# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.9
Chương, mục : Chương 2, Mục 1.1.1 và cả sáu tiểu mục Chương 2
Đề bài      : Kiểm dung sai một loạt chi tiết: nhận kích thước
              danh nghĩa, dung sai và số chi tiết; với mỗi chi
              tiết nhận kích thước đo dạng chuỗi, ép kiểu, kết
              luận, cộng dồn; cuối cùng in số chi tiết đạt, kích
              thước trung bình và sai số tương đối của trung
              bình so với kích thước danh nghĩa.
Đầu vào     : danh nghĩa và dung sai (mm, số thực); số chi tiết
              (số nguyên, miền 1–100); các kích thước đo (chuỗi)
Đầu ra      : số chi tiết đạt (số nguyên); trung bình (mm, hai
              chữ số thập phân); sai số tương đối (ký hiệu khoa
              học)
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Bảng đặc tả ba phần nằm
ở tệp .md, lập trước khi viết dòng mã đầu tiên.
"""

import math

MIEN_SO_CHI_TIET = (1, 100)


def ep_kieu(chuoi_do):
    """Ép chuỗi kích thước sang số thực, trả None khi không được."""
    try:
        return float(chuoi_do)
    except ValueError:
        return None


def chi_tiet_dat(kich_thuoc_mm, danh_nghia, dung_sai):
    """Chi tiết có nằm trong miền dung sai hay không.

    Dùng math.isclose với ngưỡng tuyệt đối lấy từ dung sai của
    bài toán, không lấy ngưỡng mặc định.
    """
    return math.isclose(kich_thuoc_mm, danh_nghia,
                        rel_tol=0.0, abs_tol=dung_sai)


def tong_hop(danh_nghia, dung_sai, cac_chuoi_do):
    """Trả về (so_dat, trung_binh, sai_so_tuong_doi).

    Cộng dồn trên giá trị gốc, không trên giá trị đã làm tròn để
    in, nếu không thì mắc lỗi L2.3-3. Phát sinh ValueError khi
    số chi tiết ngoài miền hoặc khi gặp chuỗi không ép kiểu được.
    """
    so_chi_tiet = len(cac_chuoi_do)
    if not (MIEN_SO_CHI_TIET[0] <= so_chi_tiet
            <= MIEN_SO_CHI_TIET[1]):
        raise ValueError(
            f"du lieu khong hop le: so chi tiet = {so_chi_tiet}")
    tong = 0.0
    so_dat = 0
    for thu_tu, chuoi_do in enumerate(cac_chuoi_do, start=1):
        kich_thuoc_mm = ep_kieu(chuoi_do)
        if kich_thuoc_mm is None:
            raise ValueError(
                f"du lieu khong hop le o chi tiet {thu_tu}: "
                f"{chuoi_do}")
        tong = tong + kich_thuoc_mm
        if chi_tiet_dat(kich_thuoc_mm, danh_nghia, dung_sai):
            so_dat = so_dat + 1
    trung_binh = tong / so_chi_tiet
    tuong_doi = abs(trung_binh - danh_nghia) / abs(danh_nghia)
    return so_dat, trung_binh, tuong_doi


def in_phieu(danh_nghia, dung_sai, cac_chuoi_do):
    """In phiếu tổng hợp theo đúng định dạng của bảng đặc tả."""
    so_dat, trung_binh, tuong_doi = tong_hop(
        danh_nghia, dung_sai, cac_chuoi_do)
    print(f"{'So chi tiet dat':<22}{so_dat:>8}")
    print(f"{'Kich thuoc trung binh':<22}{trung_binh:>8.2f} mm")
    print(f"{'Sai so tuong doi':<22}{tuong_doi:>8.2e}")


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    ba_chi_tiet = ["50.03", "49.97", "50.01"]
    so_dat, trung_binh, tuong_doi = tong_hop(
        50.00, 0.05, ba_chi_tiet)
    assert so_dat == 3, so_dat
    assert trung_binh == 50.00333333333333, trung_binh
    assert f"{trung_binh:.2f}" == "50.00"
    assert abs(tuong_doi - 6.666666666e-5) < 1e-12, tuong_doi
    # Cộng dồn trên giá trị gốc khác cộng dồn trên giá trị đã làm
    # tròn để in: đây là lỗi L2.3-3 nếu làm nhầm.
    tong_lam_tron = sum(
        float(f"{float(chuoi):.1f}") for chuoi in ba_chi_tiet)
    assert tong_lam_tron / 3 != trung_binh

    # --- Trường hợp biên ---------------------------------------
    # Một chi tiết duy nhất ở đúng cận trên vẫn đạt.
    so_dat_1, trung_binh_1, tuong_doi_1 = tong_hop(
        50.00, 0.05, ["50.05"])
    assert so_dat_1 == 1
    assert f"{trung_binh_1:.2f}" == "50.05"
    # Ngay ngoài cận trên thì không đạt nhưng vẫn vào trung bình.
    so_dat_2, trung_binh_2, _ = tong_hop(50.00, 0.05, ["50.06"])
    assert so_dat_2 == 0
    assert f"{trung_binh_2:.2f}" == "50.06"
    # Trung bình đúng bằng danh nghĩa cho sai số tương đối bằng 0.
    _, _, tuong_doi_0 = tong_hop(
        50.00, 0.05, ["49.95", "50.05"])
    assert tuong_doi_0 == 0.0, tuong_doi_0
    # Đủ 100 chi tiết vẫn trong miền.
    assert tong_hop(50.00, 0.05, ["50.00"] * 100)[0] == 100

    # --- Trường hợp ngoại lệ -----------------------------------
    # Danh sách rỗng, tức số chi tiết bằng 0, bị chặn trước khi
    # chia nên không phát sinh ZeroDivisionError.
    da_chan = False
    try:
        tong_hop(50.00, 0.05, [])
    except ValueError as loi:
        da_chan = "so chi tiet" in str(loi)
    assert da_chan, "so chi tiet bang 0 ma van tinh duoc"
    # Chuỗi dùng dấu phẩy thập phân bị chặn, kèm số thứ tự.
    da_chan_2 = False
    try:
        tong_hop(50.00, 0.05, ["50.03", "50,01"])
    except ValueError as loi:
        da_chan_2 = "chi tiet 2" in str(loi)
    assert da_chan_2, "chuoi sai ma van tinh duoc"

    print("BT 2.9")
    in_phieu(50.00, 0.05, ba_chi_tiet)
