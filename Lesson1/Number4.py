



a = int(input("Введи положительное целое число: "))
b = 0

while a > 0:
    if a % 10 > b:
        b = a % 10
    a = a // 10

print("Максимальная цифра в числе " + str(b))
