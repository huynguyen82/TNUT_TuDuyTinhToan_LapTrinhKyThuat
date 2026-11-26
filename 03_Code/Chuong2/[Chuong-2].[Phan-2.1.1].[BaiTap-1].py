# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.1
Chương, mục : Chương 2, Mục 2.1.1
Đề bài      : Dự đoán giá trị in ra của một đoạn mã có gán đè
              biến, rồi chạy và đối chiếu.
Đầu vào     : đoạn mã sáu dòng, mô hình hoá bằng ba hàm
Đầu ra      : giá trị in ra ở dòng cuối
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Ba hàm dưới đây tái hiện
ba thứ tự dòng của ba bộ dữ liệu kiểm thử.
"""


def gan_de_truoc_khi_tinh():
    """Gán đè xảy ra trước dòng tính: giá trị mới được dùng."""
    cong_suat_kw = 7.5
    gio_chay = 8.0
    gio_chay = 10.0
    dien_nang_kwh = cong_suat_kw * gio_chay
    return dien_nang_kwh


def gan_de_sau_khi_tinh():
    """Gán đè xảy ra sau dòng tính: không ảnh hưởng kết quả."""
    cong_suat_kw = 7.5
    gio_chay = 8.0
    dien_nang_kwh = cong_suat_kw * gio_chay
    gio_chay = 10.0
    return dien_nang_kwh


def tinh_truoc_khi_gan():
    """Dòng tính đặt trước mọi phép gán: biến chưa tồn tại."""
    dien_nang_kwh = cong_suat_kw * gio_chay  # noqa: F821
    return dien_nang_kwh


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Gán đè trước dòng tính cho 75.0 chứ không phải 60.0.
    assert gan_de_truoc_khi_tinh() == 75.0
    assert 7.5 * 10.0 == 75.0
    # Chênh lệch so với dự đoán sai là 15,0 kWh.
    assert gan_de_truoc_khi_tinh() - 60.0 == 15.0

    # --- Trường hợp biên ---------------------------------------
    # Gán đè sau dòng tính không ảnh hưởng gì, vì phép gán ở dòng
    # tính đã lấy giá trị cũ ngay lúc dòng đó chạy.
    assert gan_de_sau_khi_tinh() == 60.0
    assert gan_de_sau_khi_tinh() != gan_de_truoc_khi_tinh()
    # Hai hàm chỉ khác nhau thứ tự hai dòng, không khác nội dung.

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dùng biến trước khi gán phải phát sinh NameError.
    da_chan = False
    try:
        tinh_truoc_khi_gan()
    except NameError as loi:
        da_chan = "cong_suat_kw" in str(loi)
    assert da_chan, "bien chua gan ma van dung duoc"

    print("BT 2.1")
    print(f"  Gan de truoc khi tinh: {gan_de_truoc_khi_tinh()}")
    print(f"  Gan de sau khi tinh  : {gan_de_sau_khi_tinh()}")
    print("  Tinh truoc khi gan   : NameError")
