from tkinter import *
from tkinter import ttk, StringVar

from chkb import javascrypt

root = Tk()
root.title('IT Step')
root.geometry('400x350')

position = {'padx': 6, 'pady':6, 'anchor':NW}


python = 'Python'
java = 'Java'
javascrypt = 'JavaScrypt'

python_img = PhotoImage(file='18717248.png')

lang = StringVar(value=java)

header = ttk.Label(textvariable=lang)
header.pack(**position)


python_btn = ttk.Radiobutton(text='pyton', value=python, variable=lang)
python_btn.pack(**position)

javascrypt = ttk.Radiobutton(text='pyton', value=javascrypt, variable=lang)
javascrypt.pack(**position)

java_btn = ttk.Radiobutton(text='pyton', value=java, variable=lang)
java_btn.pack(**position)




root.mainloop()