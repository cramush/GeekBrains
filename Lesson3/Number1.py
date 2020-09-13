def func(a, b):
    if b != 0:
        res = a / b
        return res
    else:
        print("На ноль делить нельзя.")


res = func(int(input("Введи первый аргумент: ")), int(input("Введи второй аргумент: ")))
print(f'Результат: {res}')
