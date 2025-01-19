from tkinter import *
from tkinter import ttk

root = Tk()
root.title('It step')
root.geometry('305x200')



btn1 = ttk.Button(text='1')
btn1.grid(row=0, column=0)

btn2 = ttk.Button(text='2')
btn2.grid(row=0, column=1)

btn3 = ttk.Button(text='3')
btn3.grid(row=0, column=2)

btn4 = ttk.Button(text='X')
btn4.grid(row=0, column=3)

btn5 = ttk.Button(text='4')
btn5.grid(row=1, column=0)

btn6 = ttk.Button(text='5')
btn6.grid(row=1, column=1)

btn7 = ttk.Button(text='6')
btn7.grid(row=1, column=2)

btn8 = ttk.Button(text='-')
btn8.grid(row=1, column=3)

btn9 = ttk.Button(text='7')
btn9.grid(row=2, column=0)

btn10 = ttk.Button(text='8')
btn10.grid(row=2, column=1)

btn11 = ttk.Button(text='9')
btn11.grid(row=2, column=2)

btn12 = ttk.Button(text='+')
btn12.grid(row=2, column=3)

btn13 = ttk.Button(text='+/-')
btn13.grid(row=3, column=0)

btn14 = ttk.Button(text='0')
btn14.grid(row=3, column=1)

btn15 = ttk.Button(text=',')
btn15.grid(row=3, column=2)

btn16 = ttk.Button(text='=')
btn16.grid(row=3, column=3)

label = ttk.Label(text='Lable', borderwidth=5,relief='', padding=8)
label.grid(row=4, column=0, columnspan=4)




root.mainloop()