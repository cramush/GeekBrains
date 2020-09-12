import random


random_list = [random.randint(0, 50) for i in range(30)]
print("Исходный список: ", random_list)

# random_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = [el for el in random_list if random_list.count(el) < 2]
print("Новый список: ", new_list)
