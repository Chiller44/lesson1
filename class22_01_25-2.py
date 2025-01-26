from tkinter import *
from tkinter import ttk, StringVar



root = Tk()
root.title('IT Step')
root.geometry('400x350')

position = {'padx': 6, 'pady':6, 'anchor':NW}
languages = ['Python', 'Java', 'Javascrypt']
selected_language = StringVar()

header = ttk.Label(text='Виберіт мову')
header.pack(**position)

def select():
    header.config(text=f'Вибрано {selected_language.get}')

for lang in languages:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_language, command=select)
    lang_btn.pack(**position)

root.mainloop()
