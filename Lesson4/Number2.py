list1 = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список: ", list1)
list2 = [el for i, el in enumerate(list1) if list1[i - 1] < list1[i]]
print("Новый список: ", list2)
