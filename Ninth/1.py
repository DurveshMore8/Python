from tkinter import *
from tkinter import messagebox

def show():
    messagebox.showinfo("Python","Fonts Configured")
root=Tk()
root.title("GUI in Python")
l1=Label(root,text="Hello Python Programming",font=("Monotype Corsiva",30),fg="blue",bg="red")
l1.pack()
b1=Button(root,text="Click Here",font=("Adorable",15),fg="yellow",bg="purple",command=show)
b1.pack()
root.mainloop()