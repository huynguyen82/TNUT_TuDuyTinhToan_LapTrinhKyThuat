# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 3
Chương, mục : Chương 4, Mục 4.1.3
Đề bài      : Hàm tính số tháng trả hết nợ, với lãi suất là
              tham số có giá trị mặc định. Cho thấy ba cách
              gọi cùng một hàm.
Đầu vào     : số tiền vay và tiền trả mỗi tháng
Đầu ra      : số tháng trả hết nợ
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
LAI_SUAT_MAC_DINH = 0.008


def so_thang_tra_het(tien_vay, tien_tra,
                     lai_suat=LAI_SUAT_MAC_DINH):
    """So thang tra het no.

    tien_vay : so tien vay, nghin dong
    tien_tra : so tien tra moi thang, nghin dong
    lai_suat : lai suat thang, mac dinh 0.008
    """
    if tien_tra <= tien_vay * lai_suat:
        raise ValueError("tien tra khong du bu lai thang dau")
    so_du = tien_vay
    so_thang = 0
    while so_du > 0:
        so_du = so_du * (1 + lai_suat) - tien_tra
        so_thang = so_thang + 1
    return so_thang


print("Mac dinh      :", so_thang_tra_het(500000.0, 25000.0))
print("Theo thu tu   :", so_thang_tra_het(500000.0, 25000.0, 0.0))
print("Theo ten      :",
      so_thang_tra_het(500000.0, 25000.0, lai_suat=0.015))
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_thang_tra_het(500000.0, 25000.0) == 22
    assert so_thang_tra_het(500000.0, 25000.0, 0.008) == 22
    # Ba cach goi deu hop le, va hai cach dau trung nhau.
    assert (so_thang_tra_het(500000.0, 25000.0)
            == so_thang_tra_het(500000.0, 25000.0,
                                LAI_SUAT_MAC_DINH))

    # --- Trường hợp biên ---------------------------------------
    # Lai suat bang 0: so thang bang tien vay chia tien tra,
    # lam tron len.
    assert so_thang_tra_het(500000.0, 25000.0, 0.0) == 20
    # Tien tra lon hon khoan vay: tra het trong mot thang.
    assert so_thang_tra_het(1000.0, 2000.0, 0.0) == 1
    # Lai suat cao hon thi tra het lau hon.
    assert (so_thang_tra_het(500000.0, 25000.0, 0.015)
            > so_thang_tra_het(500000.0, 25000.0, 0.0))
    # Tham so co mac dinh phai dung sau tham so khong co, nen
    # goi theo thu tu van dat lai suat o vi tri thu ba.
    assert so_thang_tra_het(500000.0, 25000.0, 0.015) == 24

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tien tra khong du bu lai thang dau thi no khong bao gio het.
    da_chan = False
    try:
        so_thang_tra_het(500000.0, 100.0)
    except ValueError:
        da_chan = True
    assert da_chan, "tien tra qua it ma van tinh duoc"
    # Goi theo ten sai ten tham so phai bao loi.
    da_chan_2 = False
    try:
        so_thang_tra_het(500000.0, 25000.0, lai=0.01)
    except TypeError:
        da_chan_2 = True
    assert da_chan_2, "ten tham so sai ma van goi duoc"
