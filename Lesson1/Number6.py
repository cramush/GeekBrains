



a = input("Введи результат первого дня: ")
b = input("Введи общий результат: ")

a = int(a)
b = int(b)
days = 1

while a < b:
    a += a * 0.1
    days += 1

days = str(days)

print("Номер дня: " + days)