import random
m = []
k = []
for i in range(20):
    m.append(random.randint(-50, 50))
print(m)


def sumTenNambs(a):
    if len(a) == 1:
        return a[0]
    return a[0] + sumTenNambs(a[1:10])

i = 0
while i <= len(m) - 10:
    a = m[i: 10 + i]
    print(a, (sumTenNambs(a)))
    k.append(sumTenNambs(a))
    i +=1
print(f'Перша найменьша сума десяти чисел починається з {k.index(min(k)) + 1}  елементу')
