#FILENAME = 'orange.png'
#NEWFILENAME = 'orange_new.png'
#
#image_data = []
#
#with open (NEWFILENAME, 'rb') as file:
#    image_data = file.read()
#
#with open (FILENAME, 'wb') as file:
#    file.write(image_data)

import pickle

FILENAME = 'user.dat'

#name = 'Tom'
#age = 22
#
#with open (FILENAME, 'wb') as file:
#    pickle.dump(name, file)
#    pickle.dump(age, file)
#
#with open (FILENAME, 'rb') as file:
#    name = pickle.load(file)
#    age = pickle.load(file)
#    print(f'Name: {name}\tAge: {age}')

users = [['Tom', 22, True], ['Bob', 12, False]]

with open (FILENAME, 'wb') as file:
    users_from_file = pickle.load(file)
    for u in users_from_file:
        print(f'{u[0], {u[1]})



