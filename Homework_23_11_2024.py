#Завдання1
basketball = {'Petrov' : 198,
              'Sidorov' : 195,
              'Shevchenko' : 205,}

while True:
    choice = int(input('1 - додавання баскетболіста, 2 - видалення баскетболіста, '
                       '3 - пошук баскетболіста, 4 - зміна даних, 5 - вихід: '))
    if choice > 5 or choice < 1:
        print('Зробіть правильний вибір!')
    elif choice == 1:
        newBasket = input('Введіть призвище баскетболіста: ')
        basketball[newBasket] = int(input('Введіть зріст: '))
        print(basketball)
    elif choice == 2:
        delBasket = input("Введіть призвіще баскетболіста, якого потрібно видалити: ")
        if delBasket not in basketball:
            print('Немає такого баскетболіста в списку')
        else:
            del basketball[delBasket]
            print(basketball)
    elif choice == 3:
        findBasket = input('Введіть призвіще запитуємого баскетболіста: ')
        if findBasket not in basketball:
            print('Немає такого баскетболіста в списку')
        else:
            print(basketball.get(findBasket))
    elif choice == 4:
        changeBasket = input('Введіть призвіще баскетболіста для виправлення помилки в його зрості: ')
        if changeBasket not in basketball:
            print('Немає такого баскетболіста')
        else:
            newheight = int(input('Введіть вірний зріст: '))
            for i in basketball:
                if i == changeBasket:
                    basketball[changeBasket] = newheight
            print(basketball)
    elif choice == 5:
        break


#Завдвння3
office = {'Petrov' : ['+3801111111', '111@gmail.com', 'director', '№1', 'skype_petrov'],
          'Sidorov' : ['+3802222222', '222@gmail.com', 'manager', '№4', 'skype_sidorov'],
          'Shevchenko' : ['+3804444444', '441@gmail.com', 'driver', '№11', 'skype_sheva'],
          'Galushko' : ['+3806666666', '551@gmail.com', 'killer', '№200', 'skype_gung'],
          'Loboda' : ['+3809991111', 'song@gmail.com', 'artist', '№17', 'skype_song']}

while True:
    def findWorker(enter_type):
        z = 0
        for i in office:
            data = office.get(i)
            if enter_type in data:
                z += 1
                print(i)
        if z == 0:
            print('Введіть правильні дані')


    choice = int(input('1 - додавання робітників, 2 - видалення робітників, '
                       '3 - пошук, 4 - зміна даних, 5 - вихід: '))
    if choice > 5 or choice < 1:
        print('Зробіть правильний вибір!')
    elif choice == 1:
        anketa = []
        newWorker = input('Введіть призвище нового співробітника: ')
        anketa.append(newWorker)
        newNumber = input('Введіть номер телефона нового співробітника: ')
        anketa.append(newNumber)
        newMail = input('Введіть електронну адресу нового співробітника: ')
        anketa.append(newMail)
        title = input('Введіть посаду нового співробітника: ')
        anketa.append(title)
        newRoom = input('Введіть номер кабінета нового співробітника: ')
        anketa.append(newRoom)
        newSkype = input('Введіть skype нового співробітника: ')
        anketa.append(newSkype)
        office[newWorker] = anketa
        print(office)
    elif choice == 2:
        delWorker = input('Введіть призвище звільненого співробітника: ')
        if delWorker not in office:
            print('Немає такого співробітника')
        else:
            del office[delWorker]
            print(office)
    elif choice == 3:
        choose_type = int(input('За чим шукаємо співробітника? 1- за телефоном, 2 - за поштою, '
                           '3 - за посадою, 4 - за номером кабінета, 5 - за скайпом: '))
        if choose_type == 1:
            enter_type = input('Введiть номер телефону: ')

            findWorker(enter_type)

        if choose_type == 2:
            enter_type = input('Введiть електрону адресу: ')

            findWorker(enter_type)

        if choose_type == 3:
            enter_type = input('Введiть посаду працівника: ')

            findWorker(enter_type)

        if choose_type == 4:
            enter_type = input('Введiть номнр кабінета працівника: ')

            findWorker(enter_type)

        if choose_type == 5:
            enter_type = input('Введiть скайп працівника: ')

            findWorker(enter_type)

    elif choice == 4:
        change_type = int(input('Що треба змінити? 1- номер телефона, 2 - електронну адресу, '
                                '3 - посаду, 4 - номер кабінета, 5 - скайп: '))

        if change_type == 1:
            change_tel = input('Чий номер телефону змінився? ')
            if change_tel not in office:
                print('Немає такого співробітника')
            else:
                new_tel = input('Введіть новий номер телефону: ')
                for i in office:
                    if i == change_tel:
                        tel = office.get(i)
                        tel[0] = new_tel
                        print(tel)

        if change_type == 2:
            change_mail = input('Чия електронна адреса змінилась? ')
            if change_mail not in office:
                print('Немає такого співробітника')
            else:
                new_mail = input('Введіть нову електронну адресу: ')
                for i in office:
                    if i == change_mail:
                        mail = office.get(i)
                        mail[1] = new_mail
                        print(mail)

        if change_type == 3:
            change_title = input('Чия посада змінилась? ')
            if change_title not in office:
                print('Немає такого співробітника')
            else:
                new_title = input('Введіть нову посаду: ')
                for i in office:
                    if i == change_title:
                        title = office.get(i)
                        title[2] = new_title
                        print(title)

        if change_type == 4:
            change_room = input('Чий кабінет змінився? ')
            if change_room not in office:
                print('Немає такого співробітника')
            else:
                new_room = input('Введіть новий номер кабінета: ')
                for i in office:
                    if i == change_room:
                        room = office.get(i)
                        room[3] = new_room
                        print(room)

        if change_type == 5:
            change_skype = input('Чий skype змінився? ')
            if change_skype not in office:
                print('Немає такого співробітника')
            else:
                new_skype = input('Введіть новий skype: ')
                for i in office:
                    if i == change_skype:
                        skype = office.get(i)
                        skype[4] = new_skype
                        print(skype)
    elif choice == 5:
        break









