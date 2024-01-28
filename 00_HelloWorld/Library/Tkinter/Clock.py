import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title('Đồng hồ nhà Haru')

label = tk.Label(root, font=('Courier New', 40, 'bold'), background='violet', foreground='white')
label.pack(anchor='center')

time()
root.mainloop()
