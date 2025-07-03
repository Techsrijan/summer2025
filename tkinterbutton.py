from tkinter import *

def msg():
    print("hello")
def msg2():
    print("hi")
root=Tk()
root.title("My first window")
btn=Button(root,text="click me", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           command=msg)
btn.pack(side=TOP,fill=X)

btn1=Button(root,text="Add", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           command=msg2)
btn1.pack(side=LEFT,fill=Y)
btn12=Button(root,text="sub", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           command=msg2)
btn12.pack(side=RIGHT)
btn123=Button(root,text="mul", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           command=msg2)
btn123.pack(side=BOTTOM)

root.geometry("400x400+500+200")
root.resizable(0,0)
root.wm_iconbitmap('cal.ico')
root.mainloop()
