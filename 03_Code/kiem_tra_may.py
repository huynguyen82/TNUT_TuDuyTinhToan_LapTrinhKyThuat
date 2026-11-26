# -*- coding: utf-8 -*-
"""
Mã bài      : công cụ của tài liệu thực hành
Chương, mục : Tài liệu thực hành, phần Chuẩn bị máy
Đề bài      : Kiểm xem một máy đã đủ điều kiện làm bài thực hành
              TEE109 chưa. Kiểm năm hạng mục: phiên bản Python,
              NumPy, Matplotlib, quyền ghi tệp, và khả năng vẽ rồi
              lưu một đồ thị. In bảng kết quả và một dòng kết luận.
              Giảng viên chạy để chuẩn bị phòng máy; người học chạy
              để kiểm máy của mình trước buổi.
Đầu vào     : không có; chương trình tự dò môi trường đang chạy
Đầu ra      : bảng năm hạng mục và một dòng kết luận
Python      : 3.12
Thư viện    : thư viện chuẩn, cộng NumPy và Matplotlib nếu có
Cài đặt     : xem phần Chuẩn bị máy của tài liệu thực hành
"""

import importlib
import platform
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PYTHON_CAN = (3, 12)
THU_VIEN_CAN = {
    "numpy": "2.1.3",
    "matplotlib": "3.9.2",
}
DAU_DAT = "DAT"
DAU_LECH = "LECH"
DAU_THIEU = "THIEU"


def tach_so(chuoi):
    """Tra ve bo so cua mot chuoi phien ban, bo phan chu."""
    cac_so = []
    for phan in chuoi.split("."):
        so = ""
        for ky_tu in phan:
            if not ky_tu.isdigit():
                break
            so = so + ky_tu
        if not so:
            break
        cac_so.append(int(so))
    return tuple(cac_so)


def so_sanh_phien_ban(dang_co, can_co):
    """Tra ve DAT khi hai phien ban trung nhau, nguoc lai LECH.

    So theo so, khong so theo chu, nen "3.12.0" va "3.12" khong
    bang nhau o dang chuoi nhung deu khop yeu cau 3.12.
    """
    a = tach_so(dang_co)
    b = tach_so(can_co)
    n = min(len(a), len(b))
    return DAU_DAT if a[:n] == b[:n] else DAU_LECH


def kiem_python():
    """Tra ve (ten, can co, dang co, ket luan) cho Python."""
    dang_co = platform.python_version()
    can_co = ".".join(str(so) for so in PYTHON_CAN)
    return ("Python", can_co, dang_co,
            so_sanh_phien_ban(dang_co, can_co))


def kiem_thu_vien(ten, can_co):
    """Tra ve mot dong ket qua cho mot thu vien ngoai."""
    try:
        mo_dun = importlib.import_module(ten)
    except ImportError:
        return (ten, can_co, "chua cai", DAU_THIEU)
    dang_co = getattr(mo_dun, "__version__", "khong ro")
    return (ten, can_co, dang_co,
            so_sanh_phien_ban(dang_co, can_co))


def kiem_ghi_tep():
    """Thu ghi mot tep tam roi doc lai, de biet co quyen ghi."""
    try:
        thu_muc = Path(tempfile.gettempdir())
        tep = thu_muc / "tee109_kiem_tra_may.txt"
        tep.write_text("45.0\n72.5\n", encoding="utf-8")
        doc_duoc = tep.read_text(encoding="utf-8").strip()
        tep.unlink()
    except OSError as loi:
        return ("Ghi tep", "ghi duoc", str(loi)[:24], DAU_THIEU)
    dat = DAU_DAT if doc_duoc.startswith("45.0") else DAU_LECH
    return ("Ghi tep", "ghi duoc", "ghi va doc lai duoc", dat)


def kiem_ve_do_thi():
    """Thu ve mot do thi roi luu ra tep, khong mo cua so."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return ("Ve do thi", "luu duoc", "chua cai", DAU_THIEU)
    tep = Path(tempfile.gettempdir()) / "tee109_do_thi.png"
    hinh, truc = plt.subplots()
    truc.plot([0, 1, 2], [45.0, 72.5, 90.0])
    truc.set_xlabel("Gio")
    truc.set_ylabel("Nhiet do (do C)")
    hinh.savefig(tep)
    plt.close(hinh)
    co_tep = tep.exists() and tep.stat().st_size > 0
    if co_tep:
        tep.unlink()
    return ("Ve do thi", "luu duoc",
            "luu duoc" if co_tep else "khong luu duoc",
            DAU_DAT if co_tep else DAU_LECH)


def kiem_tat_ca():
    """Tra ve danh sach nam dong ket qua."""
    cac_dong = [kiem_python()]
    for ten, can_co in THU_VIEN_CAN.items():
        cac_dong.append(kiem_thu_vien(ten, can_co))
    cac_dong.append(kiem_ghi_tep())
    cac_dong.append(kiem_ve_do_thi())
    return cac_dong


def in_bang(cac_dong):
    """In bang ket qua va mot dong ket luan."""
    print("KIEM TRA MAY CHO THUC HANH TEE109")
    print()
    dau = (f"{'Hang muc':<12}{'Can co':<12}"
           f"{'Dang co':<22}{'Ket luan':<8}")
    print(dau)
    print("-" * len(dau))
    for ten, can_co, dang_co, ket_luan in cac_dong:
        print(f"{ten:<12}{can_co:<12}{dang_co:<22}{ket_luan:<8}")
    print("-" * len(dau))
    so_lech = sum(1 for d in cac_dong if d[3] != DAU_DAT)
    if so_lech == 0:
        print("May da du dieu kien lam bai thuc hanh.")
    else:
        print(f"Con {so_lech} hang muc chua dat. "
              "Xem phan Chuan bi may cua tai lieu thuc hanh.")
    return so_lech


if __name__ == "__main__":
    # Khối tự kiểm chạy **trước** và không in gì, để phần người
    # học nhìn thấy chỉ gồm đúng bảng kết quả.

    # Tách số bỏ được phần chữ của chuỗi phiên bản.
    assert tach_so("3.12.0") == (3, 12, 0)
    assert tach_so("2.1.3") == (2, 1, 3)
    assert tach_so("3.9.2rc1") == (3, 9, 2)

    # So phiên bản theo số, không theo chuỗi.
    assert so_sanh_phien_ban("3.12.0", "3.12") == DAU_DAT
    assert so_sanh_phien_ban("3.13.9", "3.12") == DAU_LECH
    assert so_sanh_phien_ban("2.1.3", "2.1.3") == DAU_DAT

    # Năm hạng mục, mỗi hạng mục đủ bốn ô.
    assert len(kiem_tat_ca()) == 5
    assert all(len(d) == 4 for d in kiem_tat_ca())

    # --- in-sach ---
    cac_dong = kiem_tat_ca()
    in_bang(cac_dong)
    # --- het-in-sach ---
