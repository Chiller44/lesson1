from tkinter import *
from tkinter import ttk

from chkb import languages


def delete():
    selection = lang_listbox.curselection()
    lang_listbox.delete(selection[0])

def add():
    new_language = language_entry.get()
    lang_listbox.insert(0, new_language)


def delete_all():
    lang_listbox.delete(0, END)


root = Tk()
root.title('IT Step')
root.geometry('400x350')

root.columnconfigure(index=0, weight=4)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)

language_entry = ttk.Entry()
language_entry.grid(column=0, row=0, padx=6,pady=6, sticky=NW)
ttk.Button(text='Add', command=add).grid(column=1, row=0)

lang_listbox = Listbox()
lang_listbox.grid(column=0, row=1, padx=5, pady=5, sticky=EW, columnspan=2)


lang_listbox.insert(END, 'Python', 'C+')

ttk.Button(text='Delete', command=delete).grid(column=1, row=2, padx=5, pady=5)

ttk.Button(text='Delete all', command=delete_all).grid(column=0, row=2, padx=5, pady=5)








root.mainloop()