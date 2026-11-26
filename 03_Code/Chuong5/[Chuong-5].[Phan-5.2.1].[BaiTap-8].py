# -*- coding: utf-8 -*-
"""
Mã bài      : BT 5.8
Chương, mục : Chương 5, Mục 5.2.1 và 5.4.1
Đề bài      : Chọn cấu trúc dữ liệu cho bốn tình huống, nêu độ
              phức tạp tiệm cận, rồi đo lại để xác nhận.
Đầu vào     : không có, bốn tình huống cố định trong mã
Đầu ra      : bốn lựa chọn kèm số đo xác nhận
Python      : 3.12
Thư viện    : numpy==2.1.3
Cài đặt     : pip install numpy==2.1.3

Lời giải trình bày ở tệp .md cùng tên.
"""

import timeit

import numpy as np

SO_LAN_LAP_LAI = 3


def mili_giay(ham, so_lan, so_lan_lap_lai=SO_LAN_LAP_LAI):
    """Thời gian một lần chạy, mili giây, nhỏ nhất của ba lần."""
    cac_lan = timeit.repeat(ham, number=so_lan,
                            repeat=so_lan_lap_lai)
    return min(cac_lan) / so_lan * 1000


def bon_cau_hoi(thu_tu_tu_nhien, co_ten_tu_nhien, cung_kieu,
                tinh_tren_ca_chuoi):
    """Cấu trúc dữ liệu suy ra từ bốn câu hỏi.

    Ba câu hỏi của Khối 4 Mục 5.2.1 chỉ chọn được giữa danh sách
    và từ điển. Chúng KHÔNG phân biệt được danh sách với mảng
    NumPy, vì cả hai đều dùng cho dữ liệu cùng kiểu không có tên
    tự nhiên. Câu hỏi thứ tư là câu phân biệt hai thứ đó: phép
    tính có áp lên cả chuỗi hay chỉ lấy từng phần tử.
    """
    if co_ten_tu_nhien and not thu_tu_tu_nhien:
        return "tu dien"
    if cung_kieu and not co_ten_tu_nhien and tinh_tren_ca_chuoi:
        return "mang NumPy"
    return "danh sach"


def day_so_do(so_phan_tu):
    """Dãy số đo giả lập có so_phan_tu phần tử."""
    mau = [31.2, 28.5, 26.0, 25.1, 48.6, 62.3, 71.5, 58.9]
    return (mau * (so_phan_tu // len(mau) + 1))[:so_phan_tu]


def bang_lon(so_dong):
    """Bảng giả lập có so_dong dòng."""
    cac_dong = []
    for thu_tu in range(so_dong):
        cac_dong.append((f"muc{thu_tu}", float(thu_tu)))
    return cac_dong


def tra_bang_duyet(bang, ten):
    """Tra cận dưới bằng duyệt danh sách, O(n)."""
    for thu_tu in range(len(bang)):
        if bang[thu_tu][0] == ten:
            return bang[thu_tu][1]
    return -1.0


def nhan_vong_lap(day, he_so):
    """Nhân cả chuỗi bằng vòng lặp Python, O(n)."""
    ra = []
    for gia_tri in day:
        ra.append(gia_tri * he_so)
    return ra


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Tinh huong 1: 720 so do theo gio. Thu tu la mot phan nghia.
    assert bon_cau_hoi(True, False, True, False) == "danh sach"
    day = day_so_do(720)
    t_chi_so = mili_giay(lambda: day[400], 2000)
    t_duyet = mili_giay(lambda: day.index(58.9), 2000)
    # Lay theo chi so la O(1), nhanh hon han duyet tim.
    assert t_chi_so < t_duyet

    # Tinh huong 2: bang 50 000 dong tra theo ten.
    assert bon_cau_hoi(False, True, False, False) == "tu dien"
    bang = bang_lon(50_000)
    tu_dien = dict(bang)
    ten = "muc49999"
    t_bang = mili_giay(lambda: tra_bang_duyet(bang, ten), 20)
    t_td = mili_giay(lambda: tu_dien.get(ten, -1.0), 2000)
    # Tu dien O(1) so voi duyet O(n). Chi khang dinh CHIEU, khong
    # khang dinh do lon: ty le do duoc dao dong tu khoang 10^3 den
    # 10^4 giua cac lan chay, nen mot nguong cu the se lam ca kiem
    # thu nay that bai that thuong. Ly do dao dong xem Phu luc 2.
    assert t_td < t_bang, (t_td, t_bang)
    assert t_bang / t_td > 100.0, t_bang / t_td

    # Tinh huong 3: nhan ca chuoi voi mot he so hieu chuan.
    assert bon_cau_hoi(True, False, True, True) == "mang NumPy"
    lon = day_so_do(72_000)
    mang = np.array(lon)
    t_lap = mili_giay(lambda: nhan_vong_lap(lon, 1.5), 20)
    t_np = mili_giay(lambda: mang * 1.5, 500)
    # Cung ly do: khang dinh chieu, khong khang dinh do lon.
    assert t_np < t_lap, (t_np, t_lap)

    # Tinh huong 4: bang co ca ten muc lan nong do.
    assert bon_cau_hoi(False, True, False, False) == "tu dien"
    # Ba cau hoi dau KHONG phan biet duoc tinh huong 1 voi 3:
    # ca hai cho (True, False, True). Cau hoi thu tu moi phan biet.
    assert (bon_cau_hoi(True, False, True, False)
            != bon_cau_hoi(True, False, True, True))

    # --- Trường hợp biên ---------------------------------------
    # Tu dien tra gan nhu khong doi theo quy mo bang.
    nho = dict(bang_lon(6))
    t_nho = mili_giay(lambda: nho.get("muc5", -1.0), 2000)
    assert max(t_nho, t_td) / min(t_nho, t_td) < 3.0
    # Duyet tang theo quy mo.
    bang_500 = bang_lon(500)
    t_500 = mili_giay(
        lambda: tra_bang_duyet(bang_500, "muc499"), 200)
    assert t_500 < t_bang
    # Quy mo hoa von cua NumPy thap: tu 720 phan tu da nhanh hon.
    nho_720 = np.array(day)
    t_lap_720 = mili_giay(lambda: nhan_vong_lap(day, 1.5), 50)
    t_np_720 = mili_giay(lambda: nho_720 * 1.5, 2000)
    assert t_np_720 < t_lap_720

    # --- Trường hợp ngoại lệ -----------------------------------
    # Bang co ca ten muc lan nong do: mang NumPy buoc cung kieu,
    # nen no KHONG giu duoc ban ghi hai kieu.
    hon_hop = np.array([("kem", 35.5)], dtype=object)
    assert hon_hop.dtype == object
    # Mang so thuc thi khong nhan duoc chuoi.
    da_chan = False
    try:
        np.array([1.0, 2.0]) + np.array(["a", "b"])
    except (ValueError, TypeError, np.exceptions.DTypePromotionError):
        da_chan = True
    assert da_chan, "cong mang so voi mang chuoi ma chay"
    # Cong hai mang khac do dai bao loi ve hinh dang.
    da_chan2 = False
    try:
        np.array([1.0, 2.0, 3.0]) + np.array([1.0, 2.0])
    except ValueError:
        da_chan2 = True
    assert da_chan2, "hai mang khac do dai ma cong duoc"

    print("tinh huong                      chon        do xac nhan")
    print(f"1. 720 so do theo gio           danh sach   "
          f"chi so {t_chi_so:.6f} ms < duyet {t_duyet:.6f} ms")
    print(f"2. bang 50 000 dong theo ten    tu dien     "
          f"duyet/tu dien = {t_bang / t_td:.0f} lan")
    print(f"3. nhan ca 72 000 so do         mang NumPy  "
          f"vong lap/numpy = {t_lap / t_np:.0f} lan")
    print(f"4. bang co ten muc va nong do   tu dien     "
          f"mang buoc cung kieu, dtype={hon_hop.dtype}")
    print(f"numpy {np.__version__}")
