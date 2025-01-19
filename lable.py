from tkinter import *
from tkinter import ttk

root = Tk()
root.title('It step')
root.geometry('500x300')


label = ttk.Label(text='Hello Python', font=('Arrial', 14), borderwidth=5,relief='sun', padding=8)
label.pack()

python_logo = PhotoImage(file='837815.png')
lablePhoto = ttk.Label(image=python_logo, text='Python', compound='left', background="#00FFFF")
lablePhoto.pack()

root.mainloop()