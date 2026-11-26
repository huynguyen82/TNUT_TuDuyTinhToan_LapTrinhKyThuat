# -*- coding: utf-8 -*-
"""
Mã bài      : GL 1
Chương, mục : Chương 1, Bài gỡ lỗi GL1
Đề bài      : Mã giả 30 dòng tính độ lệch tải ba pha chứa đúng ba
              lỗi: một lỗi cú pháp của mã giả, một lỗi thực thi và
              một lỗi logic. Tìm ba lỗi, nêu loại, sửa, kiểm lại.
Đầu vào     : ba danh sách tải của ba pha, đơn vị kW
Đầu ra      : ba tổng, ba độ lệch, độ lệch lớn nhất, kết luận
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Chương 1 không in mã Python. Tệp này viết lại hai bản mã giả bằng
Python chỉ để **khẳng định các con số** mà lời giải viện dẫn, nên
không con số nào trong đáp án là phỏng đoán.
"""

NGUONG_PHAN_TRAM = 15.0

# Ba lỗi cài sẵn, theo đúng số dòng của mã giả in trong sách.
BA_LOI = (
    (23, "cu phap",
     "dong 21 mo khoi 'neu' nhung khong co dong 'het neu' rieng; "
     "ca hai khoi 'neu' dung chung mot dong dong o dong 25",
     "them mot dong 'het neu' sau dong 22"),
    (17, "thuc thi",
     "chia cho trung_binh ma khong kiem trung_binh khac 0",
     "them khoi 'neu tong > 0 thi' bao quanh ba dong tinh do lech"),
    (7, "logic",
     "khoi tao tong_B bang cac_tai_B[1] roi vong lap cong lai "
     "chinh gia tri do mot lan nua",
     "khoi tao tong_B bang 0, giong tong_A va tong_C"),
)


def tong_mot_pha(cac_tai):
    """Tong cong suat mot pha, dung dong 3 va dong 4 den 6."""
    tong = 0.0
    for tai in cac_tai:
        tong = tong + tai
    return tong


def tong_mot_pha_loi(cac_tai):
    """Ban loi dong 7: khoi tao bang phan tu dau roi cong lai."""
    tong = cac_tai[0]
    for tai in cac_tai:
        tong = tong + tai
    return tong


def do_lech_ba_pha(pha_a, pha_b, pha_c, co_loi_dong_7=False):
    """Tra ve (ba tong, do lech lon nhat phan tram, ket luan).

    Phat sinh ZeroDivisionError khi ba pha deu khong mang tai, dung
    nhu loi thuc thi o dong 17 cua ma gia.
    """
    # Lỗi dòng 7 chỉ nằm ở pha B. Hai pha còn lại khởi tạo bằng 0
    # và đúng, nên bảng kết quả trông cân đối và lỗi khó nhận ra.
    tong_a = tong_mot_pha(pha_a)
    tong_b = (tong_mot_pha_loi(pha_b) if co_loi_dong_7
              else tong_mot_pha(pha_b))
    tong_c = tong_mot_pha(pha_c)
    tong = tong_a + tong_b + tong_c
    trung_binh = tong / 3.0
    cac_lech = [(mot - trung_binh) / trung_binh * 100.0
                for mot in (tong_a, tong_b, tong_c)]
    lech_max = max(abs(mot) for mot in cac_lech)
    ket_luan = "dat" if lech_max <= NGUONG_PHAN_TRAM else "khong dat"
    return (tong_a, tong_b, tong_c), lech_max, ket_luan


PHA_A = (4.0, 3.5, 2.5)
PHA_B = (5.0, 2.0)
PHA_C = (6.0, 4.0, 3.0)


def in_ket_qua():
    """In bang ba loi va ket qua hai ban tren ba bo du lieu."""
    print("Dong | Loai     | Cach sua")
    for dong, loai, _sai, sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {sua}")
    print()

    tong_sai, lech_sai, ket_sai = do_lech_ba_pha(
        PHA_A, PHA_B, PHA_C, co_loi_dong_7=True)
    tong_dung, lech_dung, ket_dung = do_lech_ba_pha(
        PHA_A, PHA_B, PHA_C)
    print("Bo du lieu thuong, ba pha 4+3,5+2,5 | 5+2 | 6+4+3 kW")
    print(f"  Ban con loi : tong {tong_sai}, "
          f"lech max {lech_sai:.2f} %, ket luan {ket_sai}")
    print(f"  Ban da sua  : tong {tong_dung}, "
          f"lech max {lech_dung:.2f} %, ket luan {ket_dung}")

    _, lech_bien, ket_bien = do_lech_ba_pha(
        (11.5,), (10.0,), (8.5,))
    print(f"Bo du lieu bien, 11,5 | 10,0 | 8,5 kW")
    print(f"  Ban da sua  : lech max {lech_bien:.2f} %, "
          f"ket luan {ket_bien}")


if __name__ == "__main__":
    in_ket_qua()

    # Ba lỗi thuộc ba loại khác nhau, đúng yêu cầu đề bài.
    assert len({loai for _, loai, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    # Bản đã sửa cho đúng ba tổng và kết luận của đề bài.
    _tong, _lech, _ket = do_lech_ba_pha(PHA_A, PHA_B, PHA_C)
    assert _tong == (10.0, 7.0, 13.0), "ba tong phai la 10, 7, 13"
    assert abs(_lech - 30.0) < 1e-9, "do lech lon nhat phai 30 %"
    assert _ket == "khong dat", "ket luan phai la khong dat"

    # Bản còn lỗi dòng 7 cho 14,29 % và kết luận **đạt** — tức nó
    # kết luận ngược hẳn mà không có dấu hiệu nào báo sai.
    _t2, _l2, _k2 = do_lech_ba_pha(PHA_A, PHA_B, PHA_C,
                                   co_loi_dong_7=True)
    assert abs(_l2 - 14.29) < 0.01, "ban loi phai cho 14,29 %"
    assert _k2 == "dat", "ban loi ket luan nguoc"

    # Ca biên: độ lệch đúng bằng ngưỡng thì vẫn là đạt, vì ngưỡng
    # dùng dấu nhỏ hơn hoặc bằng.
    _, _lb, _kb = do_lech_ba_pha((11.5,), (10.0,), (8.5,))
    assert abs(_lb - 15.0) < 1e-9 and _kb == "dat", \
        "ca bien dung bang nguong phai la dat"

    # Ca không hợp lệ: ba pha không mang tải thì dòng 17 không
    # thực hiện được. Đây là lỗi thực thi đã cài sẵn.
    _da_no = False
    try:
        do_lech_ba_pha((0.0,), (0.0,), (0.0,))
    except ZeroDivisionError:
        _da_no = True
    assert _da_no, "ba pha khong tai phai cho ZeroDivisionError"

    print()
    print("Moi khang dinh dat.")
