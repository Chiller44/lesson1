#Завдання1
ryadok = input('Введіть рядок: ')
ryadok_1 = ryadok.replace(' ', '').lower()
ryadok_2 = ryadok[::-1].replace(' ', '').lower()
if ryadok_1 == ryadok_2:
    print('Рядок э паліндром.')
else:
    print('Рядок не є паліндромом.')

#Завдання2
#буде працювати некоректно, якщо в початковому тексті є кома, лапки...
#split працює з одним значенням, в мене це пробіл
#наприклад, в такому: Usually under a “Redeem Code” section or similar.

text = input('Введіть текст: ')
reserved_words = input('Введіть зарезервованы слова: ').split(', ')
for word in text.split():
    if word.lower() in reserved_words:
        text = text.replace(word,word.upper())
print(text)

#Завдання3
text = ('Хазяйнує у лісі зима. Заховала маленьку ялиночку у сніг.'
        'А вона визирає зеленою гілочкою. Бо їй цікаво, що тут робиться. '
        'Ось пройшла шнурком хитра лисичка. Пролетіла ворона. З гілки на гілку майнула білочка. '
        'Як цікаво й біло! Сидить ялиночка під снігом і спостерігає.')
print('Кількість пропозицій в тексті: ', text.count('.') + text.count('!') + text.count('?'))



