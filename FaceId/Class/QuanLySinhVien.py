class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sinh_vien.append(sinh_vien)

    def kiem_tra_ton_tai(self, mssv):
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.maSV == mssv:
                return True
        return False

    def lay_sinh_vien_theo_mssv(self, mssv):
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.maSV == mssv:
                return sinh_vien
        return None

    def in_danh_sach_sinh_vien(self):
        for sinh_vien in self.danh_sach_sinh_vien:
            sinh_vien.inThongTin()
            print()  # In một dòng trống giữa các sinh viên