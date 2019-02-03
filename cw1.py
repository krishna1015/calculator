from tkinter import*
a=Tk()
a.config(background='gray')
def click():
    print("clickedddd")
Button(a,text='click',command=click).pack()
a.mainloop()