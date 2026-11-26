# -*- coding: utf-8 -*-
"""
Mã bài      : BT 2.6
Chương, mục : Chương 2, Mục 2.3.1
Đề bài      : In phiếu báo điện năng của phân xưởng theo mẫu ba
              cột: tên ca căn trái trong 10 ký tự, tổng điện
              năng căn phải trong 8 ký tự với một chữ số thập
              phân, rồi đơn vị.
Đầu vào     : tên ca và tổng điện năng, kWh
Đầu ra      : một dòng phiếu đúng định dạng
Python      : 3.12
Thư viện    : chỉ thư viện chuẩn
Cài đặt     : không cần cài thêm

Lời giải trình bày ở tệp .md cùng tên. Số liệu lấy từ đáp số
Bài tập 1.9: ca ngày 497,5 kWh và ca đêm 336,7 kWh.
"""

BE_RONG_TEN_CA = 10
BE_RONG_SO = 8
SO_CHU_SO_THAP_PHAN = 1
PHIEU = (("ngay", 497.5), ("dem", 336.7))


def dong_phieu(ten_ca, dien_nang_kwh):
    """Một dòng phiếu theo đúng mẫu ba cột."""
    return (f"{ten_ca:<{BE_RONG_TEN_CA}}"
            f"{dien_nang_kwh:>{BE_RONG_SO}.{SO_CHU_SO_THAP_PHAN}f}"
            f" kWh")


def phan_so_cua_dong(dong):
    """Trích phần cột số của một dòng phiếu."""
    return dong[BE_RONG_TEN_CA:BE_RONG_TEN_CA + BE_RONG_SO]


if __name__ == "__main__":
    # --- Trường hợp thường -------------------------------------
    assert dong_phieu("ngay", 497.5) == "ngay         497.5 kWh"
    assert dong_phieu("dem", 336.7) == "dem          336.7 kWh"
    # Hai dòng dài bằng nhau, nên cột số thẳng hàng.
    assert (len(dong_phieu("ngay", 497.5))
            == len(dong_phieu("dem", 336.7)))

    # --- Trường hợp biên ---------------------------------------
    # Giá trị tròn vẫn in đủ một chữ số thập phân, nên vẫn thẳng
    # cột với dòng trên. Đây là chỗ print thô làm hỏng bảng.
    assert dong_phieu("dem", 500.0) == "dem          500.0 kWh"
    assert phan_so_cua_dong(dong_phieu("dem", 500.0)) == "   500.0"
    assert (len(dong_phieu("dem", 500.0))
            == len(dong_phieu("ngay", 497.5)))
    # Tên ca đúng bằng bề rộng cột thì không còn dấu cách ngăn.
    assert dong_phieu("1234567890", 1.0).startswith("1234567890")
    # Giá trị 0 vẫn giữ đúng định dạng.
    assert phan_so_cua_dong(dong_phieu("ngay", 0.0)) == "     0.0"

    # --- Trường hợp ngoại lệ -----------------------------------
    # Tên ca dài hơn bề rộng cột thì cột bị đẩy, không bị cắt.
    dong_dai = dong_phieu("ca_dem_keo_dai", 336.7)
    assert len(dong_dai) > len(dong_phieu("dem", 336.7))
    assert dong_dai.startswith("ca_dem_keo_dai")
    # Bề rộng âm không báo lỗi mà bị bỏ qua, nên không dùng
    # được làm phép kiểm. Trường hợp thật sự bị chặn là áp đặc
    # tả số thực lên một chuỗi, tức quên ép kiểu sau input.
    assert f"{1.0:>{-8}.1f}" == "     1.0"
    da_chan = False
    try:
        f"{'50.03':.1f}"
    except ValueError as loi:
        da_chan = "Unknown format code 'f'" in str(loi)
    assert da_chan, "chuoi voi dac ta so thuc ma van dinh dang"

    print("BT 2.6")
    for ten_ca, dien_nang in PHIEU:
        print(f"  {dong_phieu(ten_ca, dien_nang)}")
