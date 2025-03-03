from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle



def registration():

    frame = Frame(root)
    frame.place(relx=0.5, rely=0.15, relheight=.7, relwidth=.7, anchor='n')

    label = Label(frame, text='SIGN UP', font=('Georgia', 14))
    label.place(relx=0.4, rely=0.1)

    label_log = Label(frame, text='Login:', font=('Georgia', 12))
    label_log.place(relx=0.1, rely=0.3)

    entry_log = Entry(frame)
    entry_log.place(relx=0.5, rely=0.3)

    label_pass = Label(frame, text='Password:', font=('Georgia', 12))
    label_pass.place(relx=0.1, rely=0.5)

    entry_pass = Entry(frame, show='*')
    entry_pass.place(relx=0.5, rely=0.5)

    label_conf_pass = Label(frame, text='Confirm password:', font=('Georgia', 12))
    label_conf_pass.place(relx=0.1, rely=0.7)

    entry_conf_pass = Entry(frame, show='*')
    entry_conf_pass.place(relx=0.5, rely=0.7)

    button = Button(frame, text='SIGN UP', font=('Georgia', 14), command=lambda : signup)
    button.place(relx=0.4, rely=0.85)

def signup():
    error = ''
    if len(entry_pass.get()) == 0:
        error = 'ggg'









def login():
    frame = Frame(root)
    frame.place(relx=0.5, rely=0.15, relheight=.7, relwidth=.7, anchor='n')

    label = Label(frame, text='SIGN UP', font=('Georgia', 14))
    label.place(relx=0.4, rely=0.1)

    label = Label(frame, text='Login:', font=('Georgia', 12))
    label.place(relx=0.1, rely=0.3)

    entry = Entry(frame)
    entry.place(relx=0.5, rely=0.3)

    label = Label(frame, text='Password:', font=('Georgia', 12))
    label.place(relx=0.1, rely=0.5)

    entry = Entry(frame)
    entry.place(relx=0.5, rely=0.5)

    button = Button(frame, text='LOG IN', font=('Georgia', 14))
    button.place(relx=0.4, rely=0.7)



root = Tk()
root.title('Registration/Login form')
root.geometry('600x400')

img = PhotoImage(file='orange-wallpaper-background-1002-1073-hd-wallpapers-600x600.png')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

sgn_btn = Button(text='SIGN UP', font=('Georgia', 18), command=registration)
sgn_btn.place(relx=0.2, rely=0.05, relwidth=0.3, relheigh=0.1)

log_btn = Button(text='LOG IN', font=('Georgia', 18), command=login)
log_btn.place(relx=0.5, rely=0.05, relwidth=0.3, relheigh=0.1)


root.mainloop()