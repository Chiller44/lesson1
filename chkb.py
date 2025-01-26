from tkinter import *
from tkinter import ttk, StringVar



root = Tk()
root.title('IT Step')
root.geometry('400x350')

def select():
    result = "Вибрано"
    if python.get() == 1: result = f'{result} Python'
    if javascrypt.get() == 1: result = f'{result} Javascrypt'
    if java.get() == 1: result = f'{result} Java'
    languages.set(result)


position = {'padx':6, 'pady':6, 'anchor':NW}

languages= StringVar()

languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

python = IntVar()
python_checkbutton = ttk.Checkbutton(text='Python', variable='python', command=select)
python_checkbutton.pack(**position)

javascrypt = IntVar()
javascrypt_checkbutton = ttk.Checkbutton(text='javascrypt', variable='javascrypt', command=select)
javascrypt_checkbutton.pack(**position)

java = IntVar()
java_checkbutton = ttk.Checkbutton(text='javas', variable='java', command=select)
java_checkbutton.pack(**position)

root.mainloop()
