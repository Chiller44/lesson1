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
while z < y:
    if z % 3 == 0 and z % 5 == 0:
        print('Fizz Buzz', end='   ')
    z += 1
print()
z = x + 1
while z < y:
    if z % 3 != 0 and z % 5 != 0:
        print(z, end=' ')
    z += 1
