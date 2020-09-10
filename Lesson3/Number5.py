def sum():
    sum_res = 0
    end = False
    while end == False:
        number = input("Введи числа или введи $ для выхода: ").split()
        res = 0
        for i in range(len(number)):
            if number[i] == "$":
                end = True
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f"Текущая сумма: {sum_res}")
    print(f"Итоговая сумма: {sum_res}")


sum()
