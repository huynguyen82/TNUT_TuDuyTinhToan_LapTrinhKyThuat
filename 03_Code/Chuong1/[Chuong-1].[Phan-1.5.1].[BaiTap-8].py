# -*- coding: utf-8 -*-
"""
Mã bài      : BT 1.8
Chương, mục : Chương 1, Mục 1.5.1
Đề bài      : Cho mã giả 14 dòng tính tổng tải trên dầm và kết
              luận điều kiện bền. Kết quả mong đợi 41,0 kN và
              dầm đạt, mã giả cho 49,0 kN và dầm không đạt. Dùng
              quy trình năm bước để tìm dòng sai, sửa, kiểm lại.
Đầu vào     : dãy tải 8,0 · 12,0 · 6,0 · 15,0 kN, tải cho phép
              45 kN
Đầu ra      : số thứ tự dòng sai, nội dung sửa, hai bảng vết
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải dạng bảng nằm ở tệp .md cùng tên.
"""

DONG_SAI = 3
TAI_CHO_PHEP = 45.0


def bang_mong_doi(cac_tai):
    """Bảng giá trị mong đợi, lập từ bảng đặc tả.

    Lập bảng này **không** được nhìn mã giả, theo bước 1 của quy
    trình năm bước ở Mục 1.5.1. Ở đây bảng dựng từ định nghĩa
    của phép cộng dồn, không dựng từ mã giả cần kiểm.
    """
    cac_dong = [("truoc vong lap", 0.0)]
    tong = 0.0
    for chi_so, tai in enumerate(cac_tai, start=1):
        tong = tong + tai
        cac_dong.append((str(chi_so), tong))
    return cac_dong


def bang_ma_gia_sai(cac_tai):
    """Bảng vết của mã giả sai: dòng 3 khởi tạo tổng bằng phần
    tử đầu tiên, rồi thân vòng lặp vẫn cộng lại phần tử đó."""
    cac_dong = [("truoc vong lap", cac_tai[0])]
    tong = cac_tai[0]
    for chi_so, tai in enumerate(cac_tai, start=1):
        tong = tong + tai
        cac_dong.append((str(chi_so), tong))
    return cac_dong


def bang_ma_gia_da_sua(cac_tai):
    """Bảng vết của mã giả sau khi sửa dòng 3 thành gán tong = 0."""
    return bang_mong_doi(cac_tai)


def luot_lech_dau_tien(bang_a, bang_b):
    """Nhãn lượt đầu tiên hai bảng khác nhau, hoặc None.

    Đây là bước 3 và bước 4 của quy trình năm bước.
    """
    for (nhan_a, gia_tri_a), (_, gia_tri_b) in zip(bang_a, bang_b):
        if abs(gia_tri_a - gia_tri_b) > 1e-9:
            return nhan_a
    return None


def ket_luan_ben(tong, tai_cho_phep=TAI_CHO_PHEP):
    """Kết luận điều kiện bền của dầm."""
    return "dat" if tong <= tai_cho_phep else "khong dat"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    cac_tai = [8.0, 12.0, 6.0, 15.0]
    mong_doi = bang_mong_doi(cac_tai)
    ma_sai = bang_ma_gia_sai(cac_tai)
    assert mong_doi[-1][1] == 41.0, mong_doi[-1]
    assert ma_sai[-1][1] == 49.0, ma_sai[-1]
    assert ket_luan_ben(41.0) == "dat"
    assert ket_luan_ben(49.0) == "khong dat"
    # Bước 3 và 4: hai bảng lệch ngay ở dòng trước vòng lặp, nên
    # dòng sai là dòng khởi tạo, tức dòng 3 của mã giả.
    assert luot_lech_dau_tien(mong_doi, ma_sai) == "truoc vong lap"
    assert DONG_SAI == 3
    # Bước 5: sửa xong thì hai bảng trùng khít.
    da_sua = bang_ma_gia_da_sua(cac_tai)
    assert luot_lech_dau_tien(mong_doi, da_sua) is None
    assert da_sua[-1][1] == 41.0

    # --- Trường hợp biên ---------------------------------------
    # Dãy một tải duy nhất: mã giả sai cho 16,0 kN, mong đợi
    # 8,0 kN. Cả hai đều dưới 45 kN nên câu kết luận không đổi;
    # lỗi chỉ lộ ra ở giá trị tổng, không lộ ở kết luận.
    mot_tai = [8.0]
    assert bang_mong_doi(mot_tai)[-1][1] == 8.0
    assert bang_ma_gia_sai(mot_tai)[-1][1] == 16.0
    assert (ket_luan_ben(8.0) == ket_luan_ben(16.0) == "dat")
    assert luot_lech_dau_tien(
        bang_mong_doi(mot_tai),
        bang_ma_gia_sai(mot_tai)) == "truoc vong lap"
    # Tổng đúng bằng tải cho phép vẫn đạt.
    assert ket_luan_ben(45.0) == "dat"
    assert ket_luan_ben(45.1) == "khong dat"
    # Bộ dữ liệu nào cũng bộc lộ lỗi, vì lệch ngay ở dòng đầu.
    for bo in ([8.0], [8.0, 12.0], cac_tai):
        assert luot_lech_dau_tien(
            bang_mong_doi(bo),
            bang_ma_gia_sai(bo)) == "truoc vong lap"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Dãy rỗng: mã giả sai không thực hiện được vì không có phần
    # tử đầu tiên, trong khi bảng mong đợi vẫn lập được.
    assert bang_mong_doi([]) == [("truoc vong lap", 0.0)]
    da_chan = False
    try:
        bang_ma_gia_sai([])
    except IndexError:
        da_chan = True
    assert da_chan, "ma gia sai van chay duoc tren day rong"

    print("BT 1.8")
    print(f"  Dong sai: dong {DONG_SAI}, khoi tao tong bang "
          f"phan tu dau tien")
    print(f"  {'luot':<16}{'mong doi':>10}{'ma gia sai':>12}"
          f"{'da sua':>9}")
    for (nhan, md), (_, ms), (_, ds) in zip(
            mong_doi, ma_sai, da_sua):
        print(f"  {nhan:<16}{md:>10.1f}{ms:>12.1f}{ds:>9.1f}")
