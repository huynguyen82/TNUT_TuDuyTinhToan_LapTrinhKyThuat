# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 2
Chương, mục : Chương 4, Mục 4.1.2
Đề bài      : So hai cách lấy lãi suất vào trong hàm: đọc từ
              biến toàn cục và nhận qua tham số. Cho thấy biến
              cục bộ không thoát ra ngoài hàm.
Đầu vào     : không có
Đầu ra      : kết quả hai cách và phạm vi của từng biến
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
LAI_SUAT = 0.008


def so_du_doc_bien_ngoai(so_du, tien_tra):
    """Doc LAI_SUAT tu pham vi toan cuc."""
    return so_du * (1 + LAI_SUAT) - tien_tra


def so_du_nhan_tham_so(so_du, lai_suat, tien_tra):
    """Nhan lai suat qua tham so, tu du khong phu thuoc ngoai."""
    ket_qua = so_du * (1 + lai_suat) - tien_tra
    return ket_qua


print("Doc bien ngoai :", so_du_doc_bien_ngoai(500000.0, 25000.0))
print("Nhan tham so   :",
      so_du_nhan_tham_so(500000.0, LAI_SUAT, 25000.0))

# Bien ket_qua la bien cuc bo: khong ton tai ngoai ham.
print("Co bien ket_qua o ngoai ham:", "ket_qua" in dir())
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_du_doc_bien_ngoai(500000.0, 25000.0) == 479000.0
    assert (so_du_doc_bien_ngoai(500000.0, 25000.0)
            == so_du_nhan_tham_so(500000.0, LAI_SUAT, 25000.0))
    assert "ket_qua" not in dir()

    # --- Trường hợp biên ---------------------------------------
    # Hai cach bang nhau chi khi bien ngoai chua bi doi. Doi
    # bien ngoai thi ham doc bien ngoai cho ket qua khac, con
    # ham nhan tham so khong doi.
    truoc = so_du_doc_bien_ngoai(500000.0, 25000.0)
    LAI_SUAT = 0.015
    sau = so_du_doc_bien_ngoai(500000.0, 25000.0)
    assert sau != truoc, (truoc, sau)
    assert so_du_nhan_tham_so(500000.0, 0.008, 25000.0) == truoc
    LAI_SUAT = 0.008
    # Ham nhan tham so kiem rieng duoc voi moi lai suat.
    for lai in (0.0, 0.008, 0.02):
        mong_doi = 500000.0 * (1 + lai) - 25000.0
        assert so_du_nhan_tham_so(500000.0, lai, 25000.0) == mong_doi

    # --- Trường hợp ngoại lệ -----------------------------------
    # Doc roi gan cung mot ten trong ham tao bien cuc bo, nen
    # phep doc truoc do bao UnboundLocalError.
    def ham_sai():
        """Doc LAI_SUAT roi gan lai cung ten trong than ham."""
        gia_tri = LAI_SUAT
        LAI_SUAT = 0.02  # noqa: F841
        return gia_tri

    da_chan = False
    try:
        ham_sai()
    except UnboundLocalError:
        da_chan = True
    assert da_chan, "doc roi gan cung ten ma khong bao loi"
