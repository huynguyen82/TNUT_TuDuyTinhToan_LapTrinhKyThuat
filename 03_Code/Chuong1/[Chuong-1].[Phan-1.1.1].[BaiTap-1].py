# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.1
Chương, mục : Chương 1, Mục 1.1.1
Đề bài      : Điền bốn ô bị xoá trong bảng đặc tả ba phần của bài
              toán phân xưởng, và giải thích hậu quả khi thiếu
              mỗi ô.
Đầu vào     : bảng đặc tả thiếu bốn ô, cho trên giấy
Đầu ra      : bốn ô đã điền, mỗi ô kèm một câu giải thích
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên. Tệp này khẳng định
các con số mà lời giải viện dẫn, để không con số nào trong đáp
án là phỏng đoán.
"""

# Bốn ô đã điền, theo đúng Bảng đặc tả của Mục 1.1.1.
DAP_AN_BON_O = {
    "don_vi_dau_ra": "kWh",
    "so_chu_so_thap_phan": 1,
    "mien_gio_chay": (0.0, 24.0),
    "tra_ve_khi_rong": 0.0,
}

HE_SO_KWH_SANG_MJ = 3.6


def doi_kwh_sang_mj(dien_nang_kwh):
    """Đổi kilôoát giờ sang mêgajun. 1 kWh bằng 3,6 MJ."""
    return dien_nang_kwh * HE_SO_KWH_SANG_MJ


def dinh_dang_dau_ra(gia_tri, so_chu_so):
    """Trình bày một giá trị theo số chữ số thập phân đã khai báo."""
    return f"{gia_tri:.{so_chu_so}f}"


def dien_nang_mot_dong_co(cong_suat_kw, gio_chay):
    """Điện năng của một động cơ, kWh. Không kiểm miền giá trị.

    Dùng để cho thấy hậu quả khi ô miền giá trị bị bỏ trống.
    """
    return cong_suat_kw * gio_chay


def gio_chay_hop_le(gio_chay, mien=None):
    """Số giờ chạy có nằm trong miền đã khai báo hay không."""
    can_duoi, can_tren = mien or DAP_AN_BON_O["mien_gio_chay"]
    return can_duoi <= gio_chay <= can_tren


def tong_dien_nang(cac_dong_co):
    """Tổng điện năng, kWh. Danh sách rỗng trả về giá trị đã
    khai báo ở ô thứ tư, tức 0,0."""
    if not cac_dong_co:
        return DAP_AN_BON_O["tra_ve_khi_rong"]
    return sum(
        dien_nang_mot_dong_co(cong_suat, gio)
        for cong_suat, gio in cac_dong_co
    )


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Ô 1 và ô 2. Thiếu đơn vị thì cùng một giá trị đọc được
    # thành hai con số lệch nhau 3,6 lần.
    assert doi_kwh_sang_mj(384.0) == 1382.4
    assert doi_kwh_sang_mj(384.0) / 384.0 == HE_SO_KWH_SANG_MJ
    # Thiếu số chữ số thập phân thì hai cách trình bày cùng đúng.
    assert dinh_dang_dau_ra(384.0, 0) == "384"
    assert dinh_dang_dau_ra(384.0, 1) == "384.0"
    assert dinh_dang_dau_ra(
        384.0, DAP_AN_BON_O["so_chu_so_thap_phan"]) == "384.0"

    # Ô 3. Thiếu miền giá trị thì 30 giờ được chấp nhận và một
    # động cơ 7,5 kW cho ra 225,0 kWh trong một ngày.
    assert dien_nang_mot_dong_co(7.5, 30.0) == 225.0
    assert not gio_chay_hop_le(30.0)
    assert dien_nang_mot_dong_co(7.5, 24.0) == 180.0

    # --- Trường hợp biên ---------------------------------------
    # Hai đầu miền giờ chạy đều hợp lệ.
    assert gio_chay_hop_le(0.0)
    assert gio_chay_hop_le(24.0)
    assert not gio_chay_hop_le(24.1)
    # Ô 4. Danh sách rỗng trả về đúng 0,0 chứ không phải lỗi.
    assert tong_dien_nang([]) == 0.0
    assert dinh_dang_dau_ra(tong_dien_nang([]), 1) == "0.0"
    # Bộ năm động cơ của Bảng dữ liệu cho đúng 384,0 kWh.
    bo_nam = [(7.5, 8.0), (15.0, 6.0), (3.0, 12.0),
              (22.0, 4.0), (11.0, 10.0)]
    assert tong_dien_nang(bo_nam) == 384.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Số chữ số thập phân âm không phải là một đặc tả hợp lệ.
    da_chan = False
    try:
        dinh_dang_dau_ra(384.0, -1)
    except ValueError:
        da_chan = True
    assert da_chan, "so chu so am ma van dinh dang duoc"

    print("BT 1.1: bon o da dien")
    for ten, gia_tri in DAP_AN_BON_O.items():
        print(f"  {ten:<22}{gia_tri}")
