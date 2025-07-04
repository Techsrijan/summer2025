from tkinter import *

def add():
    #print(x.get())
    a=int(x.get())
    b=int(y.get())
    c=a+b
    result.set(c)


def sub():
    a = int(x.get())
    b = int(y.get())
    c = a - b
    result.set(c)

def mul():
    a = int(x.get())
    b = int(y.get())
    c = a * b
    result.set(c)

def div():
    a = int(x.get())
    b = int(y.get())
    c = a % b
    result.set(c)

def clear():
    x.set('')
    y.set('')
root=Tk()
root.title("My first window")
# btn=Button(root,text="click me", fg="red",bg="yellow",
#            font=("comic sans ms",15,'bold'),
#            command=msg)
# # btn.pack(side=TOP,fill=X)
# btn.place(x=100,y=50)
lbl=Label(root,text="Enter first Number",fg="red",bg="yellow",
            font=("comic sans ms",15,'bold'))
lbl.place(x=10,y=50)

lbl=Label(root,text="Enter Second Number",fg="red",bg="yellow",
            font=("comic sans ms",15,'bold'))
lbl.place(x=10,y=100)

#x=IntVar()
x=StringVar()
txt=Entry(root,justify='right',fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=x)
txt.place(x=300,y=50)

y=StringVar()
txt1=Entry(root,justify='right',fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=y)
txt1.place(x=300,y=100)


btn=Button(root,text="ADD", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=add)
btn.place(x=120,y=200)

btn1=Button(root,text="Sub", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=sub)
btn1.place(x=230,y=200)


btn2=Button(root,text="MUL", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=mul)
btn2.place(x=330,y=200)


btn3=Button(root,text="DIV", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=div)
btn3.place(x=450,y=200)


btn4=Button(root,text="clear", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=clear)

btn4.place(x=270,y=300)
# result=IntVar()
result=StringVar()
lbl1=Label(root,fg="red",
            font=("comic sans ms",15,'bold'),textvariable=result)
lbl1.place(x=150,y=350)
root.geometry("650x600+500+200")
root.resizable(0,0)
#root.wm_iconbitmap('cal.ico')
root.mainloop()