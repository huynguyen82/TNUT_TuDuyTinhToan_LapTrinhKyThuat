# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.3
Chương, mục : Chương 6, Mục 6.1.1
Đề bài      : Chương trình chia đôi 18 dòng chứa ba lỗi, mỗi lỗi
              một loại. Tìm cả ba, ghi loại và thông báo nguyên văn,
              sửa cả ba, rồi kiểm lại.
Đầu vào     : không có
Đầu ra      : ba lỗi đã phân loại, và nghiệm của bản đã sửa
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

SAI_SO = 1e-10


# Bản sai của đề bài, đã sửa riêng lỗi cú pháp để chạy được, còn
# hai lỗi kia giữ nguyên. Giữ bản này để đo được biểu hiện thật
# của từng lỗi chứ không tả bằng lời.
def f(x):
    """Ham can tim nghiem."""
    return x ** 3 - 2.0 * x - 5.0


def chia_doi_con_hai_loi(a, b):
    """Ban con loi logic o dong 13 va loi thuc thi o dong 18."""
    so_luot = 0
    while b - a > SAI_SO:
        giua = (a + b) / 2.0
        if f(a) * f(giua) > 0.0:
            b = giua
        else:
            a = giua
        so_luot = so_luot + 1
    return (a + b) / so_luot


def chia_doi(a, b):
    """Ban da sua du ba loi. Nghiem tren doan [a, b]."""
    so_luot = 0
    while b - a > SAI_SO:
        giua = (a + b) / 2.0
        if f(a) * f(giua) < 0.0:
            b = giua
        else:
            a = giua
        so_luot = so_luot + 1
    return (a + b) / 2.0


BA_LOI = (
    (3, "cu phap",
     "def f(x) thieu dau hai cham",
     "SyntaxError: expected ':'",
     "them dau hai cham cuoi dong 3"),
    (13, "logic",
     "f(a) * f(giua) > 0.0 thay vi < 0.0",
     "khong bao gi; chon nua doan khong chua nghiem",
     "doi dau so sanh thanh <"),
    (18, "thuc thi",
     "(a + b) / so_luot thay vi / 2.0",
     "ZeroDivisionError khi vong lap chay 0 luot",
     "chia cho 2.0, khong chia cho so luot"),
)


def in_bang():
    """In bang ba loi da phan loai."""
    print("Dong | Loai     | Thong bao hoac bieu hien")
    for dong, loai, _sai, bieu_hien, _sua in BA_LOI:
        print(f"{dong:>4} | {loai:<8} | {bieu_hien}")
    print()
    print(f"Ban da sua, doan [2, 3]: {chia_doi(2.0, 3.0):.6f}")
    print(f"Ban con hai loi         : "
          f"{chia_doi_con_hai_loi(2.0, 3.0):.6f}")


if __name__ == "__main__":
    in_bang()

    # Bản đã sửa cho đúng nghiệm của bài toán A6.
    assert abs(chia_doi(2.0, 3.0) - 2.094551) < 1e-5, \
        "ban da sua phai cho nghiem dung"

    # Lỗi logic ở dòng 13 không báo gì: bản còn lỗi vẫn chạy xong
    # và trả về một số thực, chỉ là số sai.
    _sai = chia_doi_con_hai_loi(2.0, 3.0)
    assert isinstance(_sai, float), "ban con loi van tra ve so"
    assert abs(_sai - 2.094551) > 1.0, \
        "ban con loi phai cho ket qua sai han"

    # Lỗi thực thi ở dòng 18 chỉ lộ ra khi vòng lặp chạy 0 lượt,
    # tức khi hai cận đã sát nhau hơn sai số. Đây là ca biên.
    _da_no = False
    try:
        chia_doi_con_hai_loi(2.0, 2.0)
    except ZeroDivisionError:
        _da_no = True
    assert _da_no, "dong 18 phai cho ZeroDivisionError khi 0 luot"

    # Ba lỗi thuộc ba loại khác nhau, đúng yêu cầu của đề bài.
    assert len({loai for _, loai, _, _, _ in BA_LOI}) == 3, \
        "ba loi phai thuoc ba loai khac nhau"

    print()
    print("Moi khang dinh dat.")
