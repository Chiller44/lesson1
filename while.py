import random

l =[]
for _ in range(12):
    l.append(random.randint(-50, 50))
print(l)
for i in range(len(l) // 2):
    for j in range(len(l) // 2 - i - 1):
        if l[j] < l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
for i in range(len(l) // 2 + 1, len(l)):
    for j in range(len(l) // 2 + 1, len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(l)



