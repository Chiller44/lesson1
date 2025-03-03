FILENAME = 'message.txt'

def write():
    message = input('Enter str: ')
    with open(FILENAME, 'a') as file:
        file.write(message)

def read():
    with open(FILENAME, 'r') as file:
        for i in file:
            print(i, end='')


while True:
    selection = input('1. Write file\t\t2.Read file\t\t3.Exit\nChoise number: ')
    if selection == '1' or selection.lower().startswith('wr'):
        write()
    elif selection == '2' or selection.lower().startswith('read'):
        read()
    elif selection == '3' or selection.lower().startswith('exit'):
        break
    else:
        print('Incorrect command')