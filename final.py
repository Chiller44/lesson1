l =[]
def list1(l):
    while True:
        x = input('Введіть число (для виходу введіть stop): ')
        if x == 'stop':
            break
        l.append(int(x))
    n = int(input('Введіть N-й елемент: '))
    try:
        print(f'Весь список {l}')
        print(f'Максимальне значення списку {max(l)}')
        print(f'Мінімальне значення списку {min(l)}')
        print(f'N-ий елемент списку {l[n]}')
        del l[n]
        print(f'Список після видалення n-го елементу {l}')
    except IndexError:
        print('N-й елемент більше довжини списку')

list1(l)






