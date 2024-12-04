import random

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





