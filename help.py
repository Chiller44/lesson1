
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
