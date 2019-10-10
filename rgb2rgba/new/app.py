from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Frame, Label, Entry, Button, Radiobutton
from tkinter import StringVar, BooleanVar, IntVar
from tkinter import LEFT, TOP, X, W, E

from rgb2rgba import run

def select_path():
    _path = filedialog.askopenfilename()
    path.set(_path)

def do_it():
    img_path = path.get()
    low_hsv = [low_h.get(), low_s.get(), low_v.get()]
    high_hsv = [high_h.get(), high_s.get(), high_v.get()]
    img_show = show.get()
    done = run(img_path, low_hsv, high_hsv, img_show)
    if done == 'done':
        messagebox.showinfo(title='Done', message='Done!')
    else:
        messagebox.showerror(title='Error', message=done)
    pass

window = Tk()
window.title('Convert RGB to RGBA')
window.geometry('300x300')


path = StringVar()
label_1 = Label(window, text='源图片路径：').grid(row=0, column=0)
entry_1 = Entry(window, textvariable=path).grid(row=0, column=1)
button_1 = Button(window, text='选择文件', 
    command=select_path).grid(row=0, column=2)


label_2 = Label(window, text='HSV最小值：').grid(row=1, column=0)
label_6 = Label(window, text='HSV最大值：').grid(row=5, column=0)


label_3 = Label(window, text='H：').grid(row=2, column=0)
label_4 = Label(window, text='S：').grid(row=3, column=0)
label_5 = Label(window, text='V：').grid(row=4, column=0)


low_h, low_s, low_v = IntVar(), IntVar(), IntVar()
entry_2 = Entry(window, textvariable=low_h).grid(row=2, column=1)
entry_3 = Entry(window, textvariable=low_s).grid(row=3, column=1)
entry_4 = Entry(window, textvariable=low_v).grid(row=4, column=1)


label_7 = Label(window, text='H：').grid(row=6, column=0)
label_8 = Label(window, text='S：').grid(row=7, column=0)
label_9 = Label(window, text='V：').grid(row=8, column=0)


high_h, high_s, high_v = IntVar(), IntVar(), IntVar()
entry_5 = Entry(window, textvariable=high_h).grid(row=6, column=1)
entry_6 = Entry(window, textvariable=high_s).grid(row=7, column=1)
entry_7 = Entry(window, textvariable=high_v).grid(row=8, column=1)

show = BooleanVar()
label_10 = Label(window, text='显示图片：').grid(row=9, column=0)
radiobutton_1 = Radiobutton(window, text='是', 
    variable=show, value=1).grid(row=9, column=1, sticky=W)
radiobutton_2 = Radiobutton(window, text='否', 
    variable=show, value=0).grid(row=9, column=1, sticky=E)

button_3 = Button(window, text='运行', command=do_it, width=10, bd=3).grid(row=10, column=1)


window.mainloop()