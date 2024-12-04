# Модуль 2. Цикли. Частина 1

# Завдання 1
x = int(input('Введіть перше число: '))
y = int(input('Введіть друге число: '))
while x<= y:
    if x % 7 == 0:
        print(x, end=' ')
    x += 1
print('\n')

# Завдання 2
x = int(input('Введіть перше число: '))
y = int(input('Введіть друге число: '))
x1 = x
print('Числа в заданому диапазоні:')
while x1 <= y:
  print(x1, end = ' ')
  x1 += 1
print()

x2 = x
y2 = y
print('Числа діапазону за спаданням: ')
while y2 >= x2:
  print(y2, end = ' ')
  y2 -= 1
print()

x3 = x
y3 = y
print('Числа кратні семи в заданому диапазоні:')
while x3 <= y3:
  if x3 % 7 == 0:
    print(x3, end=' ')
  x3 += 1
print()

x4 = x
print("Кількість чисел кратних п'яти: ")
summ = 0
while x4 <= y:
  if x4 % 5 == 0:
    summ = summ + 1
  x4 += 1
print(summ, end =' ')
print()

# Завдання 3
x = int(input('Введіть перше число: '))
y = int(input('Введіть друге число: '))
z = x + 1
while z < y:
    if z % 3 == 0:
        print('Fizz', end=' ')
    z += 1
print()
z = x +1
while z < y:
    if z % 5 == 0:
        print('Buzz', end=' ')
    z += 1
print()
z = x + 1
while z <= y:
    if z % 3 == 0 and z % 5 == 0:
        print('FizzBuzz', end='   ')
    z += 1
print()

z = x + 1
while z < y:
    if z % 3 != 0 and z % 5 != 0:
        print(z, end=' ')
    z += 1






