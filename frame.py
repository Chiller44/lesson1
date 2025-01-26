from tkinter import *
from tkinter import ttk, StringVar

def creare_framme(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)

    entry = ttk.Entry(frame)
    entry.pack(anchor=NW)
    return frame


root = Tk()
root.title('IT Step')
root.geometry('400x350')

name_frame = creare_framme('ВВедіть імя')
name_frame.pack()

#frame1 = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
#name_label = ttk.Label(frame1, text='Enter name')
#name_label.pack(anchor=NW)

#btn1 = ttk.Button(frame1)
#btn1.pack()

#frame1.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()