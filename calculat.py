from tkinter import *
from tkinter import ttk



root = Tk()
root.title('It step')
root.geometry('350x200')

def add_digit(digit):
    value = entry.get() + str(digit)
    entry.delete(0, END)
    entry.insert(0, value)


btn1 = ttk.Button(text='1', command=lambda : add_digit(1))
btn1.grid(row=1, column=0, padx=5, pady=5)

btn2 = ttk.Button(text='2', command=lambda : add_digit(2))
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = ttk.Button(text='3', command=lambda : add_digit(3))
btn3.grid(row=1, column=2, padx=5, pady=5)

btn4 = ttk.Button(text='X', command=lambda : add_digit('x'))
btn4.grid(row=1, column=3, padx=5, pady=5)

btn5 = ttk.Button(text='4', command=lambda : add_digit(4))
btn5.grid(row=2, column=0, padx=5, pady=5)

btn6 = ttk.Button(text='5', command=lambda : add_digit(5))
btn6.grid(row=2, column=1, padx=5, pady=5)

btn7 = ttk.Button(text='6', command=lambda : add_digit(6))
btn7.grid(row=2, column=2, padx=5, pady=5)

btn8 = ttk.Button(text='-', command=lambda : add_digit('-'))
btn8.grid(row=2, column=3, padx=5, pady=5)

btn9 = ttk.Button(text='7', command=lambda : add_digit(7))
btn9.grid(row=3, column=0, padx=5, pady=5)

btn10 = ttk.Button(text='8', command=lambda : add_digit(8))
btn10.grid(row=3, column=1, padx=5, pady=5)

btn11 = ttk.Button(text='9', command=lambda : add_digit(9))
btn11.grid(row=3, column=2, padx=5, pady=5)

btn12 = ttk.Button(text='+', command=lambda : add_digit('+'))
btn12.grid(row=3, column=3, padx=5, pady=5)

btn13 = ttk.Button(text='+/-', command=lambda : add_digit('+/-'))
btn13.grid(row=4, column=0, padx=5, pady=5)

btn14 = ttk.Button(text='0', command=lambda : add_digit(0))
btn14.grid(row=4, column=1, padx=5, pady=5)

btn15 = ttk.Button(text=',', command=lambda : add_digit(','))
btn15.grid(row=4, column=2, padx=5, pady=5)

btn16 = ttk.Button(text='=')
btn16.grid(row=4, column=3, padx=5, pady=5)

entry = ttk.Entry(justify='right', font=('Arrial', 15), width=15)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, stick='we')







root.mainloop()