from tkinter import *

def left_click(event):
    print("left button is clciked")
def middle_click(event):
    print("middle button is clciked")

def right_click(event):
    print("right button is clciked")
root=Tk()
root.title("My first window")
btn=Button(root,text="Left click", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           )
btn.pack()

btn1=Button(root,text="Middle Click", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           )
btn1.pack()
btn12=Button(root,text="Right Click", fg="red",bg="yellow",
           font=("comic sans ms",25,'bold'),
           )
btn12.pack()

btn.bind("<Button-1>",left_click)
btn12.bind("<Button-3>",right_click)
btn1.bind("<Button-2>",middle_click)

root.bind("<Control-l>",left_click)
root.bind("<Control-r>",right_click)
root.bind("<Control-m>",middle_click)


root.geometry("400x400+500+200")
root.resizable(0,0)
root.wm_iconbitmap('cal.ico')
root.mainloop()
