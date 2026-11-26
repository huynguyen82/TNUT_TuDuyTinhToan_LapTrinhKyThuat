# -*- coding: utf-8 -*-
"""
Mã bài      : BT 4.1
Chương, mục : Chương 4, Mục 4.1.1
Đề bài      : Hàm thiếu lệnh return trả None; chỉ ra khoảng
              cách giữa dòng báo lỗi và dòng sai thật.
Đầu vào     : không có, mọi số liệu cố định trong mã
Đầu ra      : ba trường hợp dùng kết quả của hàm thiếu return
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

LAI_SUAT_THANG = 0.008
TIEN_TRA_THANG = 25000.0
TIEN_VAY = 500000.0


def so_du_thieu_return(so_du, lai_suat, tien_tra):
    """Bản SAI của đề bài: tính xong nhưng không trả về."""
    moi = so_du * (1 + lai_suat) - tien_tra
    # Dòng sai thật nằm ở đây: thiếu lệnh return.


def so_du_dung(so_du, lai_suat, tien_tra):
    """Bản đúng, để đối chiếu."""
    return so_du * (1 + lai_suat) - tien_tra


def thong_bao_loi_khi_tru(so_du):
    """Thông báo lỗi khi đem kết quả None vào một phép trừ."""
    ket_qua = so_du_thieu_return(
        so_du, LAI_SUAT_THANG, TIEN_TRA_THANG)
    try:
        ket_qua - TIEN_TRA_THANG
    except TypeError as loi:
        return f"TypeError: {loi}"
    return "khong co loi"


def thong_bao_loi_khi_so(so_du):
    """Thông báo lỗi khi đem kết quả None vào một phép so."""
    ket_qua = so_du_thieu_return(
        so_du, LAI_SUAT_THANG, TIEN_TRA_THANG)
    try:
        if ket_qua > 0:
            pass
    except TypeError as loi:
        return f"TypeError: {loi}"
    return "khong co loi"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # In ngay ket qua: khong co loi nao, nen loi khong lo ra.
    assert so_du_thieu_return(
        TIEN_VAY, LAI_SUAT_THANG, TIEN_TRA_THANG) is None
    # Ban dung tra ve mot so thuc.
    assert so_du_dung(TIEN_VAY, LAI_SUAT_THANG,
                      TIEN_TRA_THANG) == 479000.0

    # --- Trường hợp biên ---------------------------------------
    # Phep tru voi None bao loi o dong phep tru, khong o than ham.
    assert thong_bao_loi_khi_tru(TIEN_VAY) == (
        "TypeError: unsupported operand type(s) for -: "
        "'NoneType' and 'float'")
    # Phep so voi None cung bao loi, voi thong bao khac.
    assert thong_bao_loi_khi_so(TIEN_VAY) == (
        "TypeError: '>' not supported between instances of "
        "'NoneType' and 'int'")
    # Ca hai thong bao deu nhac toi NoneType.
    assert "NoneType" in thong_bao_loi_khi_tru(TIEN_VAY)
    assert "NoneType" in thong_bao_loi_khi_so(TIEN_VAY)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ham thieu return tra None voi moi doi so, ke ca doi so vo ly.
    assert so_du_thieu_return(0.0, 0.0, 0.0) is None
    assert so_du_thieu_return(-1.0, 0.5, 1e9) is None
    # Khoang cach giua dong bao loi va dong sai that.
    DONG_SAI_THAT = 23
    DONG_BAO_LOI = 37
    assert DONG_BAO_LOI - DONG_SAI_THAT == 14

    print("ket qua ham thieu return:",
          so_du_thieu_return(TIEN_VAY, LAI_SUAT_THANG,
                             TIEN_TRA_THANG))
    print("ket qua ban dung         :",
          so_du_dung(TIEN_VAY, LAI_SUAT_THANG, TIEN_TRA_THANG))
    print("loi khi tru :", thong_bao_loi_khi_tru(TIEN_VAY))
    print("loi khi so  :", thong_bao_loi_khi_so(TIEN_VAY))
