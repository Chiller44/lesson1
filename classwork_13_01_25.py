from tkinter import *
from tkinter import ttk

root = Tk()
root.title('It step')
root.geometry('250x250')

for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)

btn1 = ttk.Button(text='button 1')
btn1.grid(row=0, column=0, columnspan=2, ipadx=70, padx=6, pady=6)

btn2 = ttk.Button(text='button 2')
btn2.grid(row=1, column=0, ipadx=5, padx=6, pady=6)

btn3 = ttk.Button(text='button 3')
btn3.grid(row=1, column=1, ipadx=5, padx=6, pady=6)

btn4 = ttk.Button(text='button 4')
btn4.grid(row=2, column=1, rowspan=2, ipadx=5, ipady=40, padx=6, pady=6)

btn5 = ttk.Button(text='button 5')
btn5.grid(row=2, column=0, ipadx=5, padx=6, pady=6)

btn6 = ttk.Button(text='button 6')
btn6.grid(row=3, column=0, ipadx=5, padx=6, pady=6)

root.mainloop()