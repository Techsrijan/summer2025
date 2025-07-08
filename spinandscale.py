from tkinter import *
root=Tk()
def get_data():
    print(s.get())
    print(sc.get())
s=Spinbox(root,from_=1,to=5)
s.pack()
btn=Button(root,text="ADD", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=get_data)

sc=Scale(root,from_=200,to=400,sliderlength=40,
         length=200,width=30,orient=HORIZONTAL)
sc.set(300)
sc.pack()

btn.pack()
root.geometry("600x225+500+200")
root.resizable(0,0)
#root.wm_iconbitmap('cal.ico')
root.mainloop()