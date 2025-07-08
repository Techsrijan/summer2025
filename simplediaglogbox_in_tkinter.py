from tkinter import *
from tkinter import simpledialog
root=Tk()
def get_dialogbox():
    sum=0
    for i in range(5):
        a=simpledialog.askinteger('Marks Input','Enter Student Marks')
        sum=sum+a
    print(sum)

btn=Button(root,text="ADD", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=get_dialogbox)
btn.pack()
root.geometry("600x225+500+200")
root.resizable(0,0)
#root.wm_iconbitmap('cal.ico')
root.mainloop()