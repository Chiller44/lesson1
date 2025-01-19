from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Просте вікно')
root.geometry('500x250')


label1 = ttk.Label(text='Enter login')
label1.pack(pady=3)

entry1 = ttk.Entry(justify=CENTER)
entry1.pack(pady=3)

label2 = ttk.Label(text='Enter password')
label2.pack(pady=3)

entry2 = ttk.Entry(justify=CENTER)
entry2.pack(pady=3)

btn1 = ttk.Button(text="ENTER")
btn1.pack(pady=40)





root.mainloop()

