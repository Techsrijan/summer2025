from tkinter import *
from tkinter import filedialog,messagebox,colorchooser
import win32api
root=Tk()
def back_color():
    c=colorchooser.askcolor()
    t.config(background=c[1])

    print(c)

def fore_color():
    c = colorchooser.askcolor()
    t.config(foreground=c[1])
def new_print():
    # for default printer
    # printer_name=win32print.GetDefaultPrinter()
    # lbl.config(text=printer_name)
    print_file_name = filedialog.askopenfilename(initialdir="/", title="Open File",
                                                 filetypes=(("Text FILE", "*.txt"), ("All FILE", "*.*")))
    if print_file_name:
        win32api.ShellExecute(0, "print", print_file_name, None, ".", 0)
def get_text_data():
    print(t.get(1.0,END))

def open_file():
    global current_open_file
    current_open_file = ''
    f=filedialog.askopenfile(initialdir="/",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    print(f)
    current_open_file=f
    for data in f:
        # print(data)
        t.insert(END, data)

def save_file():
    if current_open_file=='':
        saveas_file()
    else:
        g=open(current_open_file.name,'a')
        matter=t.get(1.0, END)
        g.write(matter)


def saveas_file():
    fs=filedialog.asksaveasfile(title="Save File", mode="w",
                                defaultextension='.txt')
    data=t.get(1.0,END)
    fs.write(data)

def new_file():
    x=t.get(1.0, END)
    if x:
        pass
    else:
        res=messagebox.askyesnocancel('Save File Confirmation','Do you want to save this file?')
        print(res)
        if res==True:
            saveas_file()
            t.delete(1.0, END)
        elif res==False:
            t.delete(1.0,END)

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


btn_save=Button(root,text="Save file", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=save_file)
btn_save.pack()

btn_saveas=Button(root,text="Save As file", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=saveas_file)
btn_saveas.pack()

btn_new=Button(root,text="New", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=new_file)
btn_new.pack()

btn_print=Button(root,text="Print", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=new_print)
btn_print.pack()


btn_change_color=Button(root,text="Color", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=back_color)
btn_change_color.pack()

btn_change_fore_color=Button(root,text=" fore Color", fg="red",bg="yellow",
           font=("comic sans ms",15,'bold'),
           command=fore_color)
btn_change_fore_color.pack()
root.geometry("600x800+500+200")

root.mainloop()