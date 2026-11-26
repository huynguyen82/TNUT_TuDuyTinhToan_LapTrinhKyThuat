# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 2
Chương, mục : Chương 2, Mục 2.2.1
Đề bài      : Phiếu đo ghi kích thước chi tiết trục dưới dạng
              chuỗi. Ép kiểu sang số thực rồi so với hai cận của
              miền dung sai, và cho thấy bốn kiểu dữ liệu cơ bản
              cùng xuất hiện trong một bài toán.
Đầu vào     : chuỗi kích thước đo được, mm
Đầu ra      : kiểu của từng đại lượng và kết luận đạt hay không
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
# Phieu do ghi kich thuoc duoi dang chuoi.
kich_thuoc_chuoi = "50.03"
kich_thuoc_mm = float(kich_thuoc_chuoi)

so_chi_tiet = 12          # so nguyen
danh_nghia_mm = 50.00     # so thuc
dung_sai_mm = 0.05        # so thuc

can_duoi = danh_nghia_mm - dung_sai_mm
can_tren = danh_nghia_mm + dung_sai_mm
dat = can_duoi <= kich_thuoc_mm <= can_tren   # gia tri lo-gic

print("kich_thuoc_chuoi:", type(kich_thuoc_chuoi))
print("kich_thuoc_mm   :", type(kich_thuoc_mm))
print("so_chi_tiet     :", type(so_chi_tiet))
print("dat             :", type(dat))
print("Ket luan:", dat)
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert kich_thuoc_mm == 50.03
    assert isinstance(kich_thuoc_chuoi, str)
    assert isinstance(kich_thuoc_mm, float)
    assert isinstance(so_chi_tiet, int)
    assert isinstance(dat, bool)
    assert dat is True

    # --- Trường hợp biên ---------------------------------------
    # Kích thước đúng ở hai cận của miền dung sai vẫn đạt.
    assert can_duoi <= 49.95 <= can_tren
    assert can_duoi <= 50.05 <= can_tren
    # Ngoài miền thì không đạt.
    assert not can_duoi <= 50.06 <= can_tren
    # So hai chuỗi số theo thứ tự ký tự cho kết quả khác với so
    # hai số; đây là lỗi L2.2-3 của Mục 2.2.1.
    assert "9" > "10"
    assert not 9 > 10

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ép chuỗi có phần thập phân sang số nguyên phải báo lỗi.
    da_chan = False
    try:
        int("50.03")
    except ValueError:
        da_chan = True
    assert da_chan, "int cua chuoi thap phan ma van chay"
    # Chuỗi dùng dấu phẩy thập phân cũng không ép kiểu được.
    da_chan_2 = False
    try:
        float("50,03")
    except ValueError:
        da_chan_2 = True
    assert da_chan_2, "float cua chuoi co dau phay ma van chay"
