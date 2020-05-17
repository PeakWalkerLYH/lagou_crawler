#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import ImageTk, Image
from tkinter import *
import lagouwang
import threading
import tkinter.messagebox


def run():
    count = [1]

    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()
        
    def crawler():
        position_name = position.get()
        start_page = page_start.get()
        end_page = page_end.get()

        if position_name == '':
            tkinter.messagebox.showerror('警告', '职位不能为空！')
            return

        if end_page == '':
            tkinter.messagebox.showerror('警告', '终止页不能为空')
            return

        if start_page == '':
            start_page = 1
            page_start.insert(0, '1')

        start_page = int(start_page)
        end_page = int(end_page)

        if (start_page <= 0) | (end_page <= 0):
            tkinter.messagebox.showerror('警告', '页数必须大于0！')
            return

        if end_page < start_page:
            tkinter.messagebox.showerror('警告', '起始页必须小于等于终止页！')
            return

        lagouwang.main(position_name, start_page, end_page, count[0])
        count[0] += 1

        number = end_page - start_page + 1
        size = number * 15
        print(f'爬取完毕！\n一共{number}页，包含{size}条数据')
        tkinter.messagebox.showinfo('提示', f'爬取完毕！\n一共{number}页，包含{size}条数据')

    root = Tk()
    root.title('拉勾网数据爬取')
    root.geometry('640x600+320+60')
    root.resizable(width=False, height=False)
    root.iconbitmap('./image/logo.ico')

    fm0 = Frame(root)
    fm0.pack(side='top')
    photo = PhotoImage(file='./image/timg.gif')
    imageLabel = Label(fm0, image=photo, height=250, width=640)
    imageLabel.pack()

    # 第一个容器
    fm1 = Frame(root)
    fm1.pack(side='top', pady=30)
    # 职位
    position_label = Label(fm1, text='请输入职位：', font=('KaiTi', 15, 'bold'))
    position_label.pack(side='left')
    # position_label['height'] = 10

    position = Entry(fm1, width=45, highlightcolor='green', highlightthickness=2)
    position.pack(side='left', pady=10)

    # 第二个容器
    fm2 = Frame(root)
    fm2.pack(side='top')
    # 起始页码
    page_start_label = Label(fm2, text='请输入页码：', font=('KaiTi', 15, 'bold'))
    page_start_label.pack(side='left')

    page_start_label = Label(fm2, text='起始：', font=('KaiTi', 10, 'bold'))
    page_start_label.pack(side='left')

    page_start = Entry(fm2, width=15, highlightcolor='green', highlightthickness=2)
    page_start.pack(side='left')

    # 终止页码
    page_end_label = Label(fm2, text='终止：', font=('KaiTi', 10, 'bold'))
    page_end_label.pack(side='left')

    page_end = Entry(fm2, width=15, highlightcolor='green', highlightthickness=2)
    page_end.pack(side='left')

    # 第三个容器
    fm3 = Frame(root)
    fm3.pack(side='top', pady=40)
    # 开始按钮
    start = Button(fm3, text='开始爬取', font=('KaiTi', 15, 'bold'), bg='green', fg='pink', bd=2, width=10, command=lambda: thread_it(crawler))
    start.pack(side='left', padx=40)


    # 结束按钮
    end = Button(fm3, text='关闭程序', font=('KaiTi', 15, 'bold'), bg='green', fg='pink', bd=2, width=10, command=root.quit)
    end.pack(side='right', padx=40)

    root.mainloop()


if __name__ == "__main__":
    run()
