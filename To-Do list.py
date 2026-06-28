from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("600x600")
root.wm_iconbitmap("tick.png")
root.config(bg="black")
root.title("To-Do List")
l1=Label(root,text="*My Tasks*",font="daydream 18 bold",bg="black",fg="white").pack(fill=X)

def save():
    with open("tasks.txt","w") as f:
        tasks=list.get(0,END)
        for task in tasks:
            f.write(task + "\n")
    tmsg.showinfo("to-do list","tasks saved successfully!")
        
def add(event):
    if entry.get() == "":
        print("Enter a task!")
        tmsg.showinfo("to-do list","Enter a task!")
    else:
        print(list.insert(END,entry.get()))
        update_status()

        
def dele(event):
    if entry.get() == "":
        print("Enter a task!")
        tmsg.showinfo("to-do list","Enter a task!")
    else:
        print(list.delete(END))
    update_status()

def clr(event):
    if entry.get() == "":
        print("Enter a task!")
        tmsg.showinfo("to-do list","Enter a task!")
    else:
        tmsg.askyesno("clear","are you sure.?")
        if True:
            list.delete(0,END)
        else:
            print("okayy")
    update_status()

        
def update_status():
    stat.config(text="Tasks:" + str(list.size()))
    
mainmenu=Menu(root)
m1=Menu(mainmenu,tearoff=0)  
m1.add_command(label="save",command=save)
mainmenu.add_cascade(label="File",menu=m1)
root.configure(menu=mainmenu)

statusvar=StringVar()
statusvar.set("Tasks")
stat=Label(root,text="Tasks:0",relief=SUNKEN)
stat.pack(side=BOTTOM,fill=X)
list=Listbox(root)
list.pack(side=BOTTOM,padx=10,pady=60,ipadx=80,ipady=100)
scroll=Scrollbar(list)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=list.yview)
list.config(yscrollcommand=scroll.set)
entry=Entry(root,font="lucida 12 bold",relief=SUNKEN)
entry.pack(pady=20,ipadx=50,ipady=10)
b1=Button(root,text="ADD",font="lucida 12 bold")
b1.pack(side=LEFT,anchor="nw",padx=80,ipadx=30,ipady=10)
b1.bind("<Button-1>",add)
b2=Button(root,text="DEL",font="lucida 12 bold")
b2.pack(side=LEFT,anchor="nw",padx=1,ipadx=30,ipady=10)
b2.bind("<Button-1>",dele)
b3=Button(root,text="CLR",font="lucida 12 bold")
b3.pack(side=LEFT,anchor="nw",padx=40,ipadx=30,ipady=10)
b3.bind("<Button-1>",clr)

root.mainloop()