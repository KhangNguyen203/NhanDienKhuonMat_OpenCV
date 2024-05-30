class QuanLyGiangDay:
    def __init__(self):
        self.danh_sach_giang_day = []

    def them_giang_day(self, giang_day):
        self.danh_sach_giang_day.append(giang_day)

    def lay_mon_hoc_theo_giang_vien(self, ten_giang_vien):
        mon_hoc_tim_thay = []
        for giang_day in self.danh_sach_giang_day:
            if giang_day.giangVien.hoTen == ten_giang_vien:
                mon_hoc_tim_thay.append(giang_day.monHoc)
        return mon_hoc_tim_thay

    def lay_danh_sach_sinh_vien(self, ten_giang_vien, ten_mon_hoc, hoc_ky):
        danh_sach_sinh_vien = []
        for giang_day in self.danh_sach_giang_day:
            if giang_day.giangVien.hoTen == ten_giang_vien and \
               giang_day.monHoc.tenMH == ten_mon_hoc and \
               giang_day.hocKy == hoc_ky:
                danh_sach_sinh_vien.extend(giang_day.sinhVien)
        return danh_sach_sinh_vien

    def lay_giang_day(self, ten_giang_vien, ten_mon_hoc, hoc_ky):
        giang_day_tim_thay = None
        for giang_day in self.danh_sach_giang_day:
            if giang_day.giangVien.hoTen == ten_giang_vien and \
               giang_day.monHoc.tenMH == ten_mon_hoc and \
               giang_day.hocKy == hoc_ky:
                giang_day_tim_thay = giang_day
                break
        return giang_day_tim_thay

        def in_thong_tin(self):
            for giang_day in self.danh_sach_giang_day:
                print("Giảng viên:", giang_day.giangVien.hoTen)
                print("Môn học:", giang_day.monHoc.tenMH)
                print("Học kỳ:", giang_day.hocKy)
                print("------------------")
