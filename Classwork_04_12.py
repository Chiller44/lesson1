l =[]
def sum_list1(l):
    global k
    while True:
        x = input('Введіть число (для виходу введіть stop): ')
        if x == 'stop':
            break
        l.append(int(x))
    k = l
    print(l)
    print(f'Сума всіх чисел списку {sum(l)}')


try:
    sum_list1(l)
    for i in k:
        if i < 0:
            raise Exception
except:
    print("В списку присутні від'ємні числа")

print(k)