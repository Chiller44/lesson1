from tkinter import *
from tkinter import ttk

def click():
    print('Hello')

def entered(event):
    btn1['text'] = 'Entered'

def left(event):
    btn1['text'] = 'Left'

def single_click(event):
    btn2['text'] = 'Single Click'

def double_click(event):
    btn2['text'] = 'Double Click'

clicks = 0
def clicked(event):
    global clicks
    clicks = clicks +1
    btn1['text'] = f'{clicks} Clicks'

root = Tk()
root.title('It step')
root.geometry('350x250')

btn1 = ttk.Button(text='Click')
btn1.pack(anchor=CENTER, expand=1)

btn1.bind("<Enter>", entered)
btn1.bind("<Leave>", left)

btn2 = ttk.Button(text="Click")
btn2.pack(anchor=CENTER, expand=1)

btn2.bind("<ButtonPress>", single_click)
btn2.bind("<Double-ButtonPress-2>", double_click)

root.bind_class("TButton", "<Double-ButtonPress-3>", clicked)

root.mainloop()
