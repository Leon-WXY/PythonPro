import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!') \
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('300x300')
    # 设置窗口标题
    top.title('登录窗口')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='知 乎', bg='green', font=('Arial', 12), width=30, height=2)
    label.pack()
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top).pack(side='top')
    username = tkinter.Label(top, text='用户名：', fg='red').place(x=50, y=100)
    inputfiled1 = tkinter.Entry(top, show=None).place(x=100, y=100)
    psw = tkinter.Label(top, text='密 码：', fg='red').place(x=50, y=150)
    inputfiled2 = tkinter.Entry(top, show='*').place(x=100, y=150)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text).place(x=100, y=250)
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit).place(x=200, y=250)
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
