# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 6
Chương, mục : Chương 2, Mục 2.4.2
Đề bài      : Đo sai số của phép cộng dồn số thực và so sánh ba
              cách cộng một dãy, rồi kiểm dung sai bằng
              math.isclose thay cho dấu bằng.
Đầu vào     : dãy 1 000 số đo, mỗi số 0,1; viết thẳng trong mã
Đầu ra      : giá trị ba cách cộng, sai số tuyệt đối, kết luận
              dung sai
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

import math

# --- in-sach ---
day_so_do = [0.1] * 1000
gia_tri_dung = math.fsum(day_so_do)

tong_vong_lap = 0.0
for so_do in day_so_do:
    tong_vong_lap = tong_vong_lap + so_do

print("vong lap:", tong_vong_lap)
print("sum     :", sum(day_so_do))
print("fsum    :", math.fsum(day_so_do))
print("sai so tuyet doi cua vong lap:",
      abs(tong_vong_lap - gia_tri_dung))

# Kiem dung sai: so bang dau bang va so bang math.isclose.
tong_dung_sai = 50.00
for _ in range(10):
    tong_dung_sai = tong_dung_sai + 0.01
print("cong don  :", tong_dung_sai)
print("bang 50.1 :", tong_dung_sai == 50.10)
print("isclose   :", math.isclose(tong_dung_sai, 50.10,
                                  abs_tol=1e-9))
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert gia_tri_dung == 100.0
    assert abs(tong_vong_lap - gia_tri_dung) > 0.0
    # Từ Python 3.12, sum cộng dãy toàn số thực bằng thuật toán
    # bù sai số nên cho đúng kết quả, ngang math.fsum.
    assert sum(day_so_do) == gia_tri_dung
    assert math.fsum(day_so_do) == gia_tri_dung
    assert tong_dung_sai != 50.10
    assert math.isclose(tong_dung_sai, 50.10, abs_tol=1e-9)

    # --- Trường hợp biên ---------------------------------------
    # Cộng đúng một lần thì chưa có sai số tích luỹ.
    assert 0.0 + 0.1 == 0.1
    # math.isclose với rel_tol mặc định không dùng được cho số
    # gần 0: phải dùng abs_tol. Đây là lỗi L2.4-6 của Mục 2.4.2.
    assert not math.isclose(1e-12, 0.0)
    assert math.isclose(1e-12, 0.0, abs_tol=1e-9)
    # Ngưỡng phải lấy từ dung sai của bài toán, không lấy mặc
    # định: sai lệch 0,02 mm bị dung sai 0,05 mm chấp nhận.
    assert math.isclose(50.02, 50.00, abs_tol=0.05)
    assert not math.isclose(50.06, 50.00, abs_tol=0.05)

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ngưỡng âm không có nghĩa và phải bị chặn.
    da_chan = False
    try:
        math.isclose(1.0, 1.0, rel_tol=-0.1)
    except ValueError:
        da_chan = True
    assert da_chan, "rel_tol am ma van chay"
