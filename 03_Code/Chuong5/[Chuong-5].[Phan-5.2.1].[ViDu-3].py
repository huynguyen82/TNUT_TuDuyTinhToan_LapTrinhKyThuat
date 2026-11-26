# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 3
Chương, mục : Chương 5, Mục 5.2.1
Đề bài      : Bảng tra mức chất lượng không khí bằng từ điển,
              so với cách duyệt danh sách.
Đầu vào     : nồng độ cố định trong mã
Đầu ra      : cận dưới của vài mức, và mức của vài nồng độ
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# Bang muc chat luong khong khi theo nong do PM2.5, microgram
# tren met khoi. So lieu gia dinh cua de bai.

# --- in-sach ---
can_duoi = {
    "tot": 0.0,
    "trung binh": 12.1,
    "kem": 35.5,
    "xau": 55.5,
    "rat xau": 150.5,
    "nguy hai": 250.5,
}

print(f"so muc        : {len(can_duoi)}")
print(f"can duoi 'xau': {can_duoi['xau']}")
print(f"co muc 'kem'  : {'kem' in can_duoi}")
print(f"muc khong co  : {can_duoi.get('cuc xau', -1.0)}")
for ten in can_duoi:
    print(f"  {ten:<12}{can_duoi[ten]:>7.1f}")
# --- het-in-sach ---


def tra_bang_duyet(bang, ten):
    """Tra cận dưới bằng duyệt danh sách, O(n)."""
    for thu_tu in range(len(bang)):
        if bang[thu_tu][0] == ten:
            return bang[thu_tu][1]
    return -1.0


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert len(can_duoi) == 6
    assert can_duoi["xau"] == 55.5
    assert can_duoi["tot"] == 0.0
    assert ("kem" in can_duoi) is True

    # --- Trường hợp biên ---------------------------------------
    # Hai cach tra cho cung ket qua tren moi muc.
    bang = list(can_duoi.items())
    for ten in can_duoi:
        assert tra_bang_duyet(bang, ten) == can_duoi[ten]
    # Khoa khong co: get voi gia tri mac dinh noi duoc dieu do.
    assert can_duoi.get("cuc xau", -1.0) == -1.0
    assert tra_bang_duyet(bang, "cuc xau") == -1.0
    # get KHONG truyen gia tri mac dinh thi tra None, khong bao gi.
    assert can_duoi.get("cuc xau") is None
    # Thu tu khai bao duoc giu, nen duyet cho dung thu tu bang.
    assert list(can_duoi)[0] == "tot"
    assert list(can_duoi)[-1] == "nguy hai"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tra khoa khong co bang dau ngoac vuong thi bao loi.
    da_chan = False
    try:
        can_duoi["cuc xau"]
    except KeyError:
        da_chan = True
    assert da_chan, "tra khoa khong co ma van chay"
    # Khoa so thuc la loi im lang: sai so cua Muc 2.4.2.
    sai = {0.1 + 0.2: "a"}
    assert (0.3 in sai) is False
    assert list(sai)[0] == 0.30000000000000004
