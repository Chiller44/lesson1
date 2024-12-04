import random

def neparni(x, y):
    m = [i for i in range(x, y) if i % 2 != 0]
    print(m)

neparni(1,30)