from tkinter import *
cal=Tk()

Label(cal,text="Name:",fg='red',background='black').grid(row=0,column=0)
uname=StringVar()
name=Entry(cal,textvariable=uname).grid(row=0,column=1)

Label(cal,text="Age:",fg='red',background='black').grid(row=1,column=0)
uage=StringVar()
age=Entry(cal,textvariable=uage).grid(row=1,column=1)

Label(cal,text="College:",fg='red',background='black').grid(row=2,column=0)
ucollege=StringVar()
college=Entry(cal,textvariable=ucollege).grid(row=2,column=1)
def show_details():
    toplevel=Toplevel(cal)
    Label(toplevel,text=uname.get(),font=("",20)).grid()
    Label(toplevel, text=uage.get(), font=("", 20)).grid()
    Label(toplevel, text=ucollege.get(), font=("",20)).grid()
button=Button(cal,text="SUBMIT",fg='teal',background='black',font=("",20),command=show_details)
button.grid(padx=10,pady=10)
cal.config(background="gray")
cal.mainloop()