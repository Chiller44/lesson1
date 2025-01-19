from tkinter import *
from tkinter import ttk

root = Tk()
root.title('It step')
root.geometry('250x250')

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text= f'P{r}, {c}')
        btn.grid(row=r, column=c)


root.mainloop()