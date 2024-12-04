#Завдання2
number1 = int(input('Введіть перше число: '))
number2 = int(input('Введіть друге число: '))
def neparni(number1, number2):
    a = number1 + 1
    b = number2
    if number2 > number1:
        while a < number2:
            if a % 2 != 0:
                print(a, end=' ')
            a += 1
    else:
        while b < number1:
            if b % 2 != 0:
                print(b, end=' ')
            b +=1
print('Непарні числа між першим і другим числом:')
neparni(number1, number2)
print()

#Завдання3
len_line = int(input('Введіть довжину лінії: '))
direction = input('Введіть напрям (горизонтальний чи вертикальний): ')
symvol = input('Введіть символ: ')

def picture(len_line, direction, symvol):
    if direction == 'вертикальний':
        for i in range(len_line):
            print(symvol)
    if direction == 'горизонтальний':
        print(symvol * len_line)

picture(len_line, direction, symvol)
print()

#Завдання4
a1 = - 10
a2 = -19
a3 = 0
a4 =  -25

def bilshe(a1, a2, a3, a4):
    m = [a1, a2, a3, a4]
    max_ = m[0]
    for i in m:
        if i > max_:
            max_ = i
    print(max_)

bilshe(a1, a2, a3, a4)

#Завдання5
X1 = int(input('Введіть перше число: '))
X2 = int(input('Введіть друге число: '))

def summ(X1, X2):
    sum = 0
    if X1 < X2:
        y = X1 + 1
        while y < X2:
            sum += y
            y += 1
        print('Cума чисел між першим і другим числом', sum)
    if X1 > X2:
        y = X2 + 1
        while y < X1:
            sum += y
            y += 1
        print('Cума чисел між першим і другим числом', sum)

summ(X1, X2)

#Завдання7
x = int(input("Введіть число: "))

def lucky(x):
    if 99999 < x < 1000000:
        x = str(x)
        if int(x[0]) + int(x[1]) + int(x[2]) == int(x[3]) + int(x[4]) + int(x[5]):
            print(True)
        else:
            print(False)
    else:
        print('Число нешистизначне')

lucky(x)

