def func(x, y):
    res = 1
    for i in range(abs(y)):
        res = res * x
    return 1 / res


print("Результат: ", func(2, -3))
