# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 4
Chương, mục : Chương 4, Mục 4.2.1
Đề bài      : Ba hàm nhỏ của bộ bốn hàm tách từ chương trình
              theo dõi ca trực của Bài tập 3.9. Hàm đếm nằm ở
              Ví dụ 5.
Đầu vào     : các số đo cố định trong mã
Đầu ra      : kết quả của ba hàm với vài số đo mẫu
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
NGUONG = (60.0, 80.0, 100.0)
KET_THUC = -1.0


def la_ket_thuc(so_do):
    """So do co phai gia tri ket thuc hay khong."""
    return so_do == KET_THUC


def la_so_do_loi(so_do):
    """So do co phai loi cam bien hay khong."""
    return so_do < 0 and not la_ket_thuc(so_do)


def phan_loai(nhiet_do):
    """Trang thai theo bon mien cua Muc 3.1.1."""
    if nhiet_do < NGUONG[0]:
        return "binh thuong"
    elif nhiet_do < NGUONG[1]:
        return "canh bao"
    elif nhiet_do < NGUONG[2]:
        return "nguy hiem"
    return "dung may"
# --- het-in-sach ---


print(f"la_ket_thuc(-1.0)   {la_ket_thuc(-1.0)}")
print(f"la_so_do_loi(-5.0)  {la_so_do_loi(-5.0)}")
print(f"la_so_do_loi(-1.0)  {la_so_do_loi(-1.0)}")
print(f"phan_loai(45.0)     {phan_loai(45.0)}")
print(f"phan_loai(60.0)     {phan_loai(60.0)}")
print(f"phan_loai(120.0)    {phan_loai(120.0)}")


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert la_ket_thuc(-1.0) is True
    assert la_so_do_loi(-5.0) is True
    assert phan_loai(45.0) == "binh thuong"

    # --- Trường hợp biên ---------------------------------------
    # Ba ngưỡng là ba điểm biên của Mục 3.3.1.
    assert phan_loai(59.9) == "binh thuong"
    assert phan_loai(60.0) == "canh bao"
    assert phan_loai(79.9) == "canh bao"
    assert phan_loai(80.0) == "nguy hiem"
    assert phan_loai(99.9) == "nguy hiem"
    assert phan_loai(100.0) == "dung may"
    # Giá trị kết thúc không bị tính là số đo lỗi.
    assert la_so_do_loi(-1.0) is False
    assert la_ket_thuc(-1.1) is False
    assert la_so_do_loi(0.0) is False

    # --- Trường hợp ngoại lệ -----------------------------------
    # phan_loai không chặn nhiệt độ ngoài miền đo được; đây là
    # giới hạn đã biết, xem Khối 8.
    assert phan_loai(1000.0) == "dung may"
    # So sánh một chuỗi với ngưỡng số phải báo lỗi.
    da_chan = False
    try:
        phan_loai("45.0")
    except TypeError:
        da_chan = True
    assert da_chan, "doi so khong phai so ma van phan loai duoc"
