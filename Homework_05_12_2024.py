import time

#Завдання 4
def my_decor(func):
    def wrapper():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return wrapper

@my_decor
def parni():
    m = [i for i in range(100000) if i % 2 == 0]
    print(m)

parni()

#Завдання5
def my_decor2(func):
    def wrapper(x, y):
        start_time = time.time()
        func(x, y)
        print(time.time() - start_time)
    return wrapper

@my_decor2
def parni(x, y):
    m = [i for i in range(x, y) if i % 2 == 0]
    print(m)

parni(3, 500)
