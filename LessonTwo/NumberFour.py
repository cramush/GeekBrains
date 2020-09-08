line = str(input("Введи строку из нескольких слов через пробел: "))
word = []
number = 0

for i in range(line.count(' ') + 1):
    word = line.split()
    if len(str(word)) <= 10:
        number += 1
        print(f"{number} {word[i]}")
    else:
        number += 1
        print(f"{number} {word[i] [0:10]}")



