import random

#Завдвння 1
m = []
sum = 0
for _ in range(10):
    m.append(random.randint(-10, 1))
print(m)
for i in m:
    sum = sum + i
if sum/len(m) > 0:
    for i in range((len(m) * 2) // 3):
        for j in range(len(m) * 2 // 3 - i -1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    k = m[:len(m) * 2 // 3]
    j = m[len(m) * 2 // 3:]
    y = j[::-1]
    print(k + y)
else:
    for i in range((len(m) // 3)):
        for j in range(len(m) // 3 - i -1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    k = m[:len(m) // 3]
    j = m[len(m) // 3:]
    y = j[::-1]
    print(k + y)
print()

#Завдання2
otsinky = []
summa_otsinok = 0
for i in range(10):
    x = int(input('Введіть оцінку: '))
    otsinky.append(x)
print(f'Список оцінок:\n{otsinky}')
pereispyt = int(input('Який іспит перескладаємо (1-10): '))
nova_otsinka = int(input('Введіть нову оцынку: '))
otsinky[pereispyt - 1] = nova_otsinka
print(otsinky)
for i in otsinky:
    summa_otsinok += i
if summa_otsinok / len(otsinky) < 10.7:
    print('Низька успішність. Стинендія не отримується.')
else:
    print('Стипендія отримується.')
for i in range(len(otsinky)):
    for j in range(len(otsinky) - i - 1):
        if otsinky[j] > otsinky[j + 1]:
            otsinky[j], otsinky[j + 1] = otsinky[j + 1], otsinky[j]
print(f'Отсортований за зростанням список\n{otsinky}')