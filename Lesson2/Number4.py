line = str(input("Введи строку из нескольких слов через пробел: "))
number = 0
words = line.split(" ")

for word in words:
    number += 1
    print(f"{number} {word [0:10]}")

