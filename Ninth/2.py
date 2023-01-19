from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Enter Personal Details")
def confirm():
    messagebox.showinfo("Successfull","Information Submitted")
    root1=Tk()
    root1.title("Data Entered Successfully")
    lb1=Label(root1,text="PERSONAL DETAILS")
    lb1.grid(row=0,column=0)
    lb2=Label(root1,text="Name: %s %s"%(e1.get(),e2.get()))
    lb2.grid(row=1,column=0)
    if(v3.get()=="Male"):
        lb3=Label(root1,text="Gender: %s"%v3.get())
        lb3.grid(row=2,column=0)
    else:
        lb3=Label(root1,text="Gender: %s"%v4.get())
        lb3.grid(row=2,column=0)
    l4=Label(root1,text="Age: %s"%int(v5.get()))
    l4.grid(row=3,column=0)
    if(v6.get()==1):
        l5=Label(root1,text="Course: %s"%c1.cget("text"))
        l5.grid(row=4,column=0)
    elif(v7.get()==1):
        l5=Label(root1,text="Course: %s"%c2.cget("text"))
        l5.grid(row=4,column=0)
    elif(v8.get()==1):
        l5=Label(root1,text="Course: %s"%c3.cget("text"))
        l5.grid(row=4,column=0)
    elif(v9.get()==1):
        l5=Label(root1,text="Course: %s"%c4.cget("text"))
        l5.grid(row=4,column=0)
    else:
        l5=Label(root1,text="Course: %s"%c5.cget("text"))
        l5.grid(row=4,column=0)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    l1=[v3,v4,v5,v6,v7,v8,v9,v10]
    for i in l1:
        i.set(0)
def onlymale():
    v4.set(0)
def onlyfemale():
    v3.set(0)
def onlyit():
    l1=[v7,v8,v9,v10]
    for i in l1:
        i.set(0)
def onlybt():
    l1=[v6,v8,v9,v10]
    for i in l1:
        i.set(0)
def onlyms():
    l1=[v6,v7,v9,v10]
    for i in l1:
        i.set(0)
def onlyaf():
    l1=[v6,v7,v8,v10]
    for i in l1:
        i.set(0)
def onlybi():
    l1=[v6,v7,v8,v9]
    for i in l1:
        i.set(0)
l1=Label(root,text="FirstName:")
l1.grid(row=0,column=0)
l2=Label(root,text="LastName:")
l2.grid(row=1,column=0)
v1=StringVar()
v2=StringVar()
e1=Entry(root,textvariable=v1)
e1.grid(row=0,column=1)
e2=Entry(root,textvariable=v2)
e2.grid(row=1,column=1)
l3=Label(root,text="Gender:")
l3.grid(row=2,column=0)
v3=StringVar()
v4=StringVar()
r1=Radiobutton(root,text="Male",variable=v3,value="Male",command=onlymale)
r1.grid(row=2,column=1)
v3.set(0)
r2=Radiobutton(root,text="Female",variable=v4,value="Female",command=onlyfemale)
r2.grid(row=2,column=2)
v4.set(0)
v5=DoubleVar()
s1=Scale(root,variable=v5,orient=HORIZONTAL,from_=0,to=30,troughcolor="blue",label="Age:")
s1.grid(row=3,column=0)
l4=Label(root,text="Courses:")
l4.grid(row=4,column=0)
v6=IntVar()
c1=Checkbutton(root,text="BSC-IT",variable=v6,command=onlyit)
c1.grid(row=5,column=0)
v7=IntVar()
c2=Checkbutton(root,text="BSC-BT",variable=v7,command=onlybt)
c2.grid(row=6,column=0)
v8=IntVar()
c3=Checkbutton(root,text="BCOM-MS",variable=v8,command=onlyms)
c3.grid(row=7,column=0)
v9=IntVar()
c4=Checkbutton(root,text="BCOM-AF",variable=v9,command=onlyaf)
c4.grid(row=8,column=0)
v10=IntVar()
c5=Checkbutton(root,text="BCOM-BI",variable=v10,command=onlybi)
c5.grid(row=9,column=0)
b1=Button(root,text="Confirm",command=confirm)
b1.grid(row=10,column=0)
b2=Button(root,text="Clear",command=clear)
b2.grid(row=10,column=1)
root.mainloop()