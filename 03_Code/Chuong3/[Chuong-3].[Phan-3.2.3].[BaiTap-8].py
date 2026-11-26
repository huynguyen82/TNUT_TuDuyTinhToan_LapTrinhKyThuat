# -*- coding: utf-8 -*-
"""
Mã bài      : BT 3.8
Chương, mục : Chương 3, Mục 3.2.2 và 3.2.3
Đề bài      : Chọn giữa for, while và for có break cho bốn tình
              huống; nêu độ phức tạp tiệm cận và lý giải.
Đầu vào     : bốn mô tả tình huống kèm quy mô dữ liệu
Đầu ra      : bốn lựa chọn và bốn ký hiệu độ phức tạp
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên.
"""

DUNG_FOR = "for"
DUNG_WHILE = "while"
DUNG_BREAK = "for co break"


def chon_cau_truc(biet_truoc_so_luot, dung_som_duoc):
    """Chọn cấu trúc lặp theo hai câu hỏi của gợi ý đề bài."""
    if not biet_truoc_so_luot:
        return DUNG_WHILE
    if dung_som_duoc:
        return DUNG_BREAK
    return DUNG_FOR


def do_phuc_tap(cau_truc):
    """Độ phức tạp tiệm cận của mỗi lựa chọn."""
    if cau_truc == DUNG_BREAK:
        return "O(n) xau nhat, O(1) tot nhat"
    return "O(n)"


# Bốn tình huống của đề bài: (tên, biết trước số lượt, dừng
# sớm được).
CAC_TINH_HUONG = (
    ("tong 12 so do", True, False),
    ("doc den gia tri ket thuc", False, False),
    ("tim dong dau bang 500 dong", True, True),
    ("kiem moi so do trong mien", True, True),
)


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert chon_cau_truc(True, False) == DUNG_FOR
    assert do_phuc_tap(DUNG_FOR) == "O(n)"
    assert chon_cau_truc(False, False) == DUNG_WHILE

    # --- Trường hợp biên ---------------------------------------
    # Tim dong dau: dung som duoc nen chon break.
    assert chon_cau_truc(True, True) == DUNG_BREAK
    assert "O(1) tot nhat" in do_phuc_tap(DUNG_BREAK)
    # Kiem moi so do trong mien: dung som duoc ngay khi gap so
    # do dau tien ngoai mien, nen cung chon break.
    assert chon_cau_truc(True, True) == DUNG_BREAK
    # Khong biet truoc so luot thi cau hoi thu hai khong con
    # y nghia: van chon while.
    assert (chon_cau_truc(False, True)
            == chon_cau_truc(False, False) == DUNG_WHILE)
    # Bon tinh huong cho dung ba cau truc khac nhau.
    cac_lua_chon = {
        chon_cau_truc(biet, som)
        for _, biet, som in CAC_TINH_HUONG
    }
    assert len(cac_lua_chon) == 3, cac_lua_chon

    # --- Trường hợp ngoại lệ -----------------------------------
    # Moi lua chon deu co do phuc tap xau nhat la O(n); break
    # khong cai thien truong hop xau nhat.
    for cau_truc in (DUNG_FOR, DUNG_WHILE, DUNG_BREAK):
        assert do_phuc_tap(cau_truc).startswith("O(n)")

    print("BT 3.8")
    for ten, biet, som in CAC_TINH_HUONG:
        cau_truc = chon_cau_truc(biet, som)
        print(f"  {ten:<28}{cau_truc:<14}"
              f"{do_phuc_tap(cau_truc)}")
