from tkinter import *
from tkinter import ttk

root = Tk()
root.title('IT Step')
root.geometry('400x350')

def show_message():
    label['text'] = entry.get()

def clear():
    entry.delete(0, END)


entry = ttk.Entry()
entry.pack(anchor=NW, padx=8, pady=8)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=8, pady=8)

label = ttk.Label(text="test")
label.pack(anchor=NW, padx=8, pady=8)

btn2 = ttk.Button(text='Delete text', command=clear)
btn2.pack(anchor=NW, padx=8, pady=8)


root.mainloop()