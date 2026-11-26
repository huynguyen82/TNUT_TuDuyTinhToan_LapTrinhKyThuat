# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.2
Chương, mục : Chương 2, Mục 2.2.1
Đề bài      : Cho ba đoạn mã, mỗi đoạn một lỗi. Nêu loại lỗi,
              chép thông báo lỗi nguyên văn, và sửa.
Đầu vào     : ba đoạn mã, viết thẳng trong mã dưới dạng chuỗi
Đầu ra      : loại lỗi, thông báo nguyên văn và bản sửa của từng
              đoạn
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Tệp này chạy từng đoạn mã
sai để lấy thông báo lỗi nguyên văn, nên đáp án không chép tay.
"""

# Ba đoạn mã sai của đề bài, kèm bản đã sửa.
CAC_DOAN = {
    "a": {
        "sai": 'ten_ca = ngay',
        "sua": 'ten_ca = "ngay"',
        "loai": "loi thuc thi",
    },
    "b": {
        "sai": 'kich_thuoc = int("50.03")',
        "sua": 'kich_thuoc = float("50.03")',
        "loai": "loi thuc thi",
    },
    "c": {
        "sai": '50 = kich_thuoc',
        "sua": 'kich_thuoc = 50',
        "loai": "loi cu phap",
    },
}


def chay_doan(ma_nguon):
    """Chạy một đoạn mã, trả về (ten_loi, thong_bao).

    Trả về (None, None) khi đoạn mã chạy được.
    """
    try:
        exec(compile(ma_nguon, "<de bai>", "exec"), {})
    except Exception as loi:
        return type(loi).__name__, str(loi)
    return None, None


def loai_loi_theo_muc_1_5_1(ten_loi):
    """Phân loại một lỗi theo ba loại của Mục 1.5.1."""
    if ten_loi is None:
        return "khong co loi"
    if ten_loi == "SyntaxError":
        return "loi cu phap"
    return "loi thuc thi"


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    ten_loi, thong_bao = chay_doan(CAC_DOAN["a"]["sai"])
    assert ten_loi == "NameError", ten_loi
    assert thong_bao == "name 'ngay' is not defined", thong_bao
    assert loai_loi_theo_muc_1_5_1(ten_loi) == "loi thuc thi"
    assert chay_doan(CAC_DOAN["a"]["sua"]) == (None, None)

    # --- Trường hợp biên ---------------------------------------
    # Ép chuỗi có phần thập phân sang số nguyên: cùng là lỗi thực
    # thi nhưng tên lỗi khác, nên phải phân biệt tên lỗi với loại.
    ten_loi_b, thong_bao_b = chay_doan(CAC_DOAN["b"]["sai"])
    assert ten_loi_b == "ValueError", ten_loi_b
    assert "invalid literal for int()" in thong_bao_b
    assert loai_loi_theo_muc_1_5_1(ten_loi_b) == "loi thuc thi"
    assert chay_doan(CAC_DOAN["b"]["sua"]) == (None, None)
    # Hai đoạn đầu cùng loại nhưng khác tên lỗi.
    assert ten_loi != ten_loi_b
    assert (loai_loi_theo_muc_1_5_1(ten_loi)
            == loai_loi_theo_muc_1_5_1(ten_loi_b))

    # --- Trường hợp ngoại lệ -----------------------------------
    # Lỗi cú pháp khác hai lỗi trên ở chỗ không dòng nào chạy.
    ten_loi_c, thong_bao_c = chay_doan(CAC_DOAN["c"]["sai"])
    assert ten_loi_c == "SyntaxError", ten_loi_c
    assert "cannot assign to literal" in thong_bao_c
    assert loai_loi_theo_muc_1_5_1(ten_loi_c) == "loi cu phap"
    assert chay_doan(CAC_DOAN["c"]["sua"]) == (None, None)

    print("BT 2.2")
    for ma, doan in CAC_DOAN.items():
        ten, thong_bao = chay_doan(doan["sai"])
        print(f"  Doan {ma}: {doan['sai']}")
        print(f"    loai     : {loai_loi_theo_muc_1_5_1(ten)}")
        print(f"    thong bao: {ten}: {thong_bao}")
        print(f"    sua thanh: {doan['sua']}")
