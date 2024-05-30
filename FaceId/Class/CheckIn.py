from datetime import date

class CheckIn:
    def __init__(self, giang_day):
        self.giang_day = giang_day
        self.danh_sach_sinh_vien_di_hoc = []
        self.danh_sach_sinh_vien_vang = []
        self.ngay_diem_danh = date.today()

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sinh_vien.append(sinh_vien)

    def diem_danh(self, sinh_vien, di_hoc=True):
        if sinh_vien in self.danh_sach_sinh_vien:
            if di_hoc:
                self.danh_sach_sinh_vien_di_hoc.append(sinh_vien)
            else:
                self.danh_sach_sinh_vien_vang.append(sinh_vien)
        else:
            print("Sinh viên không có trong danh sách.")

    def in_danh_sach_di_hoc(self):
        print("Danh sách sinh viên đi học:")
        for sinh_vien in self.danh_sach_sinh_vien_di_hoc:
            print(sinh_vien.hoTen)

    def in_danh_sach_vang(self):
        print("Danh sách sinh viên vắng:")
        for sinh_vien in self.danh_sach_sinh_vien_vang:
            print(sinh_vien)