from tkinter import *
from tkinter import ttk

root = Tk()
root.title('IT Step')
root.geometry('400x350')

enable = IntVar()
enable2 = StringVar()

def checkbutton_changed():
    showinfo(title='info', message=enable2.get())



enabled_checkbutton = ttk.Checkbutton(text="Swich on", variable=enable2, offvalue=)
enabled_checkbutton.pack(anchor=NW, padx=6, pady=6)

enabled_label = ttk.Label(variable=enable)
enabled_label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()