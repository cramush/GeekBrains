elements = []
for i in range(7):
    answer = input("Заполни список: ")
    elements.append(answer)

print("Полученный список: ", elements)

i = 0
while i+1 < len(elements):
    t = elements[i+1]
    elements[i+1] = elements[i]
    elements[i] = t
    i += 2

print("Полученный список: ", elements)
