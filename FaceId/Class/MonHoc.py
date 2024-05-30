class MonHoc:
    id_counter = 1

    def __init__(self, tenMH):
        self.ID = MonHoc.id_counter
        MonHoc.id_counter += 1
        self.tenMH = tenMH

    def inThongTin(self):
        print("ID:", self.ID)
        print("Tên môn học:", self.tenMH)
        print("Môn học của học kỳ:", self.hocKy)
        