from tkinter import *
print('cmd 2.1.0 system')

while 1:
    a=input('C:\doubi>')
    if a=='pip install doubi':
        print(''' Collecting doubi.
        |████████████████████████████████|12kb/12kb
        doubi done.
You are using cmd 2.1.0.However,vision2.1.1is available.''')
    elif a=='shutdown':
        r=Tk('300x30')
        l1=Label(r,text='Windows将在10秒后关闭。')
        l1.pack()
        b1=Button(r,text='确定')
        b1.pack()

    else:
        print('哈哈哈，你上当了！🤪🤪🤪')
