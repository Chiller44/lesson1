from tkinter import *
from tkinter import ttk

root = Tk()
root.title('It step')
root.geometry('500x300')

def show_mess():
    label['text'] = entry.get()

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn=ttk.Button(text="Click me", command=show_mess)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)




root.mainloop()