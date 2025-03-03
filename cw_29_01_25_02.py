from tkinter import *
from tkinter import messagebox
import random



HEIGHT = 600
WIDTH = 600

tasks = []

def update_listbox():
    lisbox.delete(0, END)
    for task in tasks:
        lisbox.insert(END, task)

def add_task():
    task = text_input.get()
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning('Warning', 'Enter task in th input box, please!')
    text_input.delete((0, END))

def del_one():
    task = lisbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def del_all():
    comfirmed = messagebox.askyesno('Pleace confirm', 'Do u really want dal all?')
    if comfirmed:
        global tasks
        update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort(reverse=True)
    update_listbox()

def choose_random():
    if len(tasks) > 0:
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        messagebox.showwarning('warning', 'No tasks')

def show_number_of_task():
    number_of_task = len(tasks)
    message = f'Number of tasks: {number_of_task}'
    label_display['text'] = message

root = Tk()
root.title('Todo list')
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.resizable(False, False)

img = PhotoImage(file='todo_bg.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

root.option_add('Font', '{Comic Sans MS} 10')
root.option_add('Background', 'white')

frame = Frame(root, border=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_title = Label(frame, text='My todo-list', fg='dark blue', font='{Comic Sans MS} 16')
label_title.place(relx=0.35)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)

btn_add_task = Button(frame, text='Add task', command=add_task)
btn_add_task.place(rely=0.15, relwidth=0.25)

btn_dell = Button(frame, text='Delete', command=del_one)
btn_dell.place(rely=0.25, relwidth=0.25)

btn_dell_all = Button(frame, text='Delete All', command=del_all)
btn_dell_all.place(rely=0.35, relwidth=0.25)

btn_sort_asc = Button(frame, text='Sort (A-Z)', command=sort_asc)
btn_sort_asc.place(rely=0.45, relwidth=0.25)

btn_sort_desc = Button(frame, text='Sort (Z-A)', command=sort_desc)
btn_sort_desc.place(rely=0.55, relwidth=0.25)

btn_random = Button(frame, text='Choose random', command=choose_random)
btn_random.place(rely=0.65, relwidth=0.25)

btn_number_of_tasks = Button(frame, text='Number of task', command=show_number_of_task)
btn_number_of_tasks.place(rely=0.75, relwidth=0.25)

btn_exit = Button(frame, text='Exit', command=exit)
btn_exit.place(rely=0.85, relwidth=0.25)

lisbox = Listbox(frame)
lisbox.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.67)

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='My menu')
file_menu.add_command(label='Exit', command=exit)

menu.add_cascade(label='File', menu=file_menu)

root.mainloop()