with open("File5.txt", "w+") as file:
    line = input("Введи цифры через пробел: ")
    file.writelines(line)
    num = line.split()

with open("File5.txt", "r") as file:
    res = [int(i) for i in file.read().split()]
    summ = sum(res)
    print("Сумма чисел: ", summ)
