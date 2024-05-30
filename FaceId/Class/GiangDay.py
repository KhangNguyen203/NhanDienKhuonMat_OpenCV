class GiangDay:
    def __init__(self, monHoc, giangVien, hk):
        self.monHoc = monHoc
        self.giangVien = giangVien
        self.sinhVien = []
        self.hocKy = hk

    def themSinhVien(self, sinhVien):
        self.sinhVien.append(sinhVien)

    def inThongTin(self):
        print("Môn học:", self.monHoc.tenMH)
        print("Giảng viên:", self.giangVien.hoTen)
        print("Danh sách sinh viên:")
        for sv in self.sinhVien:
            print(sv.hoTen)
        print("",self.hocKy)

        