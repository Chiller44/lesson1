a = [1, 8, 3, 8, 7, 4]

print(a)

j = 0
while j < len(a):
    k = 0
    while k < (len(a) - 1):
        if a[k] > a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]
        k += 1
    j += 1

print(a)            