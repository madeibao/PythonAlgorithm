
from tkinter import *

from tkinter import messagebox

 

#点击关闭按钮，触发弹出消息

def closeWindow():

    messagebox.showinfo(title='warning',message='不许关闭，再考虑考虑')

    return

 

 

#点击喜欢按钮后弹出的love子窗口中，点击当前的关闭时，所呈现的结果

def closelove():

    messagebox.showinfo(title="不再考虑一下吗？", message="Think about it more")

    return

#点击喜欢按钮后弹出的love子窗口中，点击确定时关闭所有当前窗口

def closeallwindow():

    #销毁所有窗口

    window.destroy()

#点击主窗口中的确定所呈现出来的

def Love():

    #下面是在window下的一个顶级子窗口

    love=Toplevel(window)

    love.title('好巧，我也是')

    love.geometry('300x100+630+240')

    label = Label(love, text="好巧，我也是", font=('微软雅黑',15))

    label.pack()

    label3 = Label(love, text="那留给微信吧", font=('微软雅黑', 10))

    label3.pack()

    entry=Entry(love,font=('微软雅黑',10))

    btn=Button(love,text='Yes',width=18,height=2,command=closeallwindow)

    btn.pack()

    love.protocol('WM_DELETE_WINDOW',closelove)

 

#在主窗口点击不喜欢时，对于所弹出的nolove窗口，点击关闭时弹出

def closenolove():

    nolove()

 

#在主窗口点击不喜欢时，所弹出的nolove窗口

def nolove():

    no_love=Toplevel(window)

    no_love.geometry('300x100+630+240')

    no_love.title('再考虑考虑呗')

    label=Label(no_love, text='再考虑考虑呗', font=('微软雅黑',15))

    label.pack()

    btn=Button(no_love,text='好的',width=18,height=2,command=no_love.destroy)

    btn.pack()

    no_love.protocol('WM_DELETE_WINDOW',closenolove)

 

 

#创建窗口

window=Tk()

#创建窗口标题

window.title('Are you love me?')

#创建窗口大小

window.geometry('380x420+590+240')

 

#当用户点击关闭时，触发这个方法

window.protocol('WM_DELETE_WINDOW',closeWindow)

 

#标签控件

label1=Label(window,text='hey,小姐姐',font=('微软雅黑',15),fg='red')

#标签定位，根据网格布局使用grid(),还可以使用pack(),place

label1.grid()  ##grid()里的默认值是row=0,column=0,sticky=W

label2=Label(window,text='Are you love me?',font=('微软雅黑',20))

label2.grid(row=1,column=1,sticky=E)

 

#显示图片

photo=PhotoImage(file='./love1.png')

imagelabel=Label(window,image=photo)

#cloumnspan表示组件所要跨越的列数

imagelabel.grid(row=2,columnspan=2)

 

#按钮

btn1=Button (window,text='Yes',width=18,height=2,command=Love)

btn1.grid(row=3,column=0,sticky=W)

btn2=Button(window,text='No',command=nolove)

btn2.grid(row=3,column=1,sticky=E)

 

window.mainloop()
