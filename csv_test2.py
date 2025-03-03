import csv



FILENAME = 'users2.txt'

users = [
    {'name': 'Tom', 'age': 23},
    {'name': 'Sam', 'age': 24},
    {'name': 'Bob', 'age': 25}
          ]

with open(FILENAME, mode='w', newline='') as file:
    columns = ['name', 'age']
    write = csv.DictWriter(file, fieldnames=columns)

    write.writeheader()
    write.writerows(users)