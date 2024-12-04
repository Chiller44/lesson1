import random

m = []
for _ in range(10):
    m.append(random.randint(-20, 20))
print(m)
#Завдвння1
def summa(m):
    summ = 0
    for i in m:
        summ += i
    print(f'Сума всіх єлементів: {summ}')

summa(m)

#Завдання2
def bilshe(m):
    max_ = m[0]
    for i in m:
        if i > max_:
            max_ = i
    print(f'Найбільше число: {max_}')

bilshe(m)

#Завдання3
def parnepar(m):
    kil_p = 0
    kil_vid = 0
    for i in m:
        if i % 2 == 0:
            kil_p += 1
    print(f'Кількість парних чисел: {kil_p}')
    print(f'Кількість непарних чисел: {len(m) - kil_p}')
    for i in m:
        if i < 0:
            kil_vid += 1
    print(f'Кількість додатних чисел: {len(m) - kil_vid}')
    print(f"Кількість від'ємних чисел: {kil_vid}")

parnepar(m)

#Завдання4
def perevert(m):
    print(m[::-1])

perevert(m)

#Завдання5
x = int(input('Яке число шукаємо? '))
def poshuk(x):
    p = 0
    for i in m:
        if i == x:
            p += 1
    if p == 0:
        print('Такого числа немає в списку.')
    else:
        print(f'Дане число зустрічається {p} разів')

poshuk(x)

#Завдання6
f = []
h = []
for _ in range(10):
    f.append(random.randint(1, 8))
print(f)

def faktorial():
    for i in f:
        s = 1
        j = 1
        while j <= i:
            s *= j
            j += 1
        h.append(s)
    print(h)

faktorial()





