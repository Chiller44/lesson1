x1 = (1, 7, 6, 9, 4, 19, 23)
x2 = (1, 2, 1, 9, 14, 19, 48, 7)
x3 = (1, 44, 9, 9, 22, 48, 7, 101)

#Завдання1
x1_n = []
for i in x1 and x2 and x3:
    if i in x1_n:
        continue
    else:
        if i in x1 and x2 and x2:
            x1_n.append(i)
print(f'Числа з трьох кортежів {x1_n}')


x21 = []
x22 = []
x23 = []
for i in x1:
    if i in x21:
        continue
    else:
        x21.append(i)
print(f'Унікальні елементи першого кортежу {x21}')
for i in x2:
    if i in x22:
        continue
    else:
        x22.append(i)
print(f'Унікальні елементи другого кортежу {x22}')
for i in x3:
    if i in x23:
        continue
    else:
        x23.append(i)
print(f'Унікальні елементи третього кортежу {x23}')


#Завдання3
x3_n = []
for i in range(len(x1)):
    if x1[i] == x2[i] and x1[i] == x3[i]:
        x3_n.append(x1[i])
print(f'Однакові елементи на одній позиції {x3_n}')
