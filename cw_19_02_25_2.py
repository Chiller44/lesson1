from tkinter import *
from tkinter import ttk



root = Tk()
root.title('Scale')
root.geometry('500x500')

val = IntVar(value=22)

#v_scale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
#v_scale.pack()
def change(new_val):
    float_val = float(new_val)
    int_val = round(float_val)
    label['text'] = int_val




label = ttk.Label()
label.pack(anchor=N)

h_scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=50, variable=val, command=change)
h_scale.pack()

root.mainloop()