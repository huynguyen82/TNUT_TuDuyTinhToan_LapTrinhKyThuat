# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.4
Chương, mục : Chương 5, Mục 5.2.1
Đề bài      : Bảng mức chất lượng không khí bằng từ điển, hàm
              trả về tên mức của một nồng độ, và số phép so của
              hai cách tra ở ba quy mô bảng.
Đầu vào     : nồng độ (µg/m³), miền từ 0 đến 1 000
Đầu ra      : tên mức, và bảng so số phép so hai cách
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Số liệu bảng là giả định
của đề bài.
"""

MIEN_NONG_DO = (0.0, 1000.0)

can_duoi = {
    "tot": 0.0,
    "trung binh": 12.1,
    "kem": 35.5,
    "xau": 55.5,
    "rat xau": 150.5,
    "nguy hai": 250.5,
}


def ten_muc(nong_do, bang=can_duoi):
    """Tên mức chất lượng không khí của một nồng độ.

    Phát sinh ValueError khi nồng độ nằm ngoài miền đo được.
    """
    if not MIEN_NONG_DO[0] <= nong_do <= MIEN_NONG_DO[1]:
        raise ValueError(
            f"du lieu khong hop le: nong do = {nong_do}")
    ten = "tot"
    for khoa in bang:
        if nong_do >= bang[khoa]:
            ten = khoa
    return ten


def so_phep_so_duyet(bang_danh_sach, ten):
    """Số phép so khi tra bằng duyệt danh sách."""
    for thu_tu in range(len(bang_danh_sach)):
        if bang_danh_sach[thu_tu][0] == ten:
            return thu_tu + 1
    return len(bang_danh_sach)


def so_phep_so_tu_dien():
    """Số phép so khi tra bằng từ điển: luôn là 1."""
    return 1


def bang_lon(so_dong):
    """Bảng giả lập có so_dong dòng, để so theo quy mô."""
    cac_dong = []
    for thu_tu in range(so_dong):
        cac_dong.append((f"muc{thu_tu}", float(thu_tu)))
    return cac_dong


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert ten_muc(43.67) == "kem"
    assert ten_muc(5.0) == "tot"
    assert ten_muc(200.0) == "rat xau"
    assert ten_muc(300.0) == "nguy hai"
    # Hai cach tra cho cung ket qua tren moi khoa cua bang.
    bang = list(can_duoi.items())
    for khoa in can_duoi:
        tim = -1.0
        for thu_tu in range(len(bang)):
            if bang[thu_tu][0] == khoa:
                tim = bang[thu_tu][1]
        assert tim == can_duoi[khoa]

    # --- Trường hợp biên ---------------------------------------
    # Nong do dung bang can duoi thuoc muc do, ca sau muc.
    assert ten_muc(0.0) == "tot"
    assert ten_muc(12.1) == "trung binh"
    assert ten_muc(35.5) == "kem"
    assert ten_muc(55.5) == "xau"
    assert ten_muc(150.5) == "rat xau"
    assert ten_muc(250.5) == "nguy hai"
    # Nhich xuong duoi can duoi thi ve muc truoc.
    assert ten_muc(35.4) == "trung binh"
    # So phep so cua tu dien KHONG doi theo quy mo bang.
    assert so_phep_so_tu_dien() == 1
    # So phep so cua duyet tang theo quy mo: khoa cuoi bang.
    for so_dong in (6, 500, 50_000):
        lon = bang_lon(so_dong)
        assert so_phep_so_duyet(lon, f"muc{so_dong - 1}") == so_dong

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tra khoa khong co: ba cach, ba hanh vi khac nhau.
    da_chan = False
    try:
        can_duoi["cuc xau"]
    except KeyError:
        da_chan = True
    assert da_chan, "tra khoa khong co bang ngoac vuong ma chay"
    assert can_duoi.get("cuc xau", -1.0) == -1.0
    assert can_duoi.get("cuc xau") is None
    # Nong do ngoai mien bi chan.
    da_chan2 = 0
    for thu_tu in range(2):
        try:
            ten_muc((-1.0, 1001.0)[thu_tu])
        except ValueError:
            da_chan2 = da_chan2 + 1
    assert da_chan2 == 2, "nong do ngoai mien ma khong chan"

    print(f"nong do 43.67 -> muc {ten_muc(43.67)}")
    print(f"nong do 35.50 -> muc {ten_muc(35.5)}")
    print()
    print("so dong   duyet   tu dien")
    for so_dong in (6, 500, 50_000):
        lon = bang_lon(so_dong)
        duyet = so_phep_so_duyet(lon, f"muc{so_dong - 1}")
        print(f"{so_dong:>7}{duyet:>8}{so_phep_so_tu_dien():>10}")
