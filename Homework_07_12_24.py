import random

def neparni(x, y):
    m = [i for i in range(x, y) if i % 2 != 0]
    print(m)

neparni(1,30)

m = [25, 31, 1, 2, 33, 74, 15, 6, 7, 88, 19, 10, 3, 5, 13]
n = []
def v(m, x, y):
    for i in m:
        if i < x or i > y:
            n.append(i)
    print(n)


v(m, 10, 50)

symbol = input('Введіть символ для лінії: ')
length_of_line = int(input('Введіть довжину лінії: '))
type_of_line = int(input('Який тип лінії: 1 - горизонтальна, 2 - вертикальна: '))

def show_line(symbol, function_to_call):
    draw = function_to_call(symbol)
    return draw

def function_to_call(symbol, type_of_line):
    if type_of_line == 2:
        for i in range(length_of_line):
            print(symbol)
    elif type_of_line == 1:
        for i in range(length_of_line):
            print(symbol, end=" ")
    else:
        print('Зробіть правильний вібір!')

function_to_call(symbol, type_of_line)

#show_line(symbol, function_to_call)