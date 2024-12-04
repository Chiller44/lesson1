import random

m = []
n = []
new = []
for _ in range(5):
    m.append(random.randint(1, 100))
for _ in range(7):
    n.append(random.randint(-3, 3))
print(m)
print (n)


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
















