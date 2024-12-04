#Завдання1
fruits = ('banana', 'cherry', 'apple', 'mango', 'cherry', 'apple', 'strowberry', 'apple-cherry', 'banana-mango', 'apple-banana')
find_fruit = input('Enter fruit: ')
print(f'Всього {fruits.count(find_fruit)} {find_fruit} в списку')

#Завдвння2
find_fruit = input('Enter fruit: ')
count = 0
for i in fruits:
    if find_fruit in i:
        count += 1
print(f'Всього {find_fruit} {count} в списку')

cars = ('BMW', 'Audi', 'Opel', 'BMW', 'Ford', 'Mazda', 'Ford', 'Opel')
brand = input("Введіть макру авто: ")
change = input('Введіть марку авто для заміни: ')
new_cars = []
for i in list(cars):
    if i == brand:
        i = change
    new_cars.append(i)
print(new_cars)

#Завдання4
numbers = (1, 115, 459, 2, 36985, 8, -6589333634, -5487, 58436, 589678214569532587)
x = []
for i in numbers:
    x.append(len(str(abs(i))))
larged = max(x)
for i in range(1,larged + 1):
    if x.count(i) > 0:
        print(f'{i} - значних:  {x.count(i)}')



