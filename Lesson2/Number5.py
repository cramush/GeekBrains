line = []

for i in range(7):
    line.append(int(input("Заполни рейтинг: ")))

print("Полученный рейтинг: ", line)
element = int(input("Введи новый элемент рейтинга: "))
line.append(element)
line.sort(reverse=True)
print("Новый вид рейтинга: ", line)
