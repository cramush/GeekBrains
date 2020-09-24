f = open("File2.txt")
line = 0

for i in f:
    line += 1
    flag = 0
    word = 0
    for n in i:
        if flag == 0 and n != " ":
            word += 1
            flag = 1
        elif n == ' ':
            flag = 0
    print(i, f" Символов: {len(i)-1} Слов: {word}")

print(f"Строк: {line}")
f.close()
