f = open("File1.txt", 'w')
while True:
    s = input("Введи данные: ")
    if s == '':
        break
    f.write(s + '\n')
f.close()

f = open("File1.txt", "r")
print(f.read())
f.close()
