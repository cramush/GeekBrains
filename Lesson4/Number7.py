def fact(n):
    a = 1
    for i in range(1, n+1):
        a = i * a
        yield a


for i in fact(5):
    print(i)
