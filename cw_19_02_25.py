from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Combobox')
root.geometry('500x500')

def selected(event):
    selection = combox.get()
    print(selection)
    label['text'] = f'u pick: {selection}'

languages = ['Python', 'GO', 'C++', 'C#', 'JavaScript']


label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6, fill=X)

combox = ttk.Combobox(values=languages, state='readonly')
combox.pack(anchor=NW, padx=6, pady=6)
combox.bind('<<ComboboxSelected>>', selected)




print(combox.get())
root.mainloop()