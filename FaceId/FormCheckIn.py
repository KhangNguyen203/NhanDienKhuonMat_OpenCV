from tkinter import *
from tkinter.ttk import Combobox
from AvailableData import quan_ly_giang_day, quan_ly_sv
from tkinter import messagebox, Frame, font
from getData import GetData
from traningData import TrainingData
import cv2
from datetime import datetime
from RecognitionData import RecognitionData
from Class.CheckIn import CheckIn
from Class.SinhVienDiemDanh import SinhVienDiemDanh
import queryDB as db


class DiemDanh:
    #Hàm cập nhật thông tin sinh viên khi checkin thành công
    def cap_nhat_thong_tin_sv(self, group_box): 
        label_ten_sv = Label(group_box, text="Tên sinh viên:")
        label_ten_sv.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        label_ma_sv = Label(group_box, text="Mã số sinh viên:")
        label_ma_sv.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        label_lop = Label(group_box, text="Lớp:")
        label_lop.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        if self.sv_checked is not None: 
            label_sv_value = Label(group_box, text= self.sv_checked.hoTen)
            label_sv_value.grid(row=0, column=1, padx=10, pady=5, sticky=W)

            entry_ma_sv = Label(group_box, text= self.sv_checked.maSV)
            entry_ma_sv.grid(row=1, column=1, padx=10, pady=5, sticky=W)

            combo_lop = Label(group_box, text= self.sv_checked.lop)
            combo_lop.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        else: 
            label_sv_value = Label(group_box, text="                       ")
            label_sv_value.grid(row=0, column=1, padx=10, pady=5, sticky=W)

            entry_ma_sv = Label(group_box, text="")
            entry_ma_sv.grid(row=1, column=1, padx=10, pady=5, sticky=W)

            combo_lop = Label(group_box, text="")
            combo_lop.grid(row=2, column=1, padx=10, pady=5, sticky=W)

    def cap_nhat_tong(self, tong, hiendien, vang): 
        custom_font = font.Font(size=9, weight="bold")

        #Tạo groupBox lưu thông tin tổng số, hiện diện, vắng và thời gian hiện tại
        group_box3 = LabelFrame(self.window, text="Tổng Số")
        group_box3.grid(row=1, column= 1, padx=10, pady=10)

        label_tong = Label(group_box3, text="Tổng Số:")
        label_tong.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        label_hien_dien = Label(group_box3, text="Hiện Diện:" )
        label_hien_dien.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        label_vang = Label(group_box3, text="Vắng:")
        label_vang.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        label_tong_value = Label(group_box3, text= tong)
        label_tong_value.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        label_hien_dien_value = Label(group_box3, text= hiendien)
        label_hien_dien_value.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        label_vang_value = Label(group_box3, text= vang)
        label_vang_value.grid(row=2, column=1, padx=10, pady=5, sticky=W) 

        def update_thoi_gian():
            current_time = datetime.now().strftime("          Time: %H:%M:%S, ngày %d/%m/20%y")
            label_thoi_gian.config(text=current_time)
            label_thoi_gian.after(1000, update_thoi_gian)

        label_thoi_gian = Label(group_box3, text="", font=custom_font)
        label_thoi_gian.grid(row=3, column=0, padx=0, pady=0, )  
        update_thoi_gian()

    def __init__(self, giang_vien):
        self.sinh_vien_diem_danh = None
        self.giang_vien = giang_vien
        self.check_in = None
        self.sv_checked = None
        self.mon_hoc_gv = quan_ly_giang_day.lay_mon_hoc_theo_giang_vien(self.giang_vien.hoTen)
        self.danh_sach_sinh_vien = []
        self.giang_day = None
        self.window = Tk()
        self.window.title("Điểm danh")
        self.group_box = None

        window_width = 650
        window_height = 650

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    #Tạo frame_container chứa: groupBox và button
        frame_container = Frame(self.window)
        frame_container.grid(row=0, column=0, padx=10, pady=0)

        self.group_box = LabelFrame(frame_container, text="Thông tin sinh viên điểm danh")
        self.group_box.grid(row=0, column=0, padx=10, pady=10)

        self.cap_nhat_thong_tin_sv(self.group_box)

        def xu_ly_diem_danh():
            if self.giang_day is None:
                messagebox.showerror("Thông báo", "Vui lòng chọn lớp!")
            else:
                recognition = RecognitionData()
                recognition.run()

                if recognition.id is not None and recognition.name is not None:
                    is_dd = False

                    if self.check_in is None:
                        self.check_in = CheckIn(self.giang_day)

                    for sv in self.giang_day.sinhVien:
                        if str(recognition.id) == sv.maSV:
                            is_dd = True
                            self.sv_checked = sv
                            break

                    if is_dd:
                        self.cap_nhat_thong_tin_sv(self.group_box)
                        svdd = None
                        for sv in self.check_in.danh_sach_sinh_vien_di_hoc:
                            if sv.sinhSien.maSV == self.sv_checked.maSV:
                                sv.diemDanhLuc = datetime.now()
                                svdd = sv
                                break

                        if svdd is None:
                            svdd = SinhVienDiemDanh(self.sv_checked, self.giang_day.monHoc, self.giang_day.hocKy, self.giang_day.giangVien, datetime.now())
                            self.check_in.danh_sach_sinh_vien_di_hoc.append(svdd)

                        listbox_sv_dihoc.delete(0, END)
                        for sv in self.check_in.danh_sach_sinh_vien_di_hoc:
                            thoi_diem = sv.diemDanhLuc.strftime("%H:%M:%S")
                            listbox_sv_dihoc.insert(END, sv.sinhSien.hoTen + " - " + sv.sinhSien.maSV + " ( at: " + thoi_diem + " )")

                        self.cap_nhat_tong(len(self.giang_day.sinhVien), len(self.check_in.danh_sach_sinh_vien_di_hoc), len(self.giang_day.sinhVien) - len(self.check_in.danh_sach_sinh_vien_di_hoc))
                        messagebox.showinfo("Thông báo", "Đã điểm danh, sinh viên: " + self.sv_checked.maSV)
                    else:
                        messagebox.showinfo("Thông báo", "Không tìm thấy sinh viên!")
                else:
                    messagebox.showinfo("Thông báo", "Lỗi nhận diện sinh viên!")  

        button_diemdanh = Button(frame_container, text="Điểm danh", width=25, height=5, bg="blue", command= xu_ly_diem_danh)
        button_diemdanh.grid(row=1, column=0, padx=10, pady=10)
    #---------------------------------------------------

    #Tạo groupBox lưu thông tin của 1 Môn, lớp, học kì, môn học
        group_box2 = LabelFrame(self.window, text="Chọn")
        group_box2.grid(row=0, column=1, padx=10, pady=10)

        label_khoa = Label(group_box2, text="Khoa:")
        label_khoa.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        label_gv = Label(group_box2, text="Giảng viên:")
        label_gv.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        label_hk = Label(group_box2, text="Học kỳ:")
        label_hk.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        label_mh = Label(group_box2, text="Môn học:")
        label_mh.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        label_khoa_value = Label(group_box2, text= self.giang_vien.khoa)
        label_khoa_value.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        label_gv_value = Label(group_box2, text= self.giang_vien.hoTen)
        label_gv_value.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        combo_kh = Combobox(group_box2, state="readonly")
        combo_kh["values"] = ("Học kỳ 1", "Học kỳ 2")
        combo_kh.current(0)
        combo_kh.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        if self.mon_hoc_gv is not []:
            combo_mh = Combobox(group_box2, state="readonly")
            combo_mh["values"] = [mh.tenMH for mh in self.mon_hoc_gv]
            combo_mh.current(0)
            combo_mh.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        else: 
            combo_mh = Combobox(group_box2, state="readonly")
            combo_mh["values"] = ("(Trống)")
            combo_mh.current(0)
            combo_mh.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        def handle_loc_button_click():
            #Giá trị của kỳ học và môn học
            selected_hoc_ky = combo_kh.get()
            selected_mon_hoc = combo_mh.get()
            
            
            self.danh_sach_sinh_vien = quan_ly_giang_day.lay_danh_sach_sinh_vien(self.giang_vien.hoTen, selected_mon_hoc, selected_hoc_ky) #Lấy danh sách sinh viên theo gv, môn, học kỳ
            self.giang_day = quan_ly_giang_day.lay_giang_day(self.giang_vien.hoTen, selected_mon_hoc, selected_hoc_ky) #Lấy GiangDay theo gv, môn, học kỳ
            
            # Xóa dữ liệu cũ trong listbox_sv
            listbox_sv.delete(0, END)
            listbox_sv_dihoc.delete(0, END)
            
            if self.danh_sach_sinh_vien:
                for sv in self.danh_sach_sinh_vien:
                    listbox_sv.insert(END, sv.hoTen + " - "+ sv.maSV)
            else:
                listbox_sv.insert(END, "(Trống)")


            if self.check_in: 
                for sv in self.check_in.danh_sach_sinh_vien_di_hoc:
                    if sv.diemDanhLuc.strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d"):
                        if sv.monHoc.tenMH == selected_mon_hoc and sv.hocKy == selected_hoc_ky and sv.giangVien.hoTen == self.giang_vien.hoTen:
                            thoi_diem = sv.diemDanhLuc.strftime("%H:%M:%S")
                            listbox_sv_dihoc.insert(END, sv.sinhSien.hoTen + " - " + sv.sinhSien.maSV + " ( at: " + thoi_diem+" )") 
                        else:    
                            listbox_sv_dihoc.insert(END, "(Trống)")
            else:    
                listbox_sv_dihoc.insert(END, "(Trống)")

            # cập nhật thông tin: Tổng, đi học, vắng
            if self.check_in:
                sv_co_mat = []
                for sv in self.check_in.danh_sach_sinh_vien_di_hoc: 
                    if sv.monHoc.tenMH == selected_mon_hoc and sv.hocKy == selected_hoc_ky: 
                        sv_co_mat.append(sv)
                    self.cap_nhat_tong(len(self.danh_sach_sinh_vien), len(sv_co_mat), len(self.danh_sach_sinh_vien) - len(sv_co_mat))
            else: 
                self.cap_nhat_tong(len(self.danh_sach_sinh_vien), 0, len(self.danh_sach_sinh_vien))


                        
        button_loc = Button(group_box2, text="Lọc", command=handle_loc_button_click)
        button_loc.grid(row=4, columnspan=2, padx=10, pady=5)
    #---------------------------------------------------

    #Tạo groupBox thêm sinh viên
        group_box3 = LabelFrame(self.window, text="Thêm dữ liệu")
        group_box3.grid(row=1, column=0, padx=10, pady=10)

        label_mssv = Label(group_box3, text="Mã số sinh viên:")
        label_mssv.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        entry_mssv = Entry(group_box3)
        entry_mssv.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        def handle_them_button_click():
            mssv = entry_mssv.get()

            profile = db.getProfile(mssv)

            if profile is not None:
                result = messagebox.askquestion("Dữ liệu đã tồn tại", "Bạn có muốn cập nhật không?")
                if result == "yes":
                    SV = quan_ly_sv.lay_sinh_vien_theo_mssv(mssv)
                    data = GetData(SV.maSV, SV.hoTen)
                    data.run()

                # Sử dụng lớp TrainingData
                    training_data = TrainingData('dataSet')
                    training_data.train()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Thông báo", "Cập nhật dữ liệu thành công")
            else:
                if quan_ly_sv.kiem_tra_ton_tai(mssv) == True: 
                    SV = quan_ly_sv.lay_sinh_vien_theo_mssv(mssv)

                    data = GetData(SV.maSV, SV.hoTen)
                    data.run()

                # Sử dụng lớp TrainingData
                    training_data = TrainingData('dataSet')
                    training_data.train()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Thông báo", "Thêm dữ liệu thành công")
                else: 
                    messagebox.showerror("Thông báo", "Mã số sinh viên không tồn tại!")

        button_them = Button(group_box3, text="Thêm dữ liệu", command=handle_them_button_click)
        button_them.grid(row=1, columnspan=2, padx=10, pady=5)
    #---------------------------------------------------

        # Thông tin của 1 Môn, lớp, học kì, môn học
        self.cap_nhat_tong(0, 0, 0)


        frame_lists = Frame(self.window)
        frame_lists.grid(row=2, column=0, columnspan=2, pady=10)

        label_ds_sv = Label(frame_lists, text="Danh sách sinh viên:")
        label_ds_sv.grid(row=0, column=0, padx=10)

        label_sv_dihoc = Label(frame_lists, text="Sinh viên đi học:")
        label_sv_dihoc.grid(row=0, column=1, padx=10)

        listbox_sv = Listbox(frame_lists, width=40)  
        listbox_sv.grid(row=1, column=0, padx=10)  
        listbox_sv.insert(END, "(Trống)")   

        listbox_sv_dihoc = Listbox(frame_lists, width=60)  
        listbox_sv_dihoc.grid(row=1, column=1, padx=10)
        listbox_sv_dihoc.insert(END, "(Trống)") 


        #Thêm button Đăng xuất và hàm xử lý
        def handle_dang_xuat_button_click():
            result = messagebox.askquestion("Xác nhận", "Bạn có muốn thoát không?")
            if result == "yes":
                self.window.destroy()  # Đóng form đăng nhập

        button_dang_xuat = Button(self.window, text="Đăng Xuất", bg="red", command=handle_dang_xuat_button_click)
        button_dang_xuat.grid(row=3, column=0, columnspan=2, pady=10)
   

        self.window.mainloop()