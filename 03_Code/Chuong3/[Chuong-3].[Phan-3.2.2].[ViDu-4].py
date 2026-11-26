# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 4
Chương, mục : Chương 3, Mục 3.2.2
Đề bài      : Đọc liên tiếp các số đo nhiệt độ cho tới khi gặp
              giá trị kết thúc, không biết trước bao nhiêu số.
              Đếm số đo và tìm giá trị lớn nhất.
Đầu vào     : dãy số đo (°C), kết thúc bằng giá trị -1
Đầu ra      : số lượng số đo và giá trị lớn nhất
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

# --- in-sach ---
GIA_TRI_KET_THUC = -1.0

so_luong = 0
lon_nhat = 0.0
so_do = float(input("So do (-1 de ket thuc): "))

while so_do != GIA_TRI_KET_THUC:
    so_luong = so_luong + 1
    if so_do > lon_nhat:
        lon_nhat = so_do
    so_do = float(input("So do (-1 de ket thuc): "))

print(f"Da doc {so_luong} so do")
print(f"Lon nhat: {lon_nhat:.1f} do C")
# --- het-in-sach ---


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert so_luong == 3, so_luong
    assert lon_nhat == 90.0, lon_nhat
    # Dòng đọc số đo xuất hiện hai lần: một lần trước vòng lặp
    # và một lần ở cuối thân. Thiếu dòng thứ hai là lặp vô hạn.
    assert so_do == GIA_TRI_KET_THUC

    # --- Trường hợp biên ---------------------------------------
    # Dãy rỗng, tức giá trị kết thúc ngay từ số đầu tiên: vòng
    # lặp chạy 0 lượt và hai biến giữ giá trị khởi tạo.
    dem_rong = 0
    gia_tri = GIA_TRI_KET_THUC
    while gia_tri != GIA_TRI_KET_THUC:
        dem_rong = dem_rong + 1
    assert dem_rong == 0
    # Đúng một số đo trước giá trị kết thúc.
    cac_so = (45.0, GIA_TRI_KET_THUC)
    dem_mot = 0
    chi_so = 0
    while cac_so[chi_so] != GIA_TRI_KET_THUC:
        dem_mot = dem_mot + 1
        chi_so = chi_so + 1
    assert dem_mot == 1
    # Giá trị khởi tạo của lớn nhất là 0,0 nên dãy toàn số âm sẽ
    # cho kết quả sai; đây là giới hạn đã biết, xem Khối 8.
    assert lon_nhat >= 0.0

    # --- Trường hợp ngoại lệ -----------------------------------
    # So sánh số thực bằng dấu bằng làm điều kiện dừng chỉ an
    # toàn khi giá trị kết thúc nhập đúng nguyên văn. Một số
    # phép tính cho đúng giá trị, nhưng phép cộng dồn thì không,
    # theo Mục 2.4.2. Đây là lý do giá trị kết thúc phải được
    # nhập vào chứ không được tính ra.
    assert (-0.5 - 0.5) == GIA_TRI_KET_THUC
    assert (-0.1 * 10) == GIA_TRI_KET_THUC
    tong_cong_don = 0.0
    for _ in range(10):
        tong_cong_don = tong_cong_don - 0.1
    assert tong_cong_don != GIA_TRI_KET_THUC
    assert abs(tong_cong_don - GIA_TRI_KET_THUC) < 1e-15
