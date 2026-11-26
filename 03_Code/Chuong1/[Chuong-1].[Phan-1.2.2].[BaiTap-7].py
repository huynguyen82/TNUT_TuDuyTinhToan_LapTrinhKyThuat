# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.7
Chương, mục : Chương 1, Mục 1.2.2
Đề bài      : Cho ba đề bài cùng dạng cộng dồn rồi so với ngưỡng.
              Viết một đặc tả chung cho các đề khớp được, chỉ rõ
              đề nào không khớp và vì sao, rồi chọn giữa giữ đặc
              tả chung và giữ ba đặc tả riêng.
Đầu vào     : các đề bài mô tả bằng dữ liệu, mỗi đề kèm đơn vị
Đầu ra      : danh sách đề khớp, danh sách đề không khớp, và số
              dòng đặc tả của hai phương án
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên.
"""

SO_DONG_DAC_TA = 6

# Mỗi đề bài mô tả bằng năm trường. Trường dang nhận một trong
# hai giá trị: cong_don khi bài toán cộng dồn rồi so tổng với
# ngưỡng, dem khi bài toán so từng phần tử rồi đếm.
DE_BAI = {
    "dien_nang": {
        "ten": "Tong dien nang mot nhom thiet bi",
        "day": [60.0, 90.0, 36.0],
        "don_vi": "kWh",
        "nguong": 200.0,
        "dang": "cong_don",
    },
    "luong_mua": {
        "ten": "Tong luong mua mot dot",
        "day": [18.0, 42.0, 31.0, 25.0],
        "don_vi": "mm",
        "nguong": 100.0,
        "dang": "cong_don",
    },
    "chi_phi": {
        "ten": "Tong chi phi mot don hang",
        "day": [1200.0, 850.0, 400.0],
        "don_vi": "nghin dong",
        "nguong": 2000.0,
        "dang": "cong_don",
    },
    "ngay_mua": {
        "ten": "So ngay mua vuot nguong",
        "day": [18.0, 42.0, 31.0, 25.0],
        "don_vi": "mm",
        "nguong": 30.0,
        "dang": "dem",
    },
}


def kiem_de_bai(de):
    """Kiểm một đề bài có đủ thông tin để viết đặc tả hay không.

    Phát sinh ValueError khi đề bài không ghi đơn vị, đúng như
    lỗi L1.2-4 của Mục 1.2.2.
    """
    if not de.get("don_vi"):
        raise ValueError(f"de bai thieu don vi: {de['ten']}")
    return True


def khop_dac_ta_chung(de, dang_chung="cong_don"):
    """Đề bài có khớp đặc tả chung của dạng đã cho hay không."""
    kiem_de_bai(de)
    return de["dang"] == dang_chung


def giai_cong_don(de):
    """Cộng dồn dãy số đo rồi so tổng với ngưỡng."""
    tong = sum(de["day"])
    return tong, tong > de["nguong"]


def giai_dem(de):
    """Đếm số phần tử của dãy vượt ngưỡng."""
    return sum(1 for so_do in de["day"] if so_do > de["nguong"])


def phan_loai(cac_de, dang_chung="cong_don"):
    """Trả về (danh sách mã đề khớp, danh sách mã đề không khớp)."""
    khop, khong_khop = [], []
    for ma, de in cac_de.items():
        (khop if khop_dac_ta_chung(de, dang_chung)
         else khong_khop).append(ma)
    return khop, khong_khop


def so_dong_phai_viet(so_de, dung_dac_ta_chung):
    """Số dòng đặc tả phải viết cho một số đề bài cùng dạng."""
    if dung_dac_ta_chung:
        return SO_DONG_DAC_TA
    return SO_DONG_DAC_TA * so_de


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    ba_de = {ma: DE_BAI[ma]
             for ma in ("dien_nang", "luong_mua", "chi_phi")}
    khop, khong_khop = phan_loai(ba_de)
    assert khop == ["dien_nang", "luong_mua", "chi_phi"], khop
    assert khong_khop == [], khong_khop
    assert so_dong_phai_viet(3, True) == 6
    assert so_dong_phai_viet(3, False) == 18
    # Ba đề cùng khớp nên một đặc tả chung sáu dòng là đủ.
    assert giai_cong_don(DE_BAI["dien_nang"]) == (186.0, False)
    assert giai_cong_don(DE_BAI["luong_mua"]) == (116.0, True)
    assert giai_cong_don(DE_BAI["chi_phi"]) == (2450.0, True)

    # --- Trường hợp biên ---------------------------------------
    # Thêm đề bài thứ tư dạng đếm: đề này không khớp đặc tả chung
    # thứ nhất, nên phải viết đặc tả chung thứ hai.
    khop_4, khong_khop_4 = phan_loai(DE_BAI)
    assert khong_khop_4 == ["ngay_mua"], khong_khop_4
    assert len(khop_4) == 3
    assert giai_dem(DE_BAI["ngay_mua"]) == 2
    # Gán bừa đề thứ tư vào đặc tả chung thứ nhất cho ra một câu
    # kết luận nghe hợp lý nhưng trả lời sai câu hỏi.
    tong_sai, vuot = giai_cong_don(DE_BAI["ngay_mua"])
    assert tong_sai == 116.0 and vuot is True
    assert giai_dem(DE_BAI["ngay_mua"]) != tong_sai
    # Số dòng tiết kiệm được tăng theo số đề cùng dạng.
    assert so_dong_phai_viet(300, False) == 1800
    assert so_dong_phai_viet(300, True) == 6

    # --- Trường hợp ngoại lệ -----------------------------------
    # Đề bài không ghi đơn vị thì chưa viết được đặc tả chung.
    da_chan = False
    try:
        khop_dac_ta_chung(dict(DE_BAI["dien_nang"], don_vi=""))
    except ValueError:
        da_chan = True
    assert da_chan, "de bai thieu don vi ma van viet duoc dac ta"

    print("BT 1.7")
    print(f"  Khop dac ta chung cong_don: {khop_4}")
    print(f"  Khong khop                : {khong_khop_4}")
    print(f"  So dong, ba dac ta rieng  : "
          f"{so_dong_phai_viet(3, False)}")
    print(f"  So dong, mot dac ta chung : "
          f"{so_dong_phai_viet(3, True)}")
