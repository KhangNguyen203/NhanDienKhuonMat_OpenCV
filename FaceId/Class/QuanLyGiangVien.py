class QuanLyGiangVien:
    def __init__(self):
        self.danh_sach_giang_vien = []

    def them_giang_vien(self, giang_vien):
        self.danh_sach_giang_vien.append(giang_vien)

    def dang_nhap(self, ten_dang_nhap, mat_khau):
        for giang_vien in self.danh_sach_giang_vien:
            if giang_vien.ID == ten_dang_nhap and giang_vien.matKhau == mat_khau:
                return giang_vien
        return None