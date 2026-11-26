# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.6
Chương, mục : Chương 1, Mục 1.4.1
Đề bài      : Chuyển lưu đồ kết luận cân pha của bài toán tủ
              phân phối thành mã giả, rồi kiểm hai biểu diễn
              tương đương nhau bằng cách lập bảng vết cho cả hai
              và so theo từng dòng.
Đầu vào     : ba công suất pha (kW)
Đầu ra      : độ lệch lớn nhất (%) và câu kết luận
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Mã giả lời giải nằm ở tệp .md cùng tên. Tệp này cài đặt cả hai
biểu diễn rồi khẳng định hai bảng vết trùng nhau theo từng dòng.
"""

NGUONG_LECH = 15.0
TEN_PHA = ("A", "B", "C")


def do_lech(cong_suat_pha, trung_binh):
    """Độ lệch của một pha so với trung bình, %."""
    return (cong_suat_pha - trung_binh) / trung_binh * 100.0


def chay_luu_do(ba_cong_suat):
    """Thực hiện lưu đồ: tính tuần tự ba độ lệch rồi so ngưỡng.

    Trả về (lech_max, ket_luan). Phát sinh ZeroDivisionError khi
    cả ba pha không mang tải.
    """
    trung_binh = sum(ba_cong_suat) / len(ba_cong_suat)
    cac_lech = [
        do_lech(cong_suat, trung_binh)
        for cong_suat in ba_cong_suat
    ]
    lech_max = max(abs(lech) for lech in cac_lech)
    dat = lech_max <= NGUONG_LECH
    return lech_max, "dat" if dat else "khong dat"


def bang_vet_ma_gia(ba_cong_suat):
    """Bảng vết của mã giả, vòng lặp ba lượt trên ba pha.

    Trả về danh sách dòng (nhan_luot, i, ten_pha, lech, lech_max,
    con_lap). Dòng đầu là dòng trước vòng lặp.
    """
    trung_binh = sum(ba_cong_suat) / len(ba_cong_suat)
    so_pha = len(ba_cong_suat)
    cac_dong = [("truoc vong lap", 0, "-", None, 0.0, True)]
    lech_max = 0.0
    for chi_so, cong_suat in enumerate(ba_cong_suat, start=1):
        lech = do_lech(cong_suat, trung_binh)
        lech_max = max(lech_max, abs(lech))
        cac_dong.append(
            (str(chi_so), chi_so, TEN_PHA[chi_so - 1], lech,
             lech_max, chi_so < so_pha)
        )
    return cac_dong


def chay_ma_gia(ba_cong_suat):
    """Thực hiện mã giả, trả về (lech_max, ket_luan)."""
    cac_dong = bang_vet_ma_gia(ba_cong_suat)
    lech_max = cac_dong[-1][4]
    dat = lech_max <= NGUONG_LECH
    return lech_max, "dat" if dat else "khong dat"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    ba_pha = [10.0, 7.0, 13.0]
    lech_lu, ket_lu = chay_luu_do(ba_pha)
    lech_ma, ket_ma = chay_ma_gia(ba_pha)
    assert abs(lech_lu - 30.0) < 1e-9, lech_lu
    assert ket_lu == "khong dat"
    # Hai biểu diễn phải cho cùng một kết quả, đây là phép kiểm
    # tương đương mà đề bài yêu cầu.
    assert abs(lech_lu - lech_ma) < 1e-9
    assert ket_lu == ket_ma
    bang = bang_vet_ma_gia(ba_pha)
    assert len(bang) == 4, len(bang)
    assert abs(bang[1][3] - 0.0) < 1e-9
    assert abs(bang[2][3] + 30.0) < 1e-9
    assert abs(bang[3][3] - 30.0) < 1e-9
    assert bang[-1][5] is False

    # --- Trường hợp biên ---------------------------------------
    # Độ lệch đúng bằng ngưỡng 15 % vẫn được coi là đạt, vì điều
    # kiện dùng dấu nhỏ hơn hoặc bằng.
    ba_pha_bien = [11.5, 10.0, 8.5]
    lech_bien, ket_bien = chay_ma_gia(ba_pha_bien)
    assert abs(lech_bien - 15.0) < 1e-9, lech_bien
    assert ket_bien == "dat"
    assert chay_luu_do(ba_pha_bien) == chay_ma_gia(ba_pha_bien)
    # Lệch hơn ngưỡng một chút thì không đạt.
    assert chay_ma_gia([11.6, 10.0, 8.4])[1] == "khong dat"
    # Ba pha cân hoàn toàn cho độ lệch bằng 0.
    assert chay_ma_gia([10.0, 10.0, 10.0])[0] == 0.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # Cả ba pha không mang tải: bước chia cho công suất trung
    # bình không thực hiện được, đúng lỗi L1.2-2 của Mục 1.2.1.
    for ham in (chay_luu_do, chay_ma_gia):
        da_chan = False
        try:
            ham([0.0, 0.0, 0.0])
        except ZeroDivisionError:
            da_chan = True
        assert da_chan, f"{ham.__name__}: ba pha rong ma van chia"

    print("BT 1.6")
    print(f"  Luu do : lech_max {lech_lu:.0f} %, {ket_lu}")
    print(f"  Ma gia : lech_max {lech_ma:.0f} %, {ket_ma}")
    print(f"  {'luot':<16}{'pha':>4}{'lech':>9}{'lech_max':>10}")
    for nhan, _, pha, lech, lech_max, _ in bang:
        chu = "-" if lech is None else f"{lech:+.0f}"
        print(f"  {nhan:<16}{pha:>4}{chu:>9}{lech_max:>10.0f}")
