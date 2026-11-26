# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 6
Chương, mục : Chương 3, Mục 3.3.1
Đề bài      : Hai vòng lặp khác nhau đúng một ký tự ở cận trên
              của range. Cả hai chạy không báo lỗi; chỉ dữ liệu
              ở điểm biên mới phân biệt được cái nào sai.
Đầu vào     : số phần tử n, nhập từ bàn phím
Đầu ra      : hai tổng và chênh lệch giữa chúng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
so_phan_tu = int(input("So phan tu n: "))

tong_thieu = 0
for chi_so in range(1, so_phan_tu):
    tong_thieu = tong_thieu + chi_so

tong_du = 0
for chi_so in range(1, so_phan_tu + 1):
    tong_du = tong_du + chi_so

print(f"range(1, n)     cho {tong_thieu}")
print(f"range(1, n + 1) cho {tong_du}")
print(f"Chenh lech      {tong_du - tong_thieu}")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_phan_tu == 10
    assert tong_thieu == 45, tong_thieu
    assert tong_du == 55, tong_du
    # Chênh lệch luôn đúng bằng phần tử cuối bị bỏ sót.
    assert tong_du - tong_thieu == so_phan_tu

    # --- Trường hợp biên ---------------------------------------
    # Quan hệ trên đúng với mọi n, nên nó là phép kiểm nhanh.
    for so_may in (1, 2, 3, 10, 100):
        thieu = sum(range(1, so_may))
        du = sum(range(1, so_may + 1))
        assert du - thieu == so_may, so_may
    # Với n = 1 hai cách cho 0 và 1, tức lệch 100 phần trăm; đây
    # là ca biên phân biệt hai đoạn mã rõ nhất.
    assert sum(range(1, 1)) == 0
    assert sum(range(1, 2)) == 1
    # Với n lớn hai cách chỉ lệch một phần nhỏ, nên dữ liệu
    # thông thường không phân biệt được: ở n = 100 chênh lệch
    # chỉ chiếm dưới 2 phần trăm tổng đúng.
    assert (100 / sum(range(1, 101))) < 0.02
    # Dãy rỗng: cả hai cách đều chạy 0 lượt khi n bằng 0.
    assert sum(range(1, 0)) == sum(range(1, 1)) == 0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Cận của range phải là số nguyên; số thực bị chặn.
    da_chan = False
    try:
        range(1, 10.0)
    except TypeError:
        da_chan = True
    assert da_chan, "can cua range la so thuc ma van chay"
