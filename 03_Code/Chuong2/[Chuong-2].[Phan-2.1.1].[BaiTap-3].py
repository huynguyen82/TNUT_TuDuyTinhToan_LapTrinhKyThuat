# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.3
Chương, mục : Chương 2, Mục 2.1.1 và 2.3.1
Đề bài      : Chuyển phần tính điện năng của mã giả Bài tập 1.9
              thành chương trình Python cho một động cơ: nhập
              công suất và số giờ chạy, tính và in điện năng.
Đầu vào     : công suất (kW, miền 0,37–200) và số giờ chạy
              (h, miền 0–24), nhập từ bàn phím
Đầu ra      : điện năng (kWh), một chữ số thập phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Phần tính tách thành hàm
để kiểm được bằng khẳng định mà không cần gõ bàn phím.
"""

MIEN_CONG_SUAT = (0.37, 200.0)
MIEN_GIO_CHAY = (0.0, 24.0)


def kiem_mien(gia_tri, mien, ten):
    """Kiểm một giá trị theo miền đã khai báo ở bảng đặc tả."""
    if not mien[0] <= gia_tri <= mien[1]:
        raise ValueError(
            f"du lieu khong hop le: {ten} = {gia_tri}, "
            f"mien cho phep {mien}")
    return gia_tri


def dien_nang(cong_suat_kw, gio_chay):
    """Điện năng một động cơ trong một ngày, kWh."""
    kiem_mien(cong_suat_kw, MIEN_CONG_SUAT, "cong_suat_kw")
    kiem_mien(gio_chay, MIEN_GIO_CHAY, "gio_chay")
    return cong_suat_kw * gio_chay


def dinh_dang(gia_tri):
    """Trình bày điện năng theo đặc tả: một chữ số thập phân."""
    return f"{gia_tri:.1f}"


def chay_tu_ban_phim():
    """Phần nhập từ bàn phím, tách riêng khỏi phần tính."""
    cong_suat_kw = float(input("Cong suat (kW): "))
    gio_chay = float(input("So gio chay (h): "))
    print("Dien nang (kWh):",
          dinh_dang(dien_nang(cong_suat_kw, gio_chay)))


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert dien_nang(7.5, 8.0) == 60.0
    assert dinh_dang(dien_nang(7.5, 8.0)) == "60.0"
    assert dinh_dang(dien_nang(15.0, 6.0)) == "90.0"

    # --- Trường hợp biên ---------------------------------------
    # Số giờ chạy bằng 0 là giá trị hợp lệ ở cận dưới của miền.
    assert dien_nang(7.5, 0.0) == 0.0
    assert dinh_dang(dien_nang(7.5, 0.0)) == "0.0"
    # Hai cận của cả hai miền đều hợp lệ.
    assert dien_nang(0.37, 24.0) > 0
    assert dien_nang(200.0, 24.0) == 4800.0
    # Làm tròn hiển thị theo giá trị LƯU, không theo chữ số đã
    # gõ. Số 60,05 được lưu thành 60,049999..., nhỏ hơn 60,05 một
    # chút, nên làm tròn một chữ số thập phân ra 60.0 chứ không
    # ra 60.1 như quy tắc làm tròn trên giấy.
    assert dinh_dang(60.05) == "60.0"
    assert dinh_dang(60.04) == "60.0"
    assert dinh_dang(60.15) == "60.1"
    # Với giá trị biểu diễn đúng được thì áp dụng quy tắc làm
    # tròn tới số chẵn: 60,25 ra 60.2 chứ không ra 60.3.
    assert dinh_dang(60.25) == "60.2"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Giá trị ngoài miền phải bị chặn, kèm tên đại lượng sai.
    da_chan = False
    try:
        dien_nang(7.5, 30.0)
    except ValueError as loi:
        da_chan = "gio_chay" in str(loi)
    assert da_chan, "gio chay ngoai mien ma van tinh duoc"
    # Chuỗi không phải số thì phép ép kiểu báo lỗi.
    da_chan_2 = False
    try:
        float("bay phay nam")
    except ValueError:
        da_chan_2 = True
    assert da_chan_2, "chuoi khong phai so ma van ep kieu duoc"

    print("BT 2.3")
    for cong_suat, gio in ((7.5, 8.0), (7.5, 0.0)):
        print(f"  {cong_suat} kW, {gio} h -> "
              f"{dinh_dang(dien_nang(cong_suat, gio))} kWh")
