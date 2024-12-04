city1 = {'Kyiv', 'Odessa', 'Rivne', 'Mykolayv'}
city2 = {'Kyiv', 'Donetsk', 'Lviv', 'Rivne'}
x = city1.intersection(city2)
print(x)

x2 = city1.difference(city2)
print(x2)

x3 = city2.difference(city1)
print(x3)

x4 = city1.union(city2)
print(x4)

country = {'Ukraine':'Kyiv', 'Canada':'Ottava', 'Poland':'Warsaw'}
print(country.update(['GB,Ljndon']))

