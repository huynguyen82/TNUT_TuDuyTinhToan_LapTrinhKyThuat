# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.7
Chương, mục : Chương 3, Mục 3.3.1
Đề bài      : Thiết kế ca kiểm thử phân biệt được hai đoạn mã
              khác nhau ở cận trên của range, lập bảng vết, chỉ
              ra đoạn sai và giải thích vì sao ca n = 100 không
              phân biệt được.
Đầu vào     : quyền chọn giá trị n bất kỳ
Đầu ra      : giá trị n đã chọn, hai kết quả, tỉ lệ chênh lệch
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""


def tong_can_thieu(so_phan_tu):
    """Đoạn mã dùng range(1, n): bỏ sót phần tử cuối."""
    tong = 0
    for chi_so in range(1, so_phan_tu):
        tong = tong + chi_so
    return tong


def tong_can_du(so_phan_tu):
    """Đoạn mã dùng range(1, n + 1): đủ mọi phần tử."""
    tong = 0
    for chi_so in range(1, so_phan_tu + 1):
        tong = tong + chi_so
    return tong


def ket_qua_dung(so_phan_tu):
    """Kết quả đúng tính bằng công thức, không qua vòng lặp.

    Lập theo đặc tả chứ không theo chương trình, đúng bước 1
    của quy trình truy vết đối chiếu ở Mục 1.5.1.
    """
    return so_phan_tu * (so_phan_tu + 1) // 2


def ti_le_chenh(so_phan_tu):
    """Tỉ lệ chênh lệch giữa hai đoạn so với kết quả đúng."""
    dung = ket_qua_dung(so_phan_tu)
    if dung == 0:
        return 0.0
    return (tong_can_du(so_phan_tu)
            - tong_can_thieu(so_phan_tu)) / dung


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Ca n = 1 la ca bien phan biet ro nhat.
    assert tong_can_thieu(1) == 0
    assert tong_can_du(1) == 1
    assert ket_qua_dung(1) == 1
    assert ti_le_chenh(1) == 1.0
    # Doan dung can thieu cho ket qua sai o ca nay.
    assert tong_can_thieu(1) != ket_qua_dung(1)
    assert tong_can_du(1) == ket_qua_dung(1)

    # --- Trường hợp biên ---------------------------------------
    # Chenh lech luon dung bang phan tu bi bo sot.
    for so_may in (1, 2, 3, 10, 100):
        assert (tong_can_du(so_may) - tong_can_thieu(so_may)
                == so_may), so_may
        assert tong_can_du(so_may) == ket_qua_dung(so_may)
    # Ti le chenh giam khi n tang, nen ca lon che loi.
    assert ti_le_chenh(1) == 1.0
    assert abs(ti_le_chenh(3) - 0.5) < 1e-12
    assert ti_le_chenh(100) < 0.02
    truoc = 2.0
    for so_may in (1, 3, 10, 100):
        hien = ti_le_chenh(so_may)
        assert hien < truoc, so_may
        truoc = hien

    # --- Trường hợp ngoại lệ -----------------------------------
    # Ca n = 0 khong phan biet duoc hai doan: ca hai cho 0.
    assert tong_can_thieu(0) == tong_can_du(0) == 0
    assert ti_le_chenh(0) == 0.0

    print("BT 3.7")
    print(f"  {'n':>5}{'range(1,n)':>12}{'range(1,n+1)':>14}"
          f"{'dung':>8}{'ti le chenh':>14}")
    for so_may in (0, 1, 3, 10, 100):
        print(f"  {so_may:>5}{tong_can_thieu(so_may):>12}"
              f"{tong_can_du(so_may):>14}"
              f"{ket_qua_dung(so_may):>8}"
              f"{ti_le_chenh(so_may):>13.1%}")
