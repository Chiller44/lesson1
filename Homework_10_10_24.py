#Завдання1
try:
    age = int(input('Введіть свій вік: '))
    name = input("Введіть своє ім'я: ")
    if age < 0 or age > 130:
        raise Exception
    print(f'Привіт, {name}! Тобі {age} років.')
except:
    print(f'{name},шось підозрілий вік.')
print()

#Завдання2.1
age = int(input('Введіть свій вік: '))
name = input("Введіть своє ім'я: ")
def personalData(age, name):
    print(f'Привіт, {name}! Тобі {age} років.')
try:
    if age < 0 or age > 130:
        raise Exception
    personalData(age, name)
except:
    print(f'{name}, шось підозрілий вік.')
print()

#Завдання2.2
age = int(input('Введіть свій вік: '))
name = input("Введіть своє ім'я: ")
def personalData(age, name):
    try:
        if age < 0 or age > 130:
            raise Exception
        print(f'Привіт, {name}! Тобі {age} років.')
    except:
        print(f'{name}, шось підозрілий вік.')

personalData(age, name)
print()


#Завдання3
l =[]
while True:
    x = input('Введіть число (для виходу введіть stop): ')
    if x == 'stop':
        break
    l.append(int(x))
print(l)
try:
    for i in l:
        if i < 0:
            raise Exception
    print(f'Сума всіх чисел списку {sum(l)}')
except:
    print("В списку присутні від'ємні числа")
print()


#Завдання4.2
l =[]
def sum_list2(l):
    while True:
        x = input('Введіть число (для виходу введіть stop): ')
        if x == 'stop':
            break
        l.append(int(x))
    print(l)
    try:
        for i in l:
            if i < 0:
                raise Exception
        print(f'Сума всіх чисел списку {sum(l)}')
    except:
        print("В списку присутні від'ємні числа")

sum_list2(l)