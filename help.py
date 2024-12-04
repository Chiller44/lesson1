office = {'Petrov' : ['+3801111111', '111@gmail.com', 'director', '№1', 'skype_petrov'],
          'Sidorov' : ['+3802222222', '222@gmail.com', 'manager', '№4', 'skype_sidorov'],
          'Shevchenko' : ['+3804444444', '441@gmail.com', 'driver', '№11', 'skype_sheva'],
          'Sidor' : ['+3806666666', '551@gmail.com', 'killer', '№200', 'skype_gung'],
          'Loboda' : ['+3809991111', 'song@gmail.com', 'artist', '№17', 'skype_song']}
b = 'ggg'
for i in office:
    data = office.get(i)
        if enter_type in data:
            z += 1
            print(i)
        if z == 0:
            print('Введіть правильні дані')