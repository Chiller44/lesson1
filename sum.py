#Завдання1
basketball = {'Petrov' : 198,
              'Sidorov' : 195,
              'Shevchenko' : 205,}

while True:
    choice = int(input('1 - додавання баскетболіста, 2 - видалення баскетболіста, '
                       '3 - пошук баскетболіста, 4 - зміна даних: '))
    if choice > 4 or choice < 1:
        print('Зробіть правильний вибір!')
    elif choice == 1:
        newBasket = input('Введіть призвище баскетболіста: ')
        basketball[newBasket] = int(input('Введіть зріст: '))
        print(basketball)
    elif choice == 2:
        delBasket = input("Введіть призвіще баскетболіста, якого потрібно видалити: ")
        if delBasket not in basketball:
            print('Немає такого баскетболіста в списку')
        else:
            del basketball[delBasket]
            print(basketball)
    elif choice == 3:
        findBasket = input('Введіть призвіще запитуємого баскетболіста: ')
        if findBasket not in basketball:
            print('Немає такого баскетболіста в списку')
        else:
            print(basketball.get(findBasket))
    elif choice == 4:
        changeBasket = input('Введіть призвіще баскетболіста для виправлення помилки в його зрості: ')
        if changeBasket not in basketball:
            print('Немає такого баскетболіста')
        else:
            newheight = int(input('Введіть вірний зріст: '))
            for i in basketball:
                if i == changeBasket:
                    basketball[changeBasket] = newheight
            print(basketball)


