# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.5
Chương, mục : Chương 1, Mục 1.5.1
Đề bài      : Lập bảng vết thực thi cho mã giả tính trung bình
              cộng của một dãy số đo nồng độ bụi, trên hai bộ dữ
              liệu: dãy bốn số đo và dãy rỗng. Với dãy rỗng, chỉ
              ra bước nào không thực hiện được.
Đầu vào     : dãy số đo, µg/m³, miền từ 0 đến 500
Đầu ra      : bảng vết thực thi và giá trị trung bình cộng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên.
"""

MIEN_SO_DO = (0.0, 500.0)


def bang_vet_tong(day_so_do):
    """Bảng vết của vòng lặp cộng dồn trong mã giả.

    Trả về danh sách dòng (nhan_luot, i, so_do, tong, con_lap).
    Dòng đầu là dòng trước vòng lặp, theo khuôn Mục 1.5.1.
    """
    so_phan_tu = len(day_so_do)
    cac_dong = [("truoc vong lap", 0, None, 0.0, so_phan_tu > 0)]
    tong = 0.0
    for chi_so, so_do in enumerate(day_so_do, start=1):
        tong = tong + so_do
        cac_dong.append(
            (str(chi_so), chi_so, so_do, tong,
             chi_so < so_phan_tu)
        )
    return cac_dong


def trung_binh_cong(day_so_do):
    """Trung bình cộng của dãy số đo, µg/m³.

    Phát sinh ZeroDivisionError trên dãy rỗng, đúng như bước
    chia tổng cho số phần tử của mã giả.
    """
    return sum(day_so_do) / len(day_so_do)


def so_do_hop_le(so_do):
    """Số đo có nằm trong miền đã khai báo hay không."""
    return MIEN_SO_DO[0] <= so_do <= MIEN_SO_DO[1]


def in_bang_vet(ten, day_so_do):
    """In một bảng vết ra màn hình."""
    print(f"  Bang vet, {ten}: {day_so_do}")
    print(f"    {'luot':<16}{'i':>3}{'so do':>8}"
          f"{'tong':>9}  con_lap")
    for nhan, i, so_do, tong, con_lap in bang_vet_tong(day_so_do):
        chu_so_do = "-" if so_do is None else f"{so_do:.1f}"
        print(f"    {nhan:<16}{i:>3}{chu_so_do:>8}"
              f"{tong:>9.1f}  {con_lap}")


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    day_bon = [12.0, 18.0, 15.0, 21.0]
    bang_bon = bang_vet_tong(day_bon)
    assert len(bang_bon) == 5, len(bang_bon)
    assert bang_bon[0][3] == 0.0
    assert [dong[3] for dong in bang_bon[1:]] == [
        12.0, 30.0, 45.0, 66.0
    ]
    assert bang_bon[-1][4] is False
    assert trung_binh_cong(day_bon) == 16.5
    assert all(so_do_hop_le(so_do) for so_do in day_bon)

    # --- Trường hợp biên ---------------------------------------
    # Dãy một phần tử: bảng vết có đúng hai dòng, và điều kiện
    # dừng đã sai ngay sau lượt đầu tiên.
    bang_mot = bang_vet_tong([12.0])
    assert len(bang_mot) == 2, len(bang_mot)
    assert bang_mot[-1][3] == 12.0
    assert bang_mot[-1][4] is False
    assert trung_binh_cong([12.0]) == 12.0
    # Hai đầu miền số đo đều hợp lệ.
    assert so_do_hop_le(0.0)
    assert so_do_hop_le(500.0)
    assert not so_do_hop_le(500.1)
    # Dãy rỗng: bảng vết chỉ có dòng trước vòng lặp, và cột điều
    # kiện dừng đã sai ngay từ dòng đó nên thân vòng lặp không
    # chạy lượt nào.
    bang_rong = bang_vet_tong([])
    assert len(bang_rong) == 1, len(bang_rong)
    assert bang_rong[0][3] == 0.0
    assert bang_rong[0][4] is False

    # --- Trường hợp ngoại lệ -----------------------------------
    # Bước chia tổng cho số phần tử không thực hiện được trên
    # dãy rỗng; đây là lỗi dạng L1.1-2 của Mục 1.1.1.
    da_chan = False
    try:
        trung_binh_cong([])
    except ZeroDivisionError:
        da_chan = True
    assert da_chan, "day rong ma van chia duoc"

    print("BT 1.5")
    in_bang_vet("day bon so do", day_bon)
    print(f"    trung binh: {trung_binh_cong(day_bon):.1f} ug/m3")
    in_bang_vet("day rong", [])
    print("    trung binh: buoc chia khong thuc hien duoc")
