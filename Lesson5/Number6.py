with open("File6.txt", "r") as file:
    new_dict = {}
    for line in file:
        hours = line.split()
        for i in range(1, 4):
            if hours[i] != "-":
                hours[i] = int(hours[i].rstrip("(лпраб)"))
            else:
                hours[i] = 0
        new_dict[hours[0].rstrip(":")] = sum(hours[1:])
    print(new_dict)
