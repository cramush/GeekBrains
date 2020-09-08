month = int(input("Введи номер месяца: "))

year = {
    "Зима": (1, 2, 12),
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 11)
}

for key in year.keys():
    if month in year[key]:
        print("Это время года: ", key)
