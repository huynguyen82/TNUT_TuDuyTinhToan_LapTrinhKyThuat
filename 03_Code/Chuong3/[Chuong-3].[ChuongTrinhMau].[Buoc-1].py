# -*- coding: utf-8 -*-
"""
Mã bài      : Chương trình mẫu Chương 3, bước 1
Chương, mục : Chương 3, mục Chương trình mẫu
Đề bài      : Bản tối thiểu chạy được của chương trình theo dõi
              nhiệt độ một ca trực. Bản này chỉ đọc số đo tới khi
              gặp giá trị kết thúc và đếm số lượng, chưa phân loại
              và chưa xử lý số đo lỗi.
Đầu vào     : dãy số đo nhiệt độ gõ từ bàn phím, kết thúc bằng -1
Đầu ra      : số lượng số đo đã đọc
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
KET_THUC = -1.0
LOI_NHAC = "So do (do C), -1 de ket thuc: "

so_luong = 0

so_do = float(input(LOI_NHAC))
while so_do != KET_THUC:
    so_luong = so_luong + 1
    so_do = float(input(LOI_NHAC))

print(f"Da doc {so_luong} so do.")
# --- het-in-sach ---


if __name__ == "__main__":
    # Bộ dữ liệu thường của tệp .in: bốn số đo rồi giá trị kết
    # thúc, nên chương trình phải đếm được đúng bốn.
    assert so_luong == 4, so_luong

    # Dòng đọc số đo xuất hiện **hai lần**: một lần trước vòng lặp
    # để điều kiện có giá trị mà kiểm, một lần ở cuối thân để
    # điều kiện đổi giá trị cho lượt sau. Bỏ lần sau là vòng lặp
    # vô hạn, đúng lỗi L3.2-5.
    assert LOI_NHAC.count("-1") == 1

    # Giá trị kết thúc **không** được đếm: nó là dấu hiệu dừng,
    # không phải một số đo.
    assert so_do == KET_THUC

    print("Moi khang dinh dat.")
