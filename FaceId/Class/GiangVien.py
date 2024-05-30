class GiangVien:
    id_counter = 1
    
    def __init__(self, id, hoTen, matKhau, khoa):
        self.ID = id
        self.hoTen = hoTen
        self.matKhau = matKhau
        self.khoa = khoa

    def inThongTin(self):
        print("ID:", self.ID)
        print("Họ và tên:", self.hoTen)
        print("Mật khẩu:", self.matKhau)
        print("Khoa:", self.khoa)