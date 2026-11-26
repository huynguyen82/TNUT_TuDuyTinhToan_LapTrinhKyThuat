# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 1
Chương, mục : Chương 2, Mục 2.1.1
Đề bài      : Chuyển phần tính điện năng của mã giả Bài tập 1.9
              thành chương trình Python cho một động cơ, dùng
              biến và phép gán.
Đầu vào     : công suất (kW) và số giờ chạy (h), viết thẳng
              trong mã
Đầu ra      : điện năng tiêu thụ trong một ngày (kWh)
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
# Dong co so 1 cua phan xuong, theo Bang du lieu Chuong 1.
cong_suat_kw = 7.5
gio_chay = 8.0

# Dien nang mot ngay, don vi kWh.
dien_nang_kwh = cong_suat_kw * gio_chay

print("Cong suat (kW):", cong_suat_kw)
print("So gio chay (h):", gio_chay)
print("Dien nang (kWh):", dien_nang_kwh)
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert dien_nang_kwh == 60.0, dien_nang_kwh
    assert cong_suat_kw * gio_chay == 60.0

    # --- Trường hợp biên ---------------------------------------
    # Số giờ chạy bằng 0 cho điện năng bằng 0.
    assert 7.5 * 0.0 == 0.0
    # Động cơ chạy đủ 24 giờ cho mức lớn nhất trong một ngày.
    assert 7.5 * 24.0 == 180.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dùng một tên biến chưa gán phải phát sinh NameError; đây là
    # lỗi L2.1-2 của Mục 2.1.1.
    da_chan = False
    try:
        print(cong_suat_kv)  # noqa: F821
    except NameError:
        da_chan = True
    assert da_chan, "ten bien chua gan ma van dung duoc"
