# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 1
Chương, mục : Chương 5, Mục 5.1.1
Đề bài      : Lưu 24 số đo PM2.5 của một ngày vào một danh sách,
              lấy theo chỉ số và cắt lát ba giờ cao điểm sáng.
Đầu vào     : 24 số đo cố định trong mã
Đầu ra      : vài phần tử và một đoạn cắt lát
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
# 24 so do PM2.5 cua mot ngay, don vi microgram tren met khoi.
ngay = [
    31.2, 28.5, 26.0, 25.1, 27.4, 34.8,
    48.6, 62.3, 71.5, 58.9, 44.2, 39.7,
    36.1, 35.4, 38.0, 42.6, 51.3, 64.8,
    69.2, 55.7, 46.3, 40.1, 36.8, 33.5,
]

print(f"so gio do duoc : {len(ngay)}")
print(f"gio 0          : {ngay[0]}")
print(f"gio 6          : {ngay[6]}")
print(f"gio cuoi       : {ngay[-1]}")
cao_diem_sang = ngay[6:9]
print(f"cao diem sang  : {cao_diem_sang}")
print(f"so gio cao diem: {len(cao_diem_sang)}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert len(ngay) == 24
    assert ngay[0] == 31.2
    assert ngay[6] == 48.6
    assert cao_diem_sang == [48.6, 62.3, 71.5]

    # --- Trường hợp biên ---------------------------------------
    # Can tren cua cat lat khong thuoc doan, dung quy tac range.
    assert len(ngay[6:9]) == 3
    # Chi so am dem tu cuoi, nen ngay[-1] la ngay[23].
    assert ngay[-1] == ngay[23]
    assert ngay[-24] == ngay[0]
    # Cat lat vuot cuoi cho doan ngan hon, KHONG bao loi.
    assert len(ngay[20:30]) == 4
    # Cat lat nguoc cho danh sach RONG, cung khong bao loi.
    assert ngay[5:2] == []
    # Cat lat bo ca hai can cho ban sao ca danh sach.
    assert ngay[:] == ngay

    # --- Trường hợp ngoại lệ -----------------------------------
    # Chi so bang do dai danh sach bao loi: loi lech mot.
    da_chan = False
    try:
        ngay[24]
    except IndexError:
        da_chan = True
    assert da_chan, "chi so 24 tren danh sach 24 phan tu ma chay"
    # Chi so am vuot dau danh sach cung bao loi.
    da_chan2 = False
    try:
        ngay[-25]
    except IndexError:
        da_chan2 = True
    assert da_chan2, "chi so -25 ma van chay"
