# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.1
Chương, mục : Chương 5, Mục 5.1.1
Đề bài      : Dự đoán bốn phép cắt lát, trong đó hai phép vượt
              ra ngoài danh sách mà không báo lỗi.
Đầu vào     : không có, 24 số đo cố định trong mã
Đầu ra      : bốn đoạn cắt lát và số phần tử của từng đoạn
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

ngay = [
    31.2, 28.5, 26.0, 25.1, 27.4, 34.8,
    48.6, 62.3, 71.5, 58.9, 44.2, 39.7,
    36.1, 35.4, 38.0, 42.6, 51.3, 64.8,
    69.2, 55.7, 46.3, 40.1, 36.8, 33.5,
]


def bon_doan(day):
    """Bốn đoạn cắt lát của đề bài."""
    return day[6:9], day[20:30], day[5:2], day[-3:]


def co_bao_loi(day, chi_so):
    """Lấy một phần tử theo chỉ số có báo lỗi hay không."""
    try:
        day[chi_so]
    except IndexError:
        return True
    return False


if __name__ == "__main__":
    cao_diem, vuot_cuoi, nguoc, ba_cuoi = bon_doan(ngay)

    # --- Trường hợp thường -------------------------------------
    # Doan trong long danh sach: cho dung so phan tu mong doi.
    assert cao_diem == [48.6, 62.3, 71.5]
    assert len(cao_diem) == 3
    # Can tren 9 KHONG thuoc doan, nen 3 phan tu chu khong phai 4.
    assert len(ngay[6:9]) == 9 - 6
    # Ba phan tu cuoi bang chi so am.
    assert ba_cuoi == [40.1, 36.8, 33.5]

    # --- Trường hợp biên ---------------------------------------
    # Can tren 30 vuot cuoi danh sach 24 phan tu: 4 phan tu,
    # KHONG bao loi.
    assert vuot_cuoi == [46.3, 40.1, 36.8, 33.5]
    assert len(vuot_cuoi) == 4
    assert len(vuot_cuoi) == len(ngay) - 20
    # Hai can viet nguoc: danh sach RONG, cung khong bao loi.
    assert nguoc == []
    assert len(nguoc) == 0
    # Cat lat bo ca hai can cho ban sao ca danh sach.
    assert ngay[:] == ngay

    # --- Trường hợp ngoại lệ -----------------------------------
    # Cung chi so 24: cat lat im lang, lay phan tu thi bao loi.
    assert co_bao_loi(ngay, 24) is True
    assert co_bao_loi(ngay, 23) is False
    assert len(ngay[24:30]) == 0
    # Cung chi so -25: cung mot cach xu su.
    assert co_bao_loi(ngay, -25) is True
    assert len(ngay[-30:-24]) == 0

    ten_doan = ("ngay[6:9]", "ngay[20:30]", "ngay[5:2]",
                "ngay[-3:]")
    for thu_tu in range(4):
        doan = bon_doan(ngay)[thu_tu]
        print(f"{ten_doan[thu_tu]:<12}{len(doan)} phan tu  {doan}")
    print(f"ngay[24]     bao IndexError: "
          f"{co_bao_loi(ngay, 24)}")
    print(f"ngay[24:30]  cho {len(ngay[24:30])} phan tu, "
          f"khong bao loi")
