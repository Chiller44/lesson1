import random

list1 = []
list2 = []
for _ in range(10):
    list1.append(random.randint(-5, 5))
for _ in range(9):
    list2.append(random.randint(-5, 50))
print('Список1: ', list1)
print('Список2: ', list2)
print('Елементи обох списків: ', list1 + list2)

list3 = []
for i in list1 + list2:
    if i in list3:
        continue
    else:
        list3.append(i)
print('Елементи списків без повторень: ',list3)
print('Не розумію чим він відрізняється від списку з унікальних елементів.')

list4 = []
for i in list1 and list2:
    if i in list4:
        continue
    else:
        if i in list1 and list2:
            list4.append(i)
print('Елементи спільні для двох списків: ',list4)

list5 = [max(list1), min(list1), max(list2), min(list2)]
print('Максимальне і мінімальне значення кожного із списків: ', list5)


