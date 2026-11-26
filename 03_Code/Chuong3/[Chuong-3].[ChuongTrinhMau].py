# -*- coding: utf-8 -*-
"""
Mã bài      : Chương trình mẫu Chương 3, bản đầy đủ
Chương, mục : Chương 3, mục Chương trình mẫu
Đề bài      : Theo dõi nhiệt độ một ca trực. Đọc các số đo liên
              tiếp tới khi gặp giá trị kết thúc; bỏ qua số đo lỗi
              và đếm riêng; phân bốn trạng thái theo ba ngưỡng;
              dừng ngay khi gặp số đo tới ngưỡng dừng máy; in phiếu
              ca trực có định dạng.
Đầu vào     : dãy số đo nhiệt độ gõ từ bàn phím, đơn vị độ C,
              kết thúc bằng -1; số đo âm khác -1 là lỗi cảm biến
Đầu ra      : phiếu ca trực gồm bốn số đếm trạng thái, số đo lỗi,
              nhiệt độ trung bình và kết luận ca
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Chương 3 chưa có danh sách và chưa có hàm, nên chương trình dùng
bốn biến đếm riêng thay cho một danh sách, và viết thành một khối
liền thay vì tách hàm. Chương 4 tách nó thành bộ hàm; Chương 5
thay bốn biến đếm bằng một cấu trúc dữ liệu.
"""

NGUONG_CANH_BAO = 60.0
NGUONG_NGUY_HIEM = 80.0
NGUONG_DUNG_MAY = 100.0
KET_THUC = -1.0
LOI_NHAC = "So do (do C), -1 de ket thuc: "

# --- in-sach ---
binh_thuong = 0
canh_bao = 0
nguy_hiem = 0
dung_may = 0
so_loi = 0
tong = 0.0

so_do = float(input(LOI_NHAC))
while so_do != KET_THUC:
    if so_do < 0.0:
        so_loi = so_loi + 1
        so_do = float(input(LOI_NHAC))
        continue
    tong = tong + so_do
    if so_do < NGUONG_CANH_BAO:
        binh_thuong = binh_thuong + 1
    elif so_do < NGUONG_NGUY_HIEM:
        canh_bao = canh_bao + 1
    elif so_do < NGUONG_DUNG_MAY:
        nguy_hiem = nguy_hiem + 1
    else:
        dung_may = dung_may + 1
        break
    so_do = float(input(LOI_NHAC))
# --- het-in-sach ---

so_hop_le = binh_thuong + canh_bao + nguy_hiem + dung_may

print()
print(f"{'PHIEU CA TRUC':<22}")
print(f"{'Binh thuong':<22}{binh_thuong:>6}")
print(f"{'Canh bao':<22}{canh_bao:>6}")
print(f"{'Nguy hiem':<22}{nguy_hiem:>6}")
print(f"{'Dung may':<22}{dung_may:>6}")
print(f"{'So do loi':<22}{so_loi:>6}")
if so_hop_le > 0:
    print(f"{'Trung binh (do C)':<22}{tong / so_hop_le:>6.1f}")
else:
    print(f"{'Trung binh (do C)':<22}{'khong co':>6}")
if dung_may > 0:
    print(f"{'Ket luan':<22}{'DUNG MAY':>6}")
else:
    print(f"{'Ket luan':<22}{'tiep tuc':>6}")


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    # Tệp .in cho 45,0 · 72,5 · -5,0 · 85,0 · 120,0 rồi -1.
    assert binh_thuong == 1, binh_thuong
    assert canh_bao == 1, canh_bao
    assert nguy_hiem == 1, nguy_hiem
    assert dung_may == 1, dung_may
    assert so_loi == 1, so_loi

    # --- Trường hợp biên ---------------------------------------
    # Số đo 120,0 tới ngưỡng dừng máy nên vòng lặp thoát bằng
    # break. Giá trị -1 phía sau **không** được đọc tới.
    assert so_do == 120.0, so_do

    # Số đo gây dừng máy **vẫn** là một số đo hợp lệ: nó vào tổng
    # và vào mẫu số. Đếm nó vào tổng mà bỏ khỏi mẫu số thì trung
    # bình ra 107,5 thay vì 80,6 — đúng lỗi L5.1-6 ở dạng sớm.
    assert tong == 322.5, tong
    assert so_hop_le == 4, so_hop_le
    assert abs(tong / so_hop_le - 80.625) < 1e-9

    # --- Trường hợp dữ liệu không hợp lệ -----------------------
    # Số đo -5,0 là lỗi cảm biến: nó bị continue bỏ qua nên không
    # vào tổng, nhưng vẫn được đếm riêng. Dùng break ở đó là lỗi
    # L3.2-9: ba số đo sau sẽ mất.
    assert so_loi == 1 and so_hop_le == 4

    print()
    print("Moi khang dinh dat.")
