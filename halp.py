from tkinter import *
from tkinter import ttk

from Classwork_20_01_25 import show_message
from help import button

root = Tk()
root.title('It step')
root.geometry('250x250')

def click_btn():
    lable['text'] = button.get(['text'])


btn = ttk.Button(text='text', command=click_btn)
btn.pack()

lable = ttk.Label()
lable.pack()


root.mainloop()
















