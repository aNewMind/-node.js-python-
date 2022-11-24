#!/user/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
import js2py
import os

# 创建一个主界面
root = Tk()
root.title("node.js转python")
root.geometry("600x500")
lb = Label(root, text='', bg='#87CEEB')
lb.place(x=60, y=5)


# 定义一个处理文件的相关函数
def askfile():
    # 从本地选择一个文件，并返回文件的目录
    dir = tkinter.filedialog.askdirectory()
    if dir != '':
        lb.config(text=dir)
    else:
        lb.config(text='您没有选择任何目录')


btn_ask = Button(root, text='选择node.js编写的系统所在的目录', relief=RAISED, command=askfile)
btn_ask.grid(row=0, column=0)


def btn1_cmd():
    os.mkdir('D:/Desktop/jsToPython')
    file_dir = lb.cget('text')
    file_list=os.listdir(file_dir)
    lt=[]
    for file in file_list:
        if '.js' in file:
            lt.append(file)
    for file in lt:
        py_file=file.replace('.js','.py')
        js2py.translate_file(file_dir+'/'+file,'D:/Desktop/jsToPython/'+py_file)
    messagebox.showinfo('', '转换成功！')


btn1 = Button(root, text='转换', command=btn1_cmd, width=10)
btn1.place(x=200, y=160)
root.mainloop()
