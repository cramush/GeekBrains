with open("File3.txt", "r") as file:
    sal = []
    name = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            name.append(i[0])
        sal.append(i[1])

print(f"Меньше 20000: {name} \nСредний: {sum(map(int, sal)) / len(sal)}")
