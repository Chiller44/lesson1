from tkinter import *
from tkinter import ttk



root = Tk()
root.title('Підрахуйчик')
root.geometry('300x300')
root['bg'] = '#34e1eb'

def press_btn(digit):
    value = entry.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    entry.delete(0, END)
    entry.insert(0, value + digit)

def press_btn_dot(dot):
    value = entry.get()
    entry.delete(0, END)
    entry.insert(0, value+dot)


def press_operation_btn(operation):
    value = entry.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, END)
    entry.insert(0, value+operation)


def delete_all():
    entry.delete(0, END)
    entry.insert(0, '0')

def one_symb():
    entry.delete(len(entry.get())-1)

def result():
    try:
        res = entry.get()
        if res[-1] in '+-*/':
            operation = res[-1]
            res = res[:-1]+operation+res[:-1]
            entry.delete(0, END)
            entry.insert(0, eval(res))
        #if res.count(')') != res.count('('):
        #    entry.delete(0, END)
        #    entry.insert(0, 'ERROR')
        #else:
        entry.delete(0, END)
        entry.insert(0,eval(res))
    except SyntaxError:
        entry.delete(0, END)
        entry.insert(0, 'ERROR')




entry = Entry(font=('Arrial', 18), justify=RIGHT)
entry.insert(0, '0')
entry.grid(row=0, column=0, columnspan=5, padx=6, pady=6, sticky='wens')



btn = Button(text='0', bd=5, font=('Arrial', 13), command=lambda : press_btn('0')).grid(row=4, column=1, padx=6, pady=6, stick='wens')
btn = Button(text='1', bd=5, font=('Arrial', 13), command=lambda : press_btn('1')).grid(row=3, column=0, padx=6, pady=6, stick='wens')
btn = Button(text='2', bd=5, font=('Arrial', 13), command=lambda : press_btn('2')).grid(row=3, column=1, padx=6, pady=6, stick='wens')
btn = Button(text='3', bd=5, font=('Arrial', 13), command=lambda : press_btn('3')).grid(row=3, column=2, padx=6, pady=6, stick='wens')
btn = Button(text='4', bd=5, font=('Arrial', 13), command=lambda : press_btn('4')).grid(row=2, column=0, padx=6, pady=6, stick='wens')
btn = Button(text='5', bd=5, font=('Arrial', 13), command=lambda : press_btn('5')).grid(row=2, column=1, padx=6, pady=6, stick='wens')
btn = Button(text='6', bd=5, font=('Arrial', 13), command=lambda : press_btn('6')).grid(row=2, column=2, padx=6, pady=6, stick='wens')
btn = Button(text='7', bd=5, font=('Arrial', 13), command=lambda : press_btn('7')).grid(row=1, column=0, padx=6, pady=6, stick='wens')
btn = Button(text='8', bd=5, font=('Arrial', 13), command=lambda : press_btn('8')).grid(row=1, column=1, padx=6, pady=6, stick='wens')
btn = Button(text='9', bd=5, font=('Arrial', 13), command=lambda : press_btn('9')).grid(row=1, column=2, padx=6, pady=6, stick='wens')
btn = Button(text='(', bd=5, font=('Arrial', 13), command=lambda : press_btn('(')).grid(row=4, column=0, padx=6, pady=6, stick='wens')
btn = Button(text=')', bd=5, font=('Arrial', 13), command=lambda : press_btn(')')).grid(row=4, column=2, padx=6, pady=6, stick='wens')
btn = Button(text='+', fg='red', bd=5, font=('Arrial', 13), command=lambda : press_operation_btn('+')).grid(row=1, column=3, padx=6, pady=6, stick='wens')
btn = Button(text='-', fg='red', bd=5, font=('Arrial', 13), command=lambda : press_operation_btn('-')).grid(row=2, column=3, padx=6, pady=6, stick='wens')
btn = Button(text='x', fg='red', bd=5, font=('Arrial', 13), command=lambda : press_operation_btn('*')).grid(row=3, column=3, padx=6, pady=6, stick='wens')
btn = Button(text='/', fg='red', bd=5, font=('Arrial', 13), command=lambda : press_operation_btn('/')).grid(row=4, column=3, padx=6, pady=6, stick='wens')
btn = Button(text='C', bd=5, font=('Arrial', 13), command=delete_all).grid(row=1, column=4, padx=6, pady=6, stick='wens')
btn = Button(text='<--', bd=5, font=('Arrial', 13), command=one_symb).grid(row=2, column=4, padx=6, pady=6, stick='wens')
btn = Button(text=',', bd=5, font=('Arrial', 13), command=lambda : press_btn_dot('.')).grid(row=3, column=4, padx=6, pady=6, stick='wens')
btn = Button(text='=', bd=5, font=('Arrial', 13), command=result).grid(row=4, column=4, padx=6, pady=6, stick='wens')

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_columnconfigure(4, minsize=60)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)


root.mainloop()

