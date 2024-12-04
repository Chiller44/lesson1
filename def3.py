a1 = 3
a2 = -19
a3 = 0
a4 = -5

def bilshe(a1, a2, a3, a4):
    m = [a1, a2, a3, a4]
    max_ = m[0]
    for i in m:
        if i > max_:
            max_ = i
    print(f'Найбільше число {max_}')

bilshe(a1, a2, a3, a4)

X1 = int(input('Введіть перше число: '))
X2 = int(input('Введіть друге число: '))


def summ(X1, X2):
    sum = 0
    if X1 < X2:
        y = X1 + 1
        while y < X2:
            sum += y
            y += 1
        print(sum)
    if X1 > X2:
        y = X2 + 1
        while y < X1:
            sum += y
            y += 1
        print(sum)

summ(X1, X2)






