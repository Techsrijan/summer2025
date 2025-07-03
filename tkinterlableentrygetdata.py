from tkinter import *

def get_text_data():
    #print(x.get())
    result.set(x.get())
    x.set('')



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

#x=IntVar()
x=StringVar()
txt=Entry(root,justify='right',fg='red',border='10',font=("comic sans ms",15,'bold'),textvariable=x)
txt.place(x=300,y=50)

btn=Button(root,text="GET TEXT DATA", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=get_text_data)

btn.place(x=150,y=150)
# result=IntVar()
result=StringVar()
lbl1=Label(root,fg="red",
            font=("comic sans ms",15,'bold'),textvariable=result)
lbl1.place(x=150,y=350)
root.geometry("650x600+500+200")
root.resizable(0,0)
root.wm_iconbitmap('cal.ico')
root.mainloop()
