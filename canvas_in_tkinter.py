from tkinter import *
root=Tk()

canvas=Canvas(root,width=600,height=500,bg="white")
canvas.pack()

line=canvas.create_line(0,0,400,500,fill="red",width=10)
line1=canvas.create_line(50,50,200,200)

# rect=canvas.create_rectangle(200,200,500,400)
# crr1=canvas.create_oval(200,200,500,400,fill='green')
arc=canvas.create_arc(200,200,400,400,fill='yellow',extent=120)
# sq=canvas.create_rectangle(200,200,400,400,fill='blue')
# crr=canvas.create_oval(200,200,400,400,fill='yellow')

points=[200,110,480,200,280,280,200,110]
poly=canvas.create_polygon(points,fill='blue',outline='yellow',width=10)

root.geometry("800x600+200+200")

root.resizable(0,0)
root.mainloop()