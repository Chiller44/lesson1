import csv

FILE_NAME = 'users.csv'

users = [
    [ 'Tom', 28],
    [ 'Alice', 22],
    [ 'Sam', 18]
]

with open(FILE_NAME, mode='w', newline="") as file:
    write = csv.writer(file)
    write.writerows(users)

with open(FILE_NAME, mode='a', newline="") as file:
    user = ['Bob', 33]
    write = csv.writer(file)
    write.writerow(user)

with open(FILE_NAME, mode='r', newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], '---', row[1])

