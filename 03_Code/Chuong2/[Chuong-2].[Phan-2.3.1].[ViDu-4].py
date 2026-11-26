# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 4
Chương, mục : Chương 2, Mục 2.3.1
Đề bài      : Nhập kích thước đo được từ bàn phím, kiểm dung sai
              và in phiếu kết quả theo đúng định dạng của bảng
              đặc tả: kích thước hai chữ số thập phân, các cột
              căn phải.
Đầu vào     : một dòng nhập từ bàn phím, kích thước đo được (mm)
Đầu ra      : phiếu kết quả ba dòng, kích thước hai chữ số thập
              phân
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Tệp .in cùng tên chứa dòng nhập mẫu, để lần chạy nào cũng cho
đúng một kết quả và kết quả in trong sách là kết quả chạy thật.
"""

# --- in-sach ---
DANH_NGHIA_MM = 50.00
DUNG_SAI_MM = 0.05

dong_nhap = input("Kich thuoc do duoc (mm): ")
kich_thuoc_mm = float(dong_nhap)

can_duoi = DANH_NGHIA_MM - DUNG_SAI_MM
can_tren = DANH_NGHIA_MM + DUNG_SAI_MM
dat = can_duoi <= kich_thuoc_mm <= can_tren

print(f"{'Mien hop le':<16}{can_duoi:>8.2f}{can_tren:>8.2f}")
print(f"{'Do duoc':<16}{kich_thuoc_mm:>8.2f}")
print(f"{'Ket luan':<16}{'dat' if dat else 'khong dat':>8}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert kich_thuoc_mm == 50.03
    assert dat is True
    assert f"{50.03:.2f}" == "50.03"

    # --- Trường hợp biên ---------------------------------------
    # Hai cận của miền dung sai vẫn đạt.
    assert can_duoi <= 49.95 <= can_tren
    assert can_duoi <= 50.05 <= can_tren
    # Làm tròn hiển thị không đổi giá trị: in ra một chữ số thập
    # phân vẫn giữ nguyên giá trị gốc. Đây là chỗ sinh lỗi
    # L2.3-3 khi cộng dồn các giá trị đã hiển thị.
    assert f"{50.05:.1f}" == "50.0"
    assert 50.05 != float(f"{50.05:.1f}")

    # --- Trường hợp ngoại lệ -----------------------------------
    # Người dùng gõ chữ thì phép ép kiểu phải báo lỗi; đây là
    # lỗi L2.3-2 của Mục 2.3.1.
    da_chan = False
    try:
        float("nam muoi")
    except ValueError:
        da_chan = True
    assert da_chan, "chuoi khong phai so ma van ep kieu duoc"
