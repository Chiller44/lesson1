
from tkinter import *
from tkinter import ttk, StringVar

root = Tk()
root.title('IT Step')
root.geometry('400x350')

message = StringVar()
clicks = IntVar(value=0)
name = StringVar()
result = StringVar()

def clicker():
    value = clicks.get()
    clicks.set(value + 1)

def check(*args):
    print(name)
    if name.get() == 'admin':
        result.set('Заборонене імя')
    else:
        result.set("hhh")




label = ttk.Label(textvariable=message)
label.pack(anchor=NW, padx=8, pady=8)

entry = ttk.Entry(textvariable=message)
entry.pack(anchor=NW, padx=8, pady=8)

btn = ttk.Button(textvariable=message)
btn.pack(anchor=NW, padx=8, pady=8)

btn2 = ttk.Button(textvariable=clicks, command=clicker)
btn2.pack(anchor=NW, padx=8, pady=8)

name_entry = ttk.Entry(textvariable=name)
name_entry.pack(anchor=CENTER, expand=1)

check_label = ttk.Label(textvariable=result)
check_label.pack(anchor=CENTER, expand=1)

name.trace_add('write', check)



root.mainloop()
