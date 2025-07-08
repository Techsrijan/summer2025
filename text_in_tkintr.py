from tkinter import *
from tkinter import filedialog

root=Tk()
def get_text_data():
    print(t.get(1.0,END))

def open_file():
    f=filedialog.askopenfile(initialdir="/",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    print(f)
    for data in f:
        # print(data)
        t.insert(END, data)
t=Text(root,height=15,padx=10,pady=10,width=15,wrap=WORD,selectbackground='red')
# t.pack(fill=BOTH,expand=1)
# t.insert(END,'HOW are you what are you')
# t.insert(END,'HOW are you')
t.pack()
btn=Button(root,text="get_text_data", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=get_text_data)
btn.pack()
btn1=Button(root,text="open file", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=open_file)
btn1.pack()
root.geometry("600x500+500+200")

root.mainloop()