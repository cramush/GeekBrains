def func(arg1, arg2, arg3):
    h = 0
    if arg1 > arg2 and arg2 < arg3:
        h = arg1 + arg3
        return h
    if arg1 < arg2 and arg1 < arg3:
        h = arg2 + arg3
        return h
    else:
        h = arg1 + arg2
        return h


print(f'Результат: {func(int(input("Введи первый аргумент: ")), int(input("Введи второй аргумент: ")), int(input("Введи третий аргумент: ")))}')


# def func2(a, b, c):
#     maxlist = sorted([a, b, c])
#     return maxlist[0] + maxlist[1]
