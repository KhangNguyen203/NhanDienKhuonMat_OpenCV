from Class.GiangVien import GiangVien
from Class.MonHoc import MonHoc
from Class.SinhVien import SinhVien
from Class.GiangDay import GiangDay
from Class.QuanLySinhVien import QuanLySinhVien
from Class.QuanLyGiangVien import QuanLyGiangVien
from Class.QuanLyGiangDay import QuanLyGiangDay
from Class.CheckIn import CheckIn


# Tạo 3 môn học
mon_hoc1 = MonHoc("Mã Nguồn Mở")
mon_hoc2 = MonHoc("Lập Trình Giao Diện")
mon_hoc3 = MonHoc("Hướng Đối Tượng")



#Tạo và thêm sinh viên vào danh sách QLSV
quan_ly_sv = QuanLySinhVien()
sv1 = SinhVien("2051050001", "Nguyễn Khang", "Nam", "Bình Phước", "K20", "DH20IT01")
sv2 = SinhVien("2051050002", "Nguyễn Thị B", "Nữ", "Hồ Chí Minh", "K20", "DH20IT02")
sv3 = SinhVien("2051050003", "Trần Văn An", "Nam", "Đà Nẵng", "K20", "DH20IT01")
sv4 = SinhVien("2051050004", "Đoàn Thị Minh", "Nữ", "Hồ Chí Minh", "K20", "DH20IT03")
sv5 = SinhVien("2051050005", "Nguyễn Minh Anh ", "Nữ", "Lâm Đồng", "K20", "DH20IT02")
sv6 = SinhVien("2051050006", "Cao Ngọc Hiếu", "Nam", "Bình Phước", "K20", "DH20IT03")
sv7 = SinhVien("2051050007", "Phan Hoàng Đạt", "Nam", "Bình Phước", "K20", "DH20IT01")
sv8 = SinhVien("2051050008", "Hồ Hữu Thắng", "Nam", "Bình Phước", "K20", "DH20IT01")
sv9 = SinhVien("2051050009", "Đoàn Thị Thu Phương", "Nữ", "Bình Phước", "K20", "DH20IT02")
quan_ly_sv.them_sinh_vien(sv1)
quan_ly_sv.them_sinh_vien(sv2)
quan_ly_sv.them_sinh_vien(sv3)
quan_ly_sv.them_sinh_vien(sv4)
quan_ly_sv.them_sinh_vien(sv5)
quan_ly_sv.them_sinh_vien(sv6)
quan_ly_sv.them_sinh_vien(sv7)
quan_ly_sv.them_sinh_vien(sv8)
quan_ly_sv.them_sinh_vien(sv9)



# Tạo và thêm giảng viên vào danh sách QuanLyGiangVien
quan_ly_gv = QuanLyGiangVien()
gv1 = GiangVien("001","Hồ Hứa Thiên", "123456", "Khoa Công nghệ thông tin")
gv2 = GiangVien("002", "Nguyễn Văn A", "123456", "Khoa Kinh tế")
quan_ly_gv.them_giang_vien(gv1)
quan_ly_gv.them_giang_vien(gv2)


# Sử dụng lớp QuanLyGiangDay
quan_ly_giang_day = QuanLyGiangDay()

#Tạo GiangDay
giang_day1 = GiangDay(mon_hoc1, gv1, "Học kỳ 1")
giang_day1.themSinhVien(sv1)
giang_day1.themSinhVien(sv6)
giang_day1.themSinhVien(sv2)
giang_day1.themSinhVien(sv8)
giang_day1.themSinhVien(sv3)
giang_day1.themSinhVien(sv5)
giang_day1.themSinhVien(sv9)
giang_day1.themSinhVien(sv4)
giang_day1.themSinhVien(sv7)


giang_day3 = GiangDay(mon_hoc2, gv2, "Học kỳ 2")

# Thêm các đối tượng GiangDay vào danh sách
quan_ly_giang_day.them_giang_day(giang_day1)
quan_ly_giang_day.them_giang_day(giang_day3)




