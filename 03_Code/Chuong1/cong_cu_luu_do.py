# -*- coding: utf-8 -*-
"""
Mã bài      : công cụ dùng chung cho lời giải Chương 1
Chương, mục : Chương 1, Mục 1.3.1
Đề bài      : Mô tả một lưu đồ bằng dữ liệu rồi kiểm năm quy tắc
              nối ở Bảng quy tắc của Mục 1.3.1. Dùng cho lời giải
              Bài tập 1.2 và Bài tập 1.4. Tệp này là công cụ của
              người soạn, không in vào sách.
Đầu vào     : từ điển các khối và danh sách các cạnh nối
Đầu ra      : danh sách số thứ tự quy tắc bị vi phạm
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

DANG_KHOI_HOP_LE = (
    "bat_dau", "ket_thuc", "nhap", "xuat", "xu_ly", "dieu_kien",
    "noi_trang",
)
NHAN_DIEU_KIEN = ("Dung", "Sai")


def kiem_quy_tac_1(cac_khoi):
    """Quy tắc 1: đúng một khối bắt đầu."""
    so_bat_dau = sum(
        1 for dang in cac_khoi.values() if dang == "bat_dau"
    )
    return so_bat_dau == 1


def cac_khoi_toi_duoc_ket_thuc(cac_khoi, cac_canh):
    """Tập khối có đường đi dẫn tới một khối kết thúc."""
    toi_duoc = {
        ma for ma, dang in cac_khoi.items() if dang == "ket_thuc"
    }
    da_doi = True
    while da_doi:
        da_doi = False
        for tu_khoi, den_khoi, _ in cac_canh:
            if den_khoi in toi_duoc and tu_khoi not in toi_duoc:
                toi_duoc.add(tu_khoi)
                da_doi = True
    return toi_duoc


def kiem_quy_tac_2(cac_khoi, cac_canh):
    """Quy tắc 2: mọi nhánh đều dẫn tới một khối kết thúc."""
    toi_duoc = cac_khoi_toi_duoc_ket_thuc(cac_khoi, cac_canh)
    return set(cac_khoi) == toi_duoc


def kiem_quy_tac_3(cac_khoi, cac_canh):
    """Quy tắc 3: khối điều kiện có đúng hai lối ra khác nhau."""
    for ma, dang in cac_khoi.items():
        if dang != "dieu_kien":
            continue
        loi_ra = [
            (den_khoi, nhan)
            for tu_khoi, den_khoi, nhan in cac_canh
            if tu_khoi == ma
        ]
        if len(loi_ra) != 2:
            return False
        if {nhan for _, nhan in loi_ra} != set(NHAN_DIEU_KIEN):
            return False
        if loi_ra[0][0] == loi_ra[1][0]:
            return False
    return True


def kiem_quy_tac_4(cac_canh):
    """Quy tắc 4: không có hai cạnh nối cùng một cặp khối.

    Kiểm hình học của mũi tên cắt nhau cần toạ độ, nằm ngoài
    phạm vi công cụ này. Dấu hiệu dò được bằng dữ liệu là hai
    cạnh trùng nhau, vốn luôn vẽ thành hai mũi tên chồng lên.
    """
    cap = [(tu_khoi, den_khoi) for tu_khoi, den_khoi, _ in cac_canh]
    return len(cap) == len(set(cap))


def kiem_quy_tac_5(cac_khoi, cac_canh):
    """Quy tắc 5: mỗi khối không phải điều kiện có đúng một lối
    ra, trừ khối kết thúc không có lối ra nào."""
    for ma, dang in cac_khoi.items():
        if dang in ("dieu_kien", "ket_thuc"):
            continue
        so_loi_ra = sum(
            1 for tu_khoi, _, _ in cac_canh if tu_khoi == ma
        )
        if so_loi_ra != 1:
            return False
    for ma, dang in cac_khoi.items():
        if dang != "ket_thuc":
            continue
        if any(tu_khoi == ma for tu_khoi, _, _ in cac_canh):
            return False
    return True


def kiem_luu_do(cac_khoi, cac_canh):
    """Trả về danh sách số thứ tự quy tắc bị vi phạm, đã sắp xếp.

    cac_khoi: {ma_khoi: dang_khoi}
    cac_canh: [(tu_khoi, den_khoi, nhan)] với nhan là chuỗi rỗng
              khi cạnh không xuất phát từ khối điều kiện.
    Phát sinh ValueError khi gặp dạng khối ngoài bảy dạng hợp lệ.
    """
    for ma, dang in cac_khoi.items():
        if dang not in DANG_KHOI_HOP_LE:
            raise ValueError(f"dang khoi khong hop le o {ma}: {dang}")
    vi_pham = []
    if not kiem_quy_tac_1(cac_khoi):
        vi_pham.append(1)
    if not kiem_quy_tac_2(cac_khoi, cac_canh):
        vi_pham.append(2)
    if not kiem_quy_tac_3(cac_khoi, cac_canh):
        vi_pham.append(3)
    if not kiem_quy_tac_4(cac_canh):
        vi_pham.append(4)
    if not kiem_quy_tac_5(cac_khoi, cac_canh):
        vi_pham.append(5)
    return vi_pham


def so_khoi(cac_khoi):
    """Số khối của lưu đồ."""
    return len(cac_khoi)


if __name__ == "__main__":
    # Trường hợp thường: lưu đồ tuần tự ba khối, hợp lệ.
    khoi_tot = {
        "bd": "bat_dau", "nhap": "nhap", "tinh": "xu_ly",
        "xuat": "xuat", "kt": "ket_thuc",
    }
    canh_tot = [
        ("bd", "nhap", ""), ("nhap", "tinh", ""),
        ("tinh", "xuat", ""), ("xuat", "kt", ""),
    ]
    assert kiem_luu_do(khoi_tot, canh_tot) == [], \
        kiem_luu_do(khoi_tot, canh_tot)
    assert so_khoi(khoi_tot) == 5

    # Trường hợp biên: khối điều kiện có đúng hai lối ra khác
    # nhau là hợp lệ, nhưng hai lối ra trỏ cùng một khối thì sai.
    khoi_re = dict(khoi_tot, kiem="dieu_kien")
    canh_re = [
        ("bd", "nhap", ""), ("nhap", "kiem", ""),
        ("kiem", "tinh", "Dung"), ("kiem", "xuat", "Sai"),
        ("tinh", "xuat", ""), ("xuat", "kt", ""),
    ]
    assert kiem_luu_do(khoi_re, canh_re) == []
    canh_trung = [
        ("bd", "nhap", ""), ("nhap", "kiem", ""),
        ("kiem", "xuat", "Dung"), ("kiem", "xuat", "Sai"),
        ("tinh", "xuat", ""), ("xuat", "kt", ""),
    ]
    assert 3 in kiem_luu_do(khoi_re, canh_trung)

    # Nhánh quay về chính nó thì không bao giờ tới khối kết thúc,
    # nên vi phạm quy tắc 2. Nhánh quay về khối điều kiện thì vẫn
    # tới được, nên không vi phạm; đây là chỗ hai trường hợp khác
    # nhau mà nhìn hình vẽ dễ lẫn.
    khoi_cut = {
        "bd": "bat_dau", "kiem": "dieu_kien", "a": "xu_ly",
        "kt": "ket_thuc",
    }
    canh_cut = [
        ("bd", "kiem", ""), ("kiem", "kt", "Dung"),
        ("kiem", "a", "Sai"), ("a", "a", ""),
    ]
    assert 2 in kiem_luu_do(khoi_cut, canh_cut), \
        kiem_luu_do(khoi_cut, canh_cut)
    canh_quay_ve = [
        ("bd", "kiem", ""), ("kiem", "kt", "Dung"),
        ("kiem", "a", "Sai"), ("a", "kiem", ""),
    ]
    assert kiem_luu_do(khoi_cut, canh_quay_ve) == []

    # Trường hợp ngoại lệ: dạng khối ngoài bảy dạng hợp lệ.
    da_chan = False
    try:
        kiem_luu_do({"x": "hinh_sao"}, [])
    except ValueError:
        da_chan = True
    assert da_chan, "dang khoi khong hop le ma van chay"

    print("cong_cu_luu_do: moi khang dinh dat")
