def press_btn_dot(digit):
    value = entry.get()
    if value[0] == '0':
        value = value[1:]
    entry.delete(0, END)
    entry.insert(0, value+digit)