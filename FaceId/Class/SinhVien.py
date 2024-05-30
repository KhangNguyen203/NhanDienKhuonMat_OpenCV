class SinhVien:
    def __init__(self, maSV, hoTen, gioiTinh, quenQuan, khoaHoc, lop):
        self.maSV = maSV
        self.hoTen = hoTen
        self.lop = lop
        self.gioiTinh = gioiTinh
        self.quenQuan = quenQuan
        self.khoaHoc = khoaHoc

    def inThongTin(self):
        print("Mã sinh viên:", self.maSV)
        print("Họ và tên:", self.hoTen)
        print("Giới tính:", self.gioiTinh)
        print("Quê quán:", self.quenQuan)
        print("Khóa học:", self.khoaHoc)