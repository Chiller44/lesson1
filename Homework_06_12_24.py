def parni(x, y):
    m = [i for i in range(x, y) if i % 2 == 0]
    print(m)

parni(9, 20)

m = [25, 31, 1, 2, 33, 74, 15, 6, 7, 88, 19, 10, 3, 5, 13]
e = []
def w(m, x, y):
    for i in m:
        if i > x and i < y:
            e.append(i)
    print(e)

w(m, 5, 25)