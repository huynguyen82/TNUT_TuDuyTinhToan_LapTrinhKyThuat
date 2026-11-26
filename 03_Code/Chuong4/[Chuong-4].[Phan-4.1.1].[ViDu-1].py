# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 1
Chương, mục : Chương 4, Mục 4.1.1
Đề bài      : Định nghĩa hàm tính số dư sau một tháng trả nợ,
              rồi gọi lại ba lần cho ba tháng liên tiếp.
Đầu vào     : số tiền vay, lãi suất tháng, tiền trả mỗi tháng;
              viết thẳng trong mã
Đầu ra      : số dư sau từng tháng, nghìn đồng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
LAI_SUAT = 0.008
TIEN_TRA = 25000.0


def so_du_sau_mot_thang(so_du, lai_suat, tien_tra):
    """So du sau mot thang tra no, nghin dong."""
    return so_du * (1 + lai_suat) - tien_tra


so_du = 500000.0
for thang in range(1, 4):
    so_du = so_du_sau_mot_thang(so_du, LAI_SUAT, TIEN_TRA)
    print(f"Thang {thang}: {so_du:.2f} nghin dong")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_du_sau_mot_thang(500000.0, 0.008, 25000.0) == 479000.0
    assert abs(so_du - 436494.656) < 1e-6, so_du

    # --- Trường hợp biên ---------------------------------------
    # Lai suat bang 0: so du giam dung so tien tra.
    assert so_du_sau_mot_thang(1000.0, 0.0, 100.0) == 900.0
    # Tien tra bang 0: so du tang dung phan lai.
    assert so_du_sau_mot_thang(1000.0, 0.01, 0.0) == 1010.0
    # Tien tra lon hon ca goc lan lai: so du thanh am, tuc da
    # tra thua. Ham khong chan truong hop nay, xem Khoi 8.
    assert so_du_sau_mot_thang(1000.0, 0.0, 2000.0) == -1000.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Goi ham thieu doi so phai bao loi.
    da_chan = False
    try:
        so_du_sau_mot_thang(1000.0, 0.01)
    except TypeError as loi:
        da_chan = "tien_tra" in str(loi)
    assert da_chan, "goi ham thieu doi so ma van chay"
