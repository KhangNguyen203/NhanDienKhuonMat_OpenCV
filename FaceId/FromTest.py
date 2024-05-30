from tkinter import Tk, Label, Frame
from datetime import datetime

def update_thoi_gian():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label_thoi_gian.config(text=current_time)
    label_thoi_gian.after(1000, update_thoi_gian)

root = Tk()
root.title("Hiển thị thời gian")

frame_container = Frame(root)
frame_container.pack(padx=10, pady=10)

label_thoi_gian = Label(frame_container, text="")
label_thoi_gian.grid(row=0, column=0, padx=10, pady=5)

update_thoi_gian()

root.mainloop()