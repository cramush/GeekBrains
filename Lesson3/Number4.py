def func(x, y):
    res = 1
    for i in range(y):
        res = res * x
    return res


print("Результат: ", func(2, 3))
