from tkinter import *

def add():
    #print(x.get())
    a=int(x.get())
    b=int(y.get())
    c=a+b
    result.set(c)




def clear():
    x.set('')
    y.set('')
root=Tk()
root.title("My first window")

lbl=Label(root,text="Enter first Number",fg="red",bg="yellow",
            font=("comic sans ms",15,'bold'))
lbl.grid(row=0,column=0)

lbl=Label(root,text="Enter Second Number",fg="red",bg="yellow",
            font=("comic sans ms",15,'bold'))
lbl.grid(row=1,column=0)

#x=IntVar()
x=StringVar()
txt=Entry(root,justify='right',fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=x)
txt.grid(row=0,column=1)

y=StringVar()
txt1=Entry(root,justify='right',fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=y)
txt1.grid(row=1,column=1)


btn=Button(root,text="ADD", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=add)
btn.grid(row=2,column=0,columnspan=2)



btn4=Button(root,text="clear", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=clear)

btn4.grid(row=3,column=0)
# result=IntVar()
result=StringVar()
lbl1=Label(root,fg="red",
            font=("comic sans ms",15,'bold'),textvariable=result)
lbl1.grid(row=3,column=1)
root.geometry("600x225+500+200")
root.resizable(0,0)
#root.wm_iconbitmap('cal.ico')
root.mainloop()