#Завдання1
try:
    x = int(input('Введіть число: '))
    i = 1
    y = 1
    if x < 0:
        raise Exception
    while i <= x:
        y *= i
        i +=1
    print(f'Факторіал введеного числа дорівнює {y}')
except:
    print(f"Введене число від'ємне!")

#Завдання2.1
t = int(input('Введіть число: '))
def factor1(t):
    try:
        i = 1
        y = 1
        if t < 0:
            raise Exception
        while i <= t:
            y *= i
            i +=1
        print(f'Факторіал введеного числа дорівнює {y}')
    except:
        print(f"Введене число від'ємне!")

factor1(t)

#Завдання2.2
b = int(input('Введіть число: '))
def factor2(b):
    i = 1
    y = 1
    while i <= b:
        y *= i
        i += 1
    print(f'Факторіал введеного числа дорівнює {y}')
try:
    if b < 0:
        raise Exception
    factor2(b)
except:
    print(f"Введене число від'ємне!")

#Завдання3
l =[]
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

#Завдання4.1
l =[]
def list1(l):
    while True:
        x = input('Введіть число (для виходу введіть stop): ')
        if x == 'stop':
            break
        l.append(int(x))
    n = int(input('Введіть N-й елемент: '))
    print(f'Весь список {l}')
    print(f'Максимальне значення списку {max(l)}')
    print(f'Мінімальне значення списку {min(l)}')
    print(f'N-ий елемент списку {l[n]}')
    del l[n]
    print(f'Список після видалення n-го елементу {l}')

try:
    list1(l)
except IndexError:
    print('N-й елемент більше довжини списку')

#Завдання4.2
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



