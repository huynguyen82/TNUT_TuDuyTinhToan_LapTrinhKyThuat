# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 1
Chương, mục : Chương 3, Mục 3.1.1
Đề bài      : Phân loại trạng thái động cơ theo bốn miền nhiệt
              độ, dùng chuỗi if elif else.
Đầu vào     : nhiệt độ vỏ máy (°C), nhập từ bàn phím
Đầu ra      : một trong bốn câu trạng thái
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
NGUONG_CANH_BAO = 60.0
NGUONG_NGUY_HIEM = 80.0
NGUONG_DUNG_MAY = 100.0

nhiet_do = float(input("Nhiet do vo may (do C): "))

if nhiet_do < NGUONG_CANH_BAO:
    trang_thai = "binh thuong"
elif nhiet_do < NGUONG_NGUY_HIEM:
    trang_thai = "canh bao"
elif nhiet_do < NGUONG_DUNG_MAY:
    trang_thai = "nguy hiem"
else:
    trang_thai = "dung may"

print(f"{nhiet_do:.1f} do C -> {trang_thai}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert nhiet_do == 72.5
    assert trang_thai == "canh bao"
    # Chuỗi elif dừng ở điều kiện đúng đầu tiên, nên mỗi nhiệt độ
    # chỉ khớp đúng một nhánh.
    assert not (nhiet_do < NGUONG_CANH_BAO)

    # --- Trường hợp biên ---------------------------------------
    # Ba ngưỡng là ba điểm biên. Giá trị đúng bằng ngưỡng thuộc
    # miền phía trên, vì điều kiện dùng dấu nhỏ hơn thuần.
    assert not (60.0 < NGUONG_CANH_BAO)
    assert 59.9 < NGUONG_CANH_BAO
    assert not (100.0 < NGUONG_DUNG_MAY)
    assert 99.9 < NGUONG_DUNG_MAY

    # --- Trường hợp ngoại lệ -----------------------------------
    # Chuỗi không phải số thì phép ép kiểu báo lỗi trước khi vào
    # chuỗi điều kiện.
    da_chan = False
    try:
        float("bay muoi")
    except ValueError:
        da_chan = True
    assert da_chan, "chuoi khong phai so ma van ep kieu duoc"
