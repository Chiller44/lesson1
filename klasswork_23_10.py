import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(-20, 20))
l = len(numbers)
print(numbers)
sum_vid = 0
for i in numbers:
    if i < 0:
        sum_vid += i
print('Сума відємних чисел: ', sum_vid)
sum_par = 0
for i in numbers:
    if i % 2 == 0:
        sum_par += i
print('Сума парних чисел: ', sum_par)
sum_nepar = 0
for i in numbers:
    if i % 2 != 0:
        sum_nepar += i
print('Сума непарних чисел: ', sum_nepar)
krat_3 = numbers[::3]
sum_krat_3 = 0
for i in krat_3:
    sum_krat_3 += i
print('Сума елементів, індекс яких кратний трьом: ', sum_krat_3)





