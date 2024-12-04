#Завдання1
countrys = {'Poland', 'Italy', 'USA', 'Norway', 'Canada', 'Belgium'}

x = int(input('Введіть: 1 - додавання країни, 2 - видалення країни, 3 - пошук за символом, 4 - пошук країни: '))
if x == 1:
    addCuontry = input('Введіть країну для додавання в множину: ')
    countrys.add(addCuontry)
    print(countrys)
if x == 2:
    delCuontry = input('Введіть країну для видалення з множини: ')
    countrys.discard(delCuontry)
    print(countrys)
if x == 3:
    findSynb = input('Введіть символ для пошуку в множині: ')
    c = 0
    for i in countrys:
        if findSynb.lower() in i.lower():
            print(i)
            c += 1
    if c == 0:
        print('Немає такої країни в списку')

if x == 4:
    findCountry = input('Введіть країну для пошуку: ')
    if findCountry in countrys:
        print('Країна є в множині')
    else:
        print('Країни немає в множині')


#Завдвння 2, 3, 4
cities1 = {'Oslo', 'Paris', 'Kyiv', 'Munich', 'Lviv', 'Rome', "Odessa", 'Paris'}
cities2 = {'Milan', 'Kyiv', 'Riga', 'Manchester', 'Batumi', 'Oslo', "Dublin", 'Riga'}

v_obokh = cities1.intersection(cities2)
print(v_obokh)

in_cities1_no_cities2 = cities1.difference(cities2)
print(in_cities1_no_cities2)

in_cities2_no_cities1 = cities2.difference(cities1)
print(in_cities2_no_cities1)

uniq_1_and_2 = cities1.union(cities2)
print(uniq_1_and_2)