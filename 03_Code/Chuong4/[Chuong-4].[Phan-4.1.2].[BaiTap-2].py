# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.2
Chương, mục : Chương 4, Mục 4.1.2
Đề bài      : Ba hàm dùng một tên trùng biến toàn cục theo ba
              cách: chỉ đọc, chỉ gán, đọc rồi gán.
Đầu vào     : không có, mọi số liệu cố định trong mã
Đầu ra      : kết luận cho từng hàm kèm thông báo lỗi nếu có
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

LAI_SUAT = 0.008


def chi_doc():
    """Hàm thứ nhất: chỉ đọc biến toàn cục. Chạy được."""
    return LAI_SUAT


def chi_gan():
    """Hàm thứ hai: chỉ gán. Tạo biến cục bộ mới."""
    LAI_SUAT = 0.02
    return LAI_SUAT


def doc_roi_gan():
    """Hàm thứ ba: đọc rồi gán cùng một tên. Báo lỗi."""
    cu = LAI_SUAT
    LAI_SUAT = 0.02
    return cu, LAI_SUAT


def thong_bao_loi_doc_roi_gan():
    """Thông báo lỗi nguyên văn của hàm thứ ba."""
    try:
        doc_roi_gan()
    except UnboundLocalError as loi:
        return f"UnboundLocalError: {loi}"
    return "khong co loi"


def nhan_qua_tham_so(lai_suat):
    """Cách đúng: nhận giá trị qua tham số."""
    return lai_suat


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Ham chi doc chay duoc va tra dung gia tri bien toan cuc.
    assert chi_doc() == 0.008
    assert chi_doc() == LAI_SUAT
    # Ham nhan qua tham so kiem duoc voi moi gia tri.
    assert nhan_qua_tham_so(0.015) == 0.015

    # --- Trường hợp biên ---------------------------------------
    # Ham chi gan chay duoc, nhung bien toan cuc khong doi.
    assert chi_gan() == 0.02
    assert LAI_SUAT == 0.008
    # Goi lai ham chi doc sau do: van tra gia tri cu.
    assert chi_doc() == 0.008
    # Ham nhan qua tham so khong phu thuoc bien toan cuc.
    assert nhan_qua_tham_so(0.008) == chi_doc()

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ham thu ba bao loi o dong DOC, du dong do dung truoc dong gan.
    assert thong_bao_loi_doc_roi_gan() == (
        "UnboundLocalError: cannot access local variable "
        "'LAI_SUAT' where it is not associated with a value")
    da_chan = False
    try:
        doc_roi_gan()
    except UnboundLocalError:
        da_chan = True
    assert da_chan, "doc roi gan ma khong bao loi"
    # Sau ca ba lan goi, bien toan cuc van nguyen gia tri ban dau.
    assert LAI_SUAT == 0.008

    print("chi_doc()          :", chi_doc())
    print("chi_gan()          :", chi_gan())
    print("LAI_SUAT sau do    :", LAI_SUAT)
    print("doc_roi_gan()      :", thong_bao_loi_doc_roi_gan())
    print("nhan_qua_tham_so   :", nhan_qua_tham_so(0.015))
