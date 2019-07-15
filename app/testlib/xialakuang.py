import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
ttk.Label(win, text="Chooes a number").grid(column=1, row=0) # 添加一个标签0
ttk.Label(win, text="Enter a name:").grid(column=0, row=0) # 设置其在界面中出现的位置
# button被点击之后会被执行
def clickMe():
    action.configure(text='Hello'+name.get()+''+numberChosen.get())
    print('check3 is %d %s' % (chvarEn.get(), type(chvarUn.get())))
action = ttk.Button(win, text="Click Me!", command=clickMe) # 创建一个按钮, text：显示按
action.grid(column=2, row=1)
# 文本框
name = tk.StringVar() # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理

nameEntered = ttk.Entry(win, width=12, textvariable=name) # 创建一个文本框，字符长度为12，
nameEntered.grid(column=0, row=1) # 设置其在界面中出现的位置
nameEntered.focus() # 当程序运行时,光标默认会出现在该文本框中
# 一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100) # 设置下拉列表的值
numberChosen.grid(column=1, row=1) # 设置其在界面中出现的位置 column代表列 row 代表行
numberChosen.current(4) # 设置下拉列表默认显示的值，0为numberChosen['values'] 的下标值
# 复选框
chVarDis = tk.IntVar() # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled') # text为复选框

check1.select() # 该复选框是否勾选,select为勾选, deselect为不勾选
check1.grid(column=0, row=4, sticky=tk.W) # sticky=tk.W 当该列中其他行或该行中的其他列的
chvarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chvarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)
win.mainloop() # 当调用mainloop()时,窗口才会显示出来
