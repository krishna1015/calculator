from tkinter import *
cal=Tk()
cal.geometry("500x500")
cal.title("SIMPLE CALCULATOR")

cal.config(background='yellow')
label=Label(text='SIMPLE CALCULATOR').grid(row=0,column=0)
res=Label(cal,font=("",30),bg="powder blue",text="ouptut")
res.grid(row=1,column=2)

Label(cal,text="Enter first number:",fg='red',background='black').grid(row=3,column=0)
first=StringVar()
name1=Entry(cal,textvariable=first).grid(row=3,column=1)

Label(cal,text="Enter second number:",fg='red',background='black').grid(row=4,column=0)
second=StringVar()
name2=Entry(cal,textvariable=second).grid(row=4,column=1)

add=Button(cal,text="+",command=lambda:res.config(text="output"+str(int(first.get())+int(second.get()))))
add.grid(row=5,column=1)
sub=Button(cal,text="-",command=lambda:res.config(text="output"+str(int(first.get())-int(second.get()))))
sub.grid(row=6,column=1)
mul=Button(cal,text="*",command=lambda:res.config(text="output"+str(int(first.get())*int(second.get()))))
mul.grid(row=7,column=1)
div=Button(cal,text="/",command=lambda:res.config(text="output"+str(int(first.get())/int(second.get()))))
div.grid(row=8,column=1)

def show_details():
    pass

cal.mainloop()