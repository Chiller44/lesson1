
#Завдання2
x1 = int(input('Введіть перше число: '))
x2 = int(input('Введіть друге  число: '))

def parni(x1, x2):
    m = []
    if x2 > x1:
        x1 = x1 + 1
        while x1 < x2:
            if x1 % 2 == 0:
                m.append(x1)
            x1 += 1
        print(m)
    else:
        x2 = x2 + 1
        while x2 < x1:
            if x2 %2 == 0:
                m.append(x2)
            x2 += 1
        print(m)


parni(x1, x2)

#Завдання3
symbol = input('ВВедіть символ: ')
length = int(input('Введіть довжину сторони квадрата: '))
x = False

def square(symbol, length, x):
    if x == True:
        for i in range(length):
            print(symbol * length)
    else:
        print(symbol * length)
        for i in range(length - 2):
            print(symbol + ' ' * (length - 2) + symbol)
        print(symbol * length)

square(symbol, length, x)

#Завдання4
y1 = 25
y2 = -5
y3 = 17
y4 = -27
y5 = 0

def minimum(y1, y2, y3, y4, y5):
    a =(y1, y2, y3, y4, y5)
    min_ = a[0]
    for i in a:
        if i < min_:
            min_ = i
    print(min_)

minimum(y1, y2, y3, y4, y5)

#Завдання5
x1 = int(input('Введіть перше число: '))
x2 = int(input('Введіть друге  число: '))

def dobutok(x1, x2):
    dob = 1
    if x1 < x2:
        x1 = x1 + 1
        while x1 < x2:
            dob *= x1
            x1 += 1
        print(dob)
    else:
        x2 = x2 + 1
        while x2 < x1:
            dob *= x2
            x2 += 1
        print(dob)

dobutok(x1, x2)

#Завдання6
#Варіант1
x1 = input('Введіть число: ')
def kol_vo(x1):
    print(f'В {x1} {len(x1)} цифр')

kol_vo(x1)

#Варіант2
x2 = 145
def kol_vo2(x2):
    x2 = str(x2)
    print(f'В {x2} {len(x2)} цифр')

kol_vo2(x2)

#Завдання6
x1 = input('Введіть число: ')
def palindrom(x1):
    if len(x1) % 2 != 0:
        print(False)
    else:
        k = x1[:(len(x1) // 2)]
        y = x1[(len(x1) // 2):]
        if k == y[::-1]:
            print(True)
        else:
            print(False)

palindrom(x1)
