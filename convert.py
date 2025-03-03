from tkinter import *
from tkinter import ttk

from cw_19_02_25_3 import spinbox

EXCHANGE_RATES = {
    "USD" : 1,
    "EUR" : 0.92,
    "GBP" : 0.78,
    "UAH" : 42
}

def convert_currency():
    if to_currency_menu.get() != from_currency_menu.get():
        amount_spinbox.get() * EXCHANGE_RATES.keys()



root = Tk()
root.title("Конвертор валют")
root.geometry("500x500")

#вводимо валюту(вибираємо з комбобокса)
ttk.Label(root, text="З: ").pack()
from_currency_var = StringVar(value="USD")
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=list(EXCHANGE_RATES.keys()), state="readonly")
from_currency_menu.pack()

#вводимо суму
ttk.Label(root, text="Сума: ").pack()
amount_var = DoubleVar(value=1)
amount_spinbox = ttk.Spinbox(root, textvariable=amount_var, increment=1, from_=1, to=10000)
amount_spinbox.pack()

#Повзунок'
amount_scale = ttk.Scale(root, from_=1, to=10000, orient="horizontal", variable=amount_var)
amount_scale.pack(fill=X, padx=10)

#вибір валюти дял конвертації
ttk.Label(root, text="В: ").pack()
to_currency_var = StringVar(value="EUR")
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=list(EXCHANGE_RATES.keys()), state="readonly")
to_currency_menu.pack()

#btn convert
convert_button = ttk.Button(root, text="Конвертувати", command=convert_currency)
convert_button.pack(pady=10)

#result label
result_var = StringVar(value="Виберіть параметри")
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.pack()

root.mainloop()