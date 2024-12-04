import random

b = int(input('Введіть число: '))
n = int(input('Введіть степінь: '))
def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)

print(expt(b, n))

a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
def summa(a, b):
    if a > b:
        return 0
    return a + summa(a + 1, b)
print(summa(a, b))

x = int(input('Введіть число: '))
def draw(x):
    if x <= 0:
        return 0
    print('*', end=' ')
    draw(x - 1)

draw(x)
print()

#Завдання5
m = []
k = []
for i in range(20):
    m.append(random.randint(-50, 50))
print(m)
i = 0
while i <= len(m) - 10:
    print({i + 1}, f'Зріз по 10 елементів {(m[i:10 + i])}', f'Хочу побачити суму цих елементів {sum(m[i:10 + i])}', f'Та його довжину {len((m[i:10 + i]))}')
    k.append(sum(m[i:10 + i]))
    i += 1
print(f'Перша Мінімальна сума 10 чисел починається з {k.index(min(k)) + 1} елементу')