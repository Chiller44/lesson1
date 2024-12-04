m = [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
k = []
print(m)
i = 0
while i <= len(m) - 10:
    print((m[i:10 + i]), sum(m[i:10 + i]), len((m[i:10 + i])))
    k.append(sum(m[i:10 + i]))
    i += 1
print(f'Мінімальна сума 10 чисел починається з {k.index(min(k)) + 1} елементу')




