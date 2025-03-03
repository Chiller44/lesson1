from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle

HEIGHT = 550
WIDTH = 550

def registration():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=.5, rely=.5, relheight=.6, relwidth=.7, anchor='n')

    # sign in віджет
    label = Label(frame, text="Sign Up", font='16')
    label.place(relwidth=1, relheight=.1)

    # Login
    label_login = Label(frame, text="Login")
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_register = Entry(frame)
    login_register.place(relx=0.4, rely=0.2, relwidth=0.55, relheight=0.1)

    #Password
    label_password1 = Label(frame, text="Password: ")
    label_password1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relwidth=0.55, relheight=0.1)

    #Confirm pass
    label_password2 = Label(frame, text="Confirm Password: ")
    label_password2.place(rely=0.6, relwidth=0.35, relheight=0.1)

    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6, relwidth=0.55, relheight=0.1)

    #Button
    button = Button(frame, text="Sign Up", command=lambda: signup())
    button.place(relx=0.3, rely=0.8, relwidth=0.5, relheight=0.15)

    def signup():
        pass
    def save():
        pass

def login_form():
    pass

root = Tk()
root.title('Login Form')
root.geometry("%dx%d" % (WIDTH, HEIGHT)) #root.geometry("550x550")
root.resizable(True, True)

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='bg2.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_singup = Button(root, text="SIGN UP", bg='gold', command=registration)
button_singup.place(relx=0.2, rely=0.1, relwidth=0.3)

button_signin = Button(root, text="SIGN IN", bg='gold', command=login_form)
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)



root.mainloop()