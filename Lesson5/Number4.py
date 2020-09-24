num = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять"
       }

with open("File4.1.txt") as file, open("File4.2.txt", "w") as res:
    lines = [line.split() for line in file]
    new_lines = [[num[i[0]], i[1], i[2]] for i in lines]
    for i in new_lines:
        res.writelines(" ".join(i) + "\n")
