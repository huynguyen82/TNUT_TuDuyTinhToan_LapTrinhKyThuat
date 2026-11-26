# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.3
Chương, mục : Chương 5, Mục 5.1.2
Đề bài      : Năm đại lượng của bài toán A5, mỗi đại lượng một
              hàm theo Mục 4.2.1.
Đầu vào     : 24 số đo (µg/m³), miền từ 0 đến 1 000
Đầu ra      : năm đại lượng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

NGUONG = 50.0
MIEN_NONG_DO = (0.0, 1000.0)
CAO_DIEM_SANG = (6, 9)

ngay = [
    31.2, 28.5, 26.0, 25.1, 27.4, 34.8,
    48.6, 62.3, 71.5, 58.9, 44.2, 39.7,
    36.1, 35.4, 38.0, 42.6, 51.3, 64.8,
    69.2, 55.7, 46.3, 40.1, 36.8, 33.5,
]


def kiem_day(day):
    """Chặn danh sách rỗng và số đo ngoài miền.

    Phát sinh ValueError trong cả hai trường hợp.
    """
    if len(day) == 0:
        raise ValueError("du lieu khong hop le: danh sach rong")
    for so_do in day:
        if not MIEN_NONG_DO[0] <= so_do <= MIEN_NONG_DO[1]:
            raise ValueError(
                f"du lieu khong hop le: so do = {so_do}")
    return True


def gio_cao_nhat(day):
    """Giờ có nồng độ cao nhất, và nồng độ đó."""
    kiem_day(day)
    cao = max(day)
    return day.index(cao), cao


def gio_thap_nhat(day):
    """Giờ có nồng độ thấp nhất, và nồng độ đó."""
    kiem_day(day)
    thap = min(day)
    return day.index(thap), thap


def trung_binh(day):
    """Nồng độ trung bình, µg/m³."""
    kiem_day(day)
    return sum(day) / len(day)


def dem_vuot_nguong(day, nguong=NGUONG):
    """Số giờ có nồng độ vượt ngưỡng, dùng dấu lớn hơn."""
    kiem_day(day)
    vuot = 0
    for so_do in day:
        if so_do > nguong:
            vuot = vuot + 1
    return vuot


def trung_binh_cao_diem(day, khoang=CAO_DIEM_SANG):
    """Nồng độ trung bình riêng khoảng giờ cao điểm."""
    doan = day[khoang[0]:khoang[1]]
    return trung_binh(doan)


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert gio_cao_nhat(ngay) == (8, 71.5)
    assert gio_thap_nhat(ngay) == (3, 25.1)
    assert f"{trung_binh(ngay):.2f}" == "43.67"
    assert dem_vuot_nguong(ngay) == 7
    assert f"{trung_binh_cao_diem(ngay):.2f}" == "60.80"

    # --- Trường hợp biên ---------------------------------------
    # So do dung bang nguong KHONG dem la vuot.
    assert dem_vuot_nguong([NGUONG]) == 0
    assert dem_vuot_nguong([50.1]) == 1
    # Mot phan tu: trung binh bang chinh no, cuc tri cung vay.
    assert trung_binh([42.6]) == 42.6
    assert gio_cao_nhat([42.6]) == (0, 42.6)
    # Cat lat ba gio cao diem cho dung ba phan tu.
    assert len(ngay[CAO_DIEM_SANG[0]:CAO_DIEM_SANG[1]]) == 3
    # Trung binh cao diem cao hon trung binh ngay.
    assert trung_binh_cao_diem(ngay) > trung_binh(ngay)
    # Trung binh ngay duoi nguong du 7 gio vuot nguong.
    assert trung_binh(ngay) < NGUONG and dem_vuot_nguong(ngay) > 0
    # So do bang hai can cua mien van hop le.
    assert kiem_day([0.0, 1000.0]) is True

    # --- Trường hợp ngoại lệ -----------------------------------
    # Danh sach rong: tung ham phat sinh ValueError rieng, nen
    # khoanh vung duoc ham nao gap du lieu rong.
    da_chan = 0
    cac_ham = (gio_cao_nhat, gio_thap_nhat, trung_binh,
               dem_vuot_nguong)
    for thu_tu in range(4):
        try:
            cac_ham[thu_tu]([])
        except ValueError:
            da_chan = da_chan + 1
    assert da_chan == 4, "co ham khong chan danh sach rong"
    # So do ngoai mien cung bi chan.
    da_chan2 = 0
    for thu_tu in range(2):
        try:
            trung_binh([(-1.0, 1001.0)[thu_tu]])
        except ValueError:
            da_chan2 = da_chan2 + 1
    assert da_chan2 == 2, "so do ngoai mien ma khong chan"

    gio_cao, nong_do_cao = gio_cao_nhat(ngay)
    gio_thap, nong_do_thap = gio_thap_nhat(ngay)
    print(f"gio cao nhat        : {gio_cao} ({nong_do_cao})")
    print(f"gio thap nhat       : {gio_thap} ({nong_do_thap})")
    print(f"trung binh ngay     : {trung_binh(ngay):.2f}")
    print(f"so gio vuot nguong  : {dem_vuot_nguong(ngay)}")
    print(f"trung binh cao diem : "
          f"{trung_binh_cao_diem(ngay):.2f}")
