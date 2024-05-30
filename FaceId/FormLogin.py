from tkinter import *
from FormCheckIn import DiemDanh
from tkinter import messagebox
from AvailableData import quan_ly_gv


class DangNhap:
    def __init__(self):
        self.window = Tk()
        self.window.title("Đăng nhập")

        window_width = 400
        window_height = 200

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Tạo nhãn và ô văn bản cho tên đăng nhập
        label_username = Label(self.window, text="Mã giảng viên:")
        label_username.pack()
        self.entry_username = Entry(self.window)
        self.entry_username.pack()

        # Tạo nhãn và ô văn bản cho mật khẩu
        label_password = Label(self.window, text="Mật khẩu:")
        label_password.pack()
        self.entry_password = Entry(self.window, show="*")  # show="*" để ẩn mật khẩu
        self.entry_password.pack()

        # Tạo nút đăng nhập
        btn_login = Button(self.window, text="Đăng nhập", command=self.login)
        btn_login.pack()

        self.window.mainloop()

    def login(self):
        username = self.entry_username.get()  # Lấy giá trị từ ô văn bản tên đăng nhập
        password = self.entry_password.get()  # Lấy giá trị từ ô văn bản mật khẩu

        giang_vien = quan_ly_gv.dang_nhap(username, password)

        if giang_vien is not None:
            self.window.destroy()  # Đóng form đăng nhập
            diem_danh = DiemDanh(giang_vien)  # Truyền đối tượng giảng viên vào khi khởi tạo đối tượng DiemDanh
        else:
            messagebox.showerror("Thông báo", "Thông tin đăng nhập không chính xác.")

# Tạo đối tượng từ lớp DangNhap
dang_nhap = DangNhap()