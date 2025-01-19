from tkinter import *

root = Tk()
root.title('Перша наша програма в ткінтері')
root.geometry('600x350')
root.minsize(200, 500)
#root.attributes('-fullscreen', True)
root.attributes('-alpha', 0.1)

lable = Label(text='Hello Python')
lable.pack()

root.mainloop()
