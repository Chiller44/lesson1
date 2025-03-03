from tkinter import *
from tkinter import ttk



root = Tk()
root.title('Spinbox')
root.geometry('500x500')

def change():
    label['text'] = spinbox.get()

sb_var = StringVar(value=22)

label = ttk.Label()
label.pack(anchor=N)


spinbox = ttk.Spinbox(from_=0, to=100.0, increment=1.0, state='readonly', textvariable=sb_var, command=change)
spinbox.pack(anchor=NW)

root.mainloop()