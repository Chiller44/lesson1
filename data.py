month_of_year  = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

x1 = input("Введіть число в форматі 'ДД' початку інтервалу: ")
x2 = input("Введіть місяць в форматі 'ММ' початку інтервалу: ")
x3 = input("Введіть ріл в форматі 'РРРР' початку інтервалу: ")
y1 = input("Введіть число в форматі 'ДД' кінця інтервалу: ")
y2 = input("Введіть місяць в форматі 'ММ' кінця інтервалу: ")
y3 = input("Введіть рік в форматі 'РРРР' кінця інтервалу: ")

def days_between_dates(x1, x2, x3, y1, y2, y3):
    if len(x1) != 2 or len(x2) != 2 or len(x3) != 2 or len(y1) != 2 or len(y2)!= 2 or len(y3) != 2:
        print('Введіть двту в вірному форматі!')
    else:
        if int(x3) == int(y3):
            month_days = 0
            for i in range(int(x2) + 1, int(y2)):
                month_days += month_of_year.get(i)
            year_days = month_days + (month_of_year.get(int(x2)) - int(x1)) + int(y1)
            print(year_days)

        if int(x2) > int(y2):
            month_days = 0
            for i in range(int(x2) + 1, 13):
                month_days1 += month_of_year.get(i)
            print(month_days)









days_between_dates(x1, x2, x3, y1, y2, y3)





