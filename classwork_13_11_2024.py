def stepen(a, n):
    if n == 0:
        return 1
    return a * stepen(a, n - 1)

print(stepen(2, 4))

def sum(a, b):
    if a > b:
        return 0
    return a + sum(a + 1, b)

print(sum(4, 3))

def mal(a):
    if a < 0:
        return
    print("*",end=' ')
    mal(a-1)


mal(9)