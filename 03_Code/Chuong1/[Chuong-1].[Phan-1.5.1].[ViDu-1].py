# -*- coding: utf-8 -*-
"""
Mã bài      : ViDu 1, công cụ kiểm chứng của Chương 1
Chương, mục : Chương 1, dùng cho mọi mục từ 1.1 đến 1.5
Đề bài      : Cài đặt năm bài toán A, B, C, D, E của Chương 1 rồi
              khẳng định mọi đáp số sẽ in trong sách. Chương 1 không
              in mã Python; tệp này là công cụ của người soạn, bảo
              đảm mọi con số trong chương do máy tính ra.
Đầu vào     : số liệu của năm bài toán, viết thẳng trong mã
Đầu ra      : bảng đáp số in ra màn hình và các khẳng định assert
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm
"""

NGUONG_LECH_PHA = 15.0
NGUONG_PM25 = 50.0
TAI_CHO_PHEP_KN = 50.0

# Bài toán A. Phân xưởng 12 động cơ, bộ rút gọn 5 động cơ.
# Mỗi phần tử: (ma_dong_co, cong_suat_kw, gio_chay)
DONG_CO_5 = [
    (1, 7.5, 8.0),
    (2, 15.0, 6.0),
    (3, 3.0, 12.0),
    (4, 22.0, 4.0),
    (5, 11.0, 10.0),
]

# Bài toán B. Ba pha của một tủ phân phối, công suất tải (kW).
TAI_BA_PHA = {
    "A": [4.0, 3.5, 2.5],
    "B": [5.0, 2.0],
    "C": [6.0, 4.0, 3.0],
}

# Bài toán C. Dãy tải tập trung trên dầm (kN).
TAI_DAM_KN = [8.0, 12.0, 6.0, 15.0]

# Bài toán D. Điểm hoà vốn. Số liệu giả định của đề bài.
CHI_PHI_CO_DINH = 240000.0   # nghìn đồng
CHI_PHI_BIEN_DOI = 35.0      # nghìn đồng trên một sản phẩm
GIA_BAN = 95.0               # nghìn đồng trên một sản phẩm

# Bài toán E. Nồng độ PM2.5 theo giờ (µg/m³).
PM25_6_GIO = [42.0, 55.0, 61.0, 48.0, 50.0, 73.0]

# Khấu hao đường thẳng. Số liệu giả định của đề bài.
NGUYEN_GIA = 600000.0        # nghìn đồng
SO_NAM_SU_DUNG = 5


def dien_nang_tung_dong_co(danh_sach):
    """Trả về danh sách (ma_dong_co, dien_nang_kwh)."""
    return [
        (ma, cong_suat * gio) for ma, cong_suat, gio in danh_sach
    ]


def giai_bai_toan_a(danh_sach):
    """Bài toán A: tổng điện năng và động cơ tiêu thụ nhiều nhất.

    Trả về (tong_kwh, ma_lon_nhat, dien_nang_lon_nhat). Khi danh
    sách rỗng, trả về (0.0, None, None) theo đặc tả Mục 1.1.1.
    Khi hai động cơ bằng nhau, lấy mã nhỏ hơn.
    """
    cac_dien_nang = dien_nang_tung_dong_co(danh_sach)
    if not cac_dien_nang:
        return 0.0, None, None
    tong = 0.0
    ma_lon_nhat = None
    lon_nhat = None
    for ma, dien_nang in cac_dien_nang:
        tong = tong + dien_nang
        if lon_nhat is None or dien_nang > lon_nhat:
            lon_nhat = dien_nang
            ma_lon_nhat = ma
    return tong, ma_lon_nhat, lon_nhat


def giai_bai_toan_a_sai_khoi_tao(danh_sach):
    """Mã giả sai L1.3-3: gán tong bằng phần tử đầu rồi vẫn cộng
    lại phần tử đó. Dùng cho Khối 7 của Mục 1.3.1 và cho tình
    huống của Mục 1.5.1."""
    cac_dien_nang = dien_nang_tung_dong_co(danh_sach)
    tong = cac_dien_nang[0][1]
    for _, dien_nang in cac_dien_nang:
        tong = tong + dien_nang
    return tong


def giai_bai_toan_a_lech_mot(danh_sach):
    """Mã giả sai L1.4-3: lặp từ 1 đến n-1, bỏ phần tử cuối.

    Trả về (tong_kwh, ma_lon_nhat) tính trên n-1 phần tử đầu.
    """
    cac_dien_nang = dien_nang_tung_dong_co(danh_sach)[:-1]
    tong = sum(dien_nang for _, dien_nang in cac_dien_nang)
    ma_lon_nhat = max(cac_dien_nang, key=lambda cap: cap[1])[0]
    return tong, ma_lon_nhat


def giai_bai_toan_a_dao_thu_tu(danh_sach):
    """Biến thể sai: cộng dồn trước khi tính điện năng, nên tổng
    luôn cộng điện năng của động cơ trước. Biến thể này không
    còn in trong sách sau khi gộp tiểu mục; giữ lại vì bài tập
    mức 3 vẫn dùng dạng lỗi này."""
    tong = 0.0
    dien_nang = 0.0
    for _, cong_suat, gio in danh_sach:
        tong = tong + dien_nang
        dien_nang = cong_suat * gio
    return tong


def giai_bai_toan_a_nham_cong_suat(danh_sach):
    """Lỗi L1.1-3: nhân công suất danh định với 24 giờ cho mọi
    động cơ, bỏ số giờ chạy thật."""
    return sum(cong_suat * 24.0 for _, cong_suat, _ in danh_sach)


def cong_suat_tung_pha(tai_theo_pha):
    """Trả về từ điển {ten_pha: tong_cong_suat_kw}."""
    return {
        ten: sum(cac_tai) for ten, cac_tai in tai_theo_pha.items()
    }


def giai_bai_toan_b(tai_theo_pha, nguong=NGUONG_LECH_PHA):
    """Bài toán B: công suất từng pha, độ lệch và kết luận.

    Trả về (cong_suat, do_lech, lech_lon_nhat, dat). Phát sinh
    ZeroDivisionError khi tổng ba pha bằng 0, đúng như lỗi L1.2-2.
    """
    cong_suat = cong_suat_tung_pha(tai_theo_pha)
    tong = sum(cong_suat.values())
    trung_binh = tong / len(cong_suat)
    do_lech = {
        ten: (gia_tri - trung_binh) / trung_binh * 100.0
        for ten, gia_tri in cong_suat.items()
    }
    lech_lon_nhat = max(abs(gia_tri) for gia_tri in do_lech.values())
    return cong_suat, do_lech, lech_lon_nhat, lech_lon_nhat <= nguong


def giai_bai_toan_c(cac_tai, tai_cho_phep=TAI_CHO_PHEP_KN):
    """Bài toán C: tổng tải trên dầm và kết luận điều kiện bền."""
    tong = sum(cac_tai)
    return tong, tong <= tai_cho_phep


def giai_bai_toan_d(chi_phi_co_dinh, chi_phi_bien_doi, gia_ban):
    """Bài toán D: số sản phẩm hoà vốn, làm tròn lên.

    Phát sinh ValueError khi giá bán không lớn hơn chi phí biến
    đổi, vì khi đó bài toán không có điểm hoà vốn.
    """
    lai_mot_san_pham = gia_ban - chi_phi_bien_doi
    if lai_mot_san_pham <= 0:
        raise ValueError("gia ban khong lon hon chi phi bien doi")
    so_san_pham = chi_phi_co_dinh / lai_mot_san_pham
    return int(-(-so_san_pham // 1))


def giai_bai_toan_e(cac_so_do, nguong=NGUONG_PM25, dung_lon_hon=True):
    """Bài toán E: đếm số giờ vượt ngưỡng.

    dung_lon_hon=True dùng dấu lớn hơn, đúng theo đặc tả.
    dung_lon_hon=False dùng dấu lớn hơn hoặc bằng, là lỗi L1.5-2.
    Trả về (so_lan_vuot, cac_moc_tich_luy) để lập bảng vết.
    """
    so_lan_vuot = 0
    cac_moc = [0]
    for so_do in cac_so_do:
        vuot = so_do > nguong if dung_lon_hon else so_do >= nguong
        if vuot:
            so_lan_vuot = so_lan_vuot + 1
        cac_moc.append(so_lan_vuot)
    return so_lan_vuot, cac_moc


def bang_khau_hao(nguyen_gia, so_nam):
    """Trả về (muc_khau_hao_mot_nam, danh_sach_gia_tri_con_lai)."""
    muc_mot_nam = nguyen_gia / so_nam
    con_lai = []
    gia_tri = nguyen_gia
    for _ in range(so_nam):
        gia_tri = gia_tri - muc_mot_nam
        con_lai.append(gia_tri)
    return muc_mot_nam, con_lai


def bang_vet_bai_toan_a(danh_sach):
    """Lập bảng vết thực thi của bài toán A.

    Trả về danh sách dòng, mỗi dòng là
    (nhan_luot, i, dien_nang, tong, max_e, con_lap).
    Dòng đầu là dòng 'trước vòng lặp' theo khuôn Mục 1.5.1.
    """
    so_phan_tu = len(danh_sach)
    cac_dong = [("truoc vong lap", 0, None, 0.0, None, True)]
    tong = 0.0
    max_e = None
    for chi_so, (_, cong_suat, gio) in enumerate(danh_sach, start=1):
        dien_nang = cong_suat * gio
        tong = tong + dien_nang
        if max_e is None or dien_nang > max_e:
            max_e = dien_nang
        cac_dong.append(
            (str(chi_so), chi_so, dien_nang, tong, max_e,
             chi_so < so_phan_tu)
        )
    return cac_dong


def dem_buoc_bai_toan_a(so_dong_co):
    """Số bước thủ công khi giải bài toán A bằng tay.

    Một bước là một phép tính hoặc một phép so sánh: n phép nhân,
    n-1 phép cộng, n-1 phép so sánh.
    """
    if so_dong_co <= 0:
        return 0
    return 3 * so_dong_co - 2


def dem_buoc_bai_toan_b():
    """Số bước thủ công khi giải bài toán B theo dãy bước liền.

    Trả về từ điển {ten_nhom: so_buoc} để đếm lại được từng nhóm.
    """
    so_tai = {ten: len(cac_tai)
              for ten, cac_tai in TAI_BA_PHA.items()}
    return {
        "tong tung pha": sum(n - 1 for n in so_tai.values()),
        "tong ba pha": len(so_tai) - 1,
        "trung binh": 1,
        "ba do lech": 3 * len(so_tai),
        "tim lech lon nhat": len(so_tai) - 1,
        "so voi nguong": 1,
    }


def doc_tep_dong_co():
    """Đọc 04_DuLieu/Chuong1_DongCo.csv bằng module csv.

    Dùng cho Bài tập 1.9. Đường dẫn tương đối tính từ gốc dự án,
    không dùng đường dẫn tuyệt đối.
    """
    import csv
    from pathlib import Path

    duong_dan = (
        Path(__file__).resolve().parents[2]
        / "04_DuLieu" / "Chuong1_DongCo.csv"
    )
    with duong_dan.open(encoding="utf-8", newline="") as tep:
        return [
            (int(dong["ma_dong_co"]),
             float(dong["cong_suat_kw"]),
             float(dong["gio_chay"]),
             dong["ca"].strip())
            for dong in csv.DictReader(tep)
        ]


def giai_bai_tap_1_9(cac_dong_co):
    """Bài tập 1.9: tổng điện năng và động cơ lớn nhất theo ca.

    Trả về {ten_ca: (tong_kwh, ma_lon_nhat)}. Ca không có động cơ
    nào trả về (0.0, None). Phát sinh ValueError khi gặp tên ca
    ngoài hai giá trị hợp lệ.
    """
    cac_ca_hop_le = ("ngay", "dem")
    ket_qua = {}
    for ten_ca in cac_ca_hop_le:
        nhom = [
            (ma, cong_suat, gio)
            for ma, cong_suat, gio, ca in cac_dong_co
            if ca == ten_ca
        ]
        tong, ma_lon_nhat, _ = giai_bai_toan_a(nhom)
        ket_qua[ten_ca] = (round(tong, 1), ma_lon_nhat)
    for ma, _, _, ca in cac_dong_co:
        if ca not in cac_ca_hop_le:
            raise ValueError(f"ca khong hop le o dong co {ma}: {ca}")
    return ket_qua


# Bài gỡ lỗi GL1: ba lỗi cài sẵn, xem phần cuối Chương 1.
def giai_gl1_co_loi(tai_theo_pha):
    """Mã giả GL1 với lỗi logic ở dòng 7: khởi tạo tổng pha B
    bằng tải đầu tiên rồi vẫn cộng lại tải đó."""
    cong_suat = cong_suat_tung_pha(tai_theo_pha)
    cong_suat["B"] = tai_theo_pha["B"][0] + cong_suat["B"]
    tong = sum(cong_suat.values())
    trung_binh = tong / len(cong_suat)
    do_lech = {
        ten: (gia_tri - trung_binh) / trung_binh * 100.0
        for ten, gia_tri in cong_suat.items()
    }
    lech_lon_nhat = max(abs(gia_tri) for gia_tri in do_lech.values())
    return cong_suat, lech_lon_nhat, lech_lon_nhat <= NGUONG_LECH_PHA


def so_dai_luong_tinh_tay_a(so_dong_co):
    """Số đại lượng có tên khi giải bài toán A bằng tay.

    Mỗi động cơ sinh một đại lượng điện năng riêng, cộng thêm
    đại lượng tổng và đại lượng giá trị lớn nhất.
    """
    return so_dong_co + 2


# Mô hình tính toán của bài toán A, Mục 1.1.1: ba bước xử lý và
# sáu đại lượng có tên, không đổi theo số động cơ.
SO_BUOC_MO_HINH_A = 3
SO_DAI_LUONG_MO_HINH_A = 6


def so_buoc_sua_khi_doi_gio_chay(so_dong_co):
    """Số bước phải làm lại khi một giá trị giờ chạy thay đổi.

    Phải tính lại một phép nhân, rồi cộng lại và so lại toàn bộ:
    1 + (n - 1) + (n - 1) bước.
    """
    if so_dong_co <= 0:
        return 0
    return 2 * so_dong_co - 1


def so_buoc_soat_bai_toan_b(co_phan_ra):
    """Số bước phải soát lại khi kết quả bài toán B sai.

    Không phân rã thì phải soát cả dãy bước liền. Có phân rã thì
    chỉ soát phần lớn nhất, vì ba phần kiểm được độc lập.
    """
    cac_nhom = dem_buoc_bai_toan_b()
    if not co_phan_ra:
        return sum(cac_nhom.values())
    return max(
        cac_nhom["tong tung pha"],
        cac_nhom["ba do lech"],
        cac_nhom["trung binh"] + cac_nhom["tim lech lon nhat"]
        + cac_nhom["so voi nguong"],
    )


def in_bang_khoi_5():
    """In các bảng so sánh định lượng của Khối 5, Chương 1."""
    print("\nKhoi 5 Muc 1.1.1: tinh tay so voi mo hinh")
    cac_dong = [
        ("So buoc phai viet ra, n = 5",
         dem_buoc_bai_toan_a(5), SO_BUOC_MO_HINH_A),
        ("So dai luong co ten",
         so_dai_luong_tinh_tay_a(5), SO_DAI_LUONG_MO_HINH_A),
        ("So buoc sua khi mot gio chay doi",
         so_buoc_sua_khi_doi_gio_chay(5), 0),
        ("So buoc phai viet ra, n = 1 200",
         dem_buoc_bai_toan_a(1200), SO_BUOC_MO_HINH_A),
    ]
    for ten, cu, moi in cac_dong:
        print(f"  {ten:<34}{cu:>6}{moi:>8}")

    print("\nKhoi 5 Muc 1.2.1: day buoc lien so voi phan ra")
    tong_buoc = sum(dem_buoc_bai_toan_b().values())
    cac_dong_b = [
        ("So buoc thu cong", tong_buoc, tong_buoc),
        ("So dai luong co ten", 9, 9),
        ("So buoc phai soat khi ket qua sai",
         so_buoc_soat_bai_toan_b(False),
         so_buoc_soat_bai_toan_b(True)),
        ("So buoc viet lai cho tu thu hai", tong_buoc, 0),
    ]
    for ten, cu, moi in cac_dong_b:
        print(f"  {ten:<34}{cu:>6}{moi:>8}")


def in_bang_dap_so():
    """In mọi đáp số của Chương 1 để đối chiếu với dàn ý."""
    tong_a, ma_a, max_a = giai_bai_toan_a(DONG_CO_5)
    print("Bai toan A, bo 5 dong co")
    print(f"  tong dien nang      : {tong_a:.1f} kWh")
    print(f"  dong co lon nhat    : so {ma_a}, {max_a:.1f} kWh")
    print(f"  so buoc thu cong n=5   : {dem_buoc_bai_toan_a(5)}")
    print(f"  so buoc thu cong n=12  : {dem_buoc_bai_toan_a(12)}")
    print(f"  so buoc thu cong n=1200: {dem_buoc_bai_toan_a(1200)}")

    print("\nBa ma gia sai cua bai toan A")
    print(f"  L1.3-3 sai khoi tao : "
          f"{giai_bai_toan_a_sai_khoi_tao(DONG_CO_5):.1f} kWh")
    tong_lech, ma_lech = giai_bai_toan_a_lech_mot(DONG_CO_5)
    print(f"  L1.4-3 lech mot     : {tong_lech:.1f} kWh, "
          f"dong co so {ma_lech}")
    print(f"  bien the dao thu tu : "
          f"{giai_bai_toan_a_dao_thu_tu(DONG_CO_5):.1f} kWh")
    print(f"  L1.1-3 nham cong suat: "
          f"{giai_bai_toan_a_nham_cong_suat(DONG_CO_5):.1f} kWh")
    print(f"  ti so so voi dap an  : "
          f"{giai_bai_toan_a_nham_cong_suat(DONG_CO_5) / tong_a:.2f}")

    cong_suat, do_lech, lech_max, dat = giai_bai_toan_b(TAI_BA_PHA)
    print("\nBai toan B, do lech tai ba pha")
    for ten in sorted(cong_suat):
        print(f"  pha {ten}: {cong_suat[ten]:.1f} kW, "
              f"lech {do_lech[ten]:+.0f} %")
    print(f"  lech lon nhat       : {lech_max:.0f} %")
    print(f"  dat nguong 15 %     : {dat}")
    so_buoc_b = sum(dem_buoc_bai_toan_b().values())
    print(f"  so buoc thu cong    : {so_buoc_b}")

    tong_c, dat_c = giai_bai_toan_c(TAI_DAM_KN)
    print("\nBai toan C, dieu kien ben cua dam")
    print(f"  tong tai            : {tong_c:.1f} kN")
    print(f"  dat tai cho phep    : {dat_c}")

    so_san_pham = giai_bai_toan_d(
        CHI_PHI_CO_DINH, CHI_PHI_BIEN_DOI, GIA_BAN)
    print("\nBai toan D, diem hoa von")
    print(f"  so san pham hoa von : {so_san_pham}")

    so_vuot, cac_moc = giai_bai_toan_e(PM25_6_GIO)
    so_vuot_sai, _ = giai_bai_toan_e(PM25_6_GIO, dung_lon_hon=False)
    print("\nBai toan E, so gio PM2.5 vuot nguong")
    print(f"  dung dau lon hon    : {so_vuot} gio")
    print(f"  cac moc tich luy    : {cac_moc}")
    print(f"  dung dau lon hon hoac bang: {so_vuot_sai} gio")

    muc, con_lai = bang_khau_hao(NGUYEN_GIA, SO_NAM_SU_DUNG)
    print("\nBang khau hao duong thang")
    print(f"  muc mot nam         : {muc:.0f} nghin dong")
    print(f"  gia tri con lai     : "
          f"{[int(gia_tri) for gia_tri in con_lai]}")

    print("\nBang vet thuc thi bai toan A")
    print(f"  {'luot':<15}{'i':>3}{'E':>8}{'tong':>9}"
          f"{'max_E':>8}  con_lap")
    for nhan, i, dien_nang, tong, max_e, con_lap in \
            bang_vet_bai_toan_a(DONG_CO_5):
        chu_e = "-" if dien_nang is None else f"{dien_nang:.1f}"
        chu_max = "-" if max_e is None else f"{max_e:.1f}"
        print(f"  {nhan:<15}{i:>3}{chu_e:>8}{tong:>9.1f}"
              f"{chu_max:>8}  {con_lap}")


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    tong_a, ma_a, max_a = giai_bai_toan_a(DONG_CO_5)
    assert tong_a == 384.0, tong_a
    assert ma_a == 5, ma_a
    assert max_a == 110.0, max_a
    assert dien_nang_tung_dong_co(DONG_CO_5) == [
        (1, 60.0), (2, 90.0), (3, 36.0), (4, 88.0), (5, 110.0)
    ]

    cong_suat, do_lech, lech_max, dat_b = giai_bai_toan_b(TAI_BA_PHA)
    assert cong_suat == {"A": 10.0, "B": 7.0, "C": 13.0}, cong_suat
    assert do_lech["A"] == 0.0, do_lech
    assert abs(do_lech["B"] + 30.0) < 1e-9, do_lech
    assert abs(do_lech["C"] - 30.0) < 1e-9, do_lech
    assert abs(lech_max - 30.0) < 1e-9, lech_max
    assert dat_b is False

    tong_c, dat_c = giai_bai_toan_c(TAI_DAM_KN)
    assert tong_c == 41.0, tong_c
    assert dat_c is True

    assert giai_bai_toan_d(
        CHI_PHI_CO_DINH, CHI_PHI_BIEN_DOI, GIA_BAN) == 4000

    so_vuot, cac_moc = giai_bai_toan_e(PM25_6_GIO)
    assert so_vuot == 3, so_vuot
    assert cac_moc == [0, 0, 1, 2, 2, 2, 3], cac_moc

    muc, con_lai = bang_khau_hao(NGUYEN_GIA, SO_NAM_SU_DUNG)
    assert muc == 120000.0, muc
    assert con_lai == [480000.0, 360000.0, 240000.0, 120000.0, 0.0]

    # Ba mã giả sai dùng trong Khối 7 của các mục 1.4 và 1.5.
    assert giai_bai_toan_a_sai_khoi_tao(DONG_CO_5) == 444.0
    assert giai_bai_toan_a_lech_mot(DONG_CO_5) == (274.0, 2)
    assert giai_bai_toan_a_dao_thu_tu(DONG_CO_5) == 274.0
    assert giai_bai_toan_a_nham_cong_suat(DONG_CO_5) == 1404.0

    # Số bước thủ công in trong Khối 2 và Khối 5.
    assert dem_buoc_bai_toan_a(5) == 13
    assert dem_buoc_bai_toan_a(12) == 34
    assert dem_buoc_bai_toan_a(1200) == 3598
    assert sum(dem_buoc_bai_toan_b().values()) == 20
    assert so_dai_luong_tinh_tay_a(5) == 7
    assert so_dai_luong_tinh_tay_a(1200) == 1202
    assert so_buoc_sua_khi_doi_gio_chay(5) == 9
    assert so_buoc_soat_bai_toan_b(False) == 20
    assert so_buoc_soat_bai_toan_b(True) == 9
    assert so_buoc_sua_khi_doi_gio_chay(0) == 0

    # Bảng vết thực thi: 6 dòng cho bộ 5 động cơ.
    bang_vet = bang_vet_bai_toan_a(DONG_CO_5)
    assert len(bang_vet) == 6, len(bang_vet)
    assert bang_vet[0][3] == 0.0
    assert bang_vet[-1][3] == 384.0
    assert bang_vet[-1][4] == 110.0
    assert bang_vet[-1][5] is False
    assert [dong[3] for dong in bang_vet[1:]] == [
        60.0, 150.0, 186.0, 274.0, 384.0
    ]

    # Bài tập 1.9 trên tệp dữ liệu 12 động cơ.
    cac_dong_co = doc_tep_dong_co()
    assert len(cac_dong_co) == 12, len(cac_dong_co)
    assert cac_dong_co[:5] == [
        (1, 7.5, 8.0, "ngay"), (2, 15.0, 6.0, "ngay"),
        (3, 3.0, 12.0, "dem"), (4, 22.0, 4.0, "ngay"),
        (5, 11.0, 10.0, "dem"),
    ], cac_dong_co[:5]
    ket_qua_1_9 = giai_bai_tap_1_9(cac_dong_co)
    assert ket_qua_1_9["ngay"] == (497.5, 2), ket_qua_1_9
    assert ket_qua_1_9["dem"] == (336.7, 5), ket_qua_1_9

    # Bài gỡ lỗi GL1: lỗi logic làm kết luận lật từ sai thành đúng.
    cong_suat_gl1, lech_gl1, dat_gl1 = giai_gl1_co_loi(TAI_BA_PHA)
    assert cong_suat_gl1["B"] == 12.0, cong_suat_gl1
    assert abs(lech_gl1 - 14.2857) < 1e-3, lech_gl1
    assert dat_gl1 is True
    assert giai_bai_toan_b(TAI_BA_PHA)[3] is False

    # --- Trường hợp biên --------------------------------------
    # Danh sách rỗng: theo đặc tả Mục 1.1.1 trả về 0,0 kWh.
    assert giai_bai_toan_a([]) == (0.0, None, None)
    assert dem_buoc_bai_toan_a(0) == 0
    assert dem_buoc_bai_toan_a(1) == 1
    # Hai động cơ bằng nhau: lấy mã nhỏ hơn.
    assert giai_bai_toan_a(
        [(1, 10.0, 11.0), (2, 11.0, 10.0)]) == (220.0, 1, 110.0)
    # Số đo đúng bằng ngưỡng không tính là vượt.
    assert giai_bai_toan_e([50.0])[0] == 0
    assert giai_bai_toan_e([50.0], dung_lon_hon=False)[0] == 1
    # Lỗi L1.5-2: bộ dữ liệu không có điểm biên che được lỗi.
    bo_khong_co_bien = [42.0, 55.0, 61.0, 48.0, 73.0]
    assert (giai_bai_toan_e(bo_khong_co_bien)[0]
            == giai_bai_toan_e(bo_khong_co_bien,
                               dung_lon_hon=False)[0] == 3)
    # Độ lệch đúng bằng ngưỡng 15 % vẫn được coi là đạt.
    _, _, lech_bien, dat_bien = giai_bai_toan_b(
        {"A": [11.5], "B": [10.0], "C": [8.5]})
    assert abs(lech_bien - 15.0) < 1e-9, lech_bien
    assert dat_bien is True
    # Tổng tải đúng bằng tải cho phép vẫn đạt.
    assert giai_bai_toan_c([50.0]) == (50.0, True)

    # --- Trường hợp ngoại lệ -----------------------------------
    # L1.2-2: ba pha không mang tải thì phép chia không thực hiện.
    try:
        giai_bai_toan_b({"A": [0.0], "B": [0.0], "C": [0.0]})
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("thieu ZeroDivisionError khi tong = 0")
    # Bài toán D không có đáp số khi giá bán không bù chi phí.
    try:
        giai_bai_toan_d(240000.0, 95.0, 95.0)
    except ValueError:
        pass
    else:
        raise AssertionError("thieu ValueError khi g <= c_bd")
    # Bài tập 1.9: tên ca ngoài hai giá trị hợp lệ phải bị chặn.
    try:
        giai_bai_tap_1_9([(1, 7.5, 8.0, "chieu")])
    except ValueError:
        pass
    else:
        raise AssertionError("ca khong hop le ma van chay")
    # Ca không có động cơ nào trả về 0,0 kWh.
    assert giai_bai_tap_1_9(
        [(1, 7.5, 8.0, "ngay")])["dem"] == (0.0, None)

    # Mã giả sai khởi tạo không chạy được trên danh sách rỗng.
    try:
        giai_bai_toan_a_sai_khoi_tao([])
    except IndexError:
        pass
    else:
        raise AssertionError("thieu IndexError tren danh sach rong")

    in_bang_dap_so()
    in_bang_khoi_5()
