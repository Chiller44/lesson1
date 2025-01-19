from tkinter import *


def click_button(text):
    label.config(text="Button {}".format(text))


root = Tk()
root.title('"HOME WORK"')

button = Button(text="button 1", command=lambda: click_button(1)).grid(row=2, column=1)
button1 = Button(text="button 2", command=lambda: click_button(2)).grid(row=2, column=2)
button2 = Button(text="button 3", command=lambda: click_button(3)).grid(row=2, column=3)

label = Label(text="Position 1 ", bg="yellow", fg="red", width=10, height=5)

label.grid(row=1, column=1)

root.mainloop()
