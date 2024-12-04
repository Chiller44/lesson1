import random

m = []
n = []
for _ in range(5):
    m.append(random.randint(-10, 10))
for _ in range(5):
    n.append(random.randint(-10, 10))
print(m)
print(n)

#Завдання1
def dobutok(m):
    d = 1
    for i in m:
        d *= i
    print(d)

dobutok(m)

#Завдвння2
def minimum(m):
    min_ = m[0]
    for i in range(len(m)):
        if m[i] < min_:
            min_ = m[i]
    print(min_)

minimum(m)

#Завдання3
def proste(m):
    l = []
    j = 0
    for i in m:
        k = 0
        x = 1
        while x <= i:
            if i % x == 0:
                k += 1
            x += 1
        if k == 2:
            j += 1
            l.append(i)

    print(f'Вивів ще новий список з простими чмслами: {l}')
    print(f'Простих чисел {j}')

proste(m)

#Завдання4
x = int(input('ВВедите число: '))
def vydalennya(x):
    k = 0
    for i in m:
        if x in m:
            m.remove(x)
            k += 1
    print(f'Видалених чисел {k}')

vydalennya(x)

#Завдання5
def mn(m, n):
    newList = []
    for i in m and n:
        if i in newList:
            continue
        else:
            if i in m and n:
                newList.append(i)
    print(newList)

mn(m, n)

#Завдання6
x = int(input('ВВедите степень: '))
def stepen(m, x):
    newList2 = []
    a = 1
    for i in m:
        a = i ** x
        newList2.append(a)
    print(newList2)

stepen(m, x)