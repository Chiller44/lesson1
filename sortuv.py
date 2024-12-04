import random

m = []
n = []
for _ in range(10):
    m.append(random.randint(-50, 50))
for _ in range(11):
    n.append(random.randint(-50, 50))
print(f'Перший список {m}')
print(f'Другий список {n}')

#Завдання1
for i in range(len(m)):
    for i in range(len(m) - i - 1):
        if m[i] > m[i + 1]:
            m[i], m[i + 1] = m[i + 1], m[i]
print(f'Отсортований за зростанням перший список {m}')

#Завдання
for i in range(len(n) // 2):
    for i in range(len(n) // 2 - i - 1):
        if n[i] < n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
for i in range(len(n) // 2 + 1, len(n)):
    for i in range(len(n) // 2 + 1, len(n) - i - 1):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
print(f'Перша половина другого списка за спаданням, друга половина - за зростанням {n}')