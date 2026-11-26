# -*- coding: utf-8 -*-
"""
Mã bài      : Bài tập 6.1
Chương, mục : Chương 6, Mục 6.1.1
Đề bài      : Xếp sáu thông báo lỗi lấy từ năm chương trước vào ba
              loại, và cho biết thông báo có nói được dòng mã sai
              hay không.
Đầu vào     : sáu thông báo lỗi của đề bài
Đầu ra      : bảng ba cột, và hai số đếm theo loại
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# Mỗi dòng: (số thứ tự, thông báo, loại, có nói dòng mã sai).
SAU_THONG_BAO = (
    (1, "SyntaxError: expected ':'", "cu phap", True),
    (2, "IndexError: list index out of range", "thuc thi", True),
    (3, "Chay xong, in 75.0 kWh thay vi 60.0 kWh", "logic", False),
    (4, "ValueError: could not convert string to float",
     "thuc thi", True),
    (5, "Khong bao loi; chuoi toan so am cho ket qua 0",
     "logic", False),
    (6, "UnboundLocalError: cannot access local variable",
     "thuc thi", True),
)

# Mã lỗi gốc của năm chương trước, để đối chiếu ngược.
NGUON = {1: "L3.1-1", 2: "L5.1-1", 3: "L2.1-3",
         4: "L2.3-2", 5: "L5.1-5", 6: "L4.1-5"}


def dem_theo_loai():
    """Tra ve tu dien so dem theo ba loai."""
    so_dem = {"cu phap": 0, "thuc thi": 0, "logic": 0}
    for _, _, loai, _ in SAU_THONG_BAO:
        so_dem[loai] += 1
    return so_dem


def in_bang():
    """In bang sau thong bao da phan loai."""
    print("STT | Loai     | Noi duoc dong sai | Ma loi goc")
    for so, _tb, loai, noi_duoc in SAU_THONG_BAO:
        co = "co   " if noi_duoc else "khong"
        print(f"{so:>3} | {loai:<8} | {co:<17} | {NGUON[so]}")
    print()
    so_dem = dem_theo_loai()
    for loai in ("cu phap", "thuc thi", "logic"):
        print(f"So thong bao loai {loai:<8}: {so_dem[loai]}")


if __name__ == "__main__":
    in_bang()

    _dem = dem_theo_loai()
    # Sáu thông báo phủ cả ba loại, không loại nào vắng.
    assert all(_dem[loai] > 0 for loai in _dem), \
        "ca ba loai deu phai co mat"

    # Hai câu hỏi của đề bài trùng nhau: đúng các thông báo loại
    # logic là các thông báo không nói được dòng sai.
    for _so, _tb, _loai, _noi in SAU_THONG_BAO:
        assert (_loai == "logic") == (not _noi), \
            f"thong bao {_so} khong khop hai cau hoi"

    # Thông báo 6 nhắc tới một khai báo nên dễ nhầm thành lỗi cú
    # pháp, nhưng nó xảy ra lúc chạy nên là lỗi thực thi.
    assert SAU_THONG_BAO[5][2] == "thuc thi", \
        "UnboundLocalError la loi thuc thi"

    print()
    print("Moi khang dinh dat.")
