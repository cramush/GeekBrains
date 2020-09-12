from itertools import count, cycle

# а) итератор, генерирующий целые числа, начиная с указанного.

def new_count(start, stop):
    for i in count(start):
        if i <= stop:
            print(i)
        else:
            break


new_count(start=int(input("enter start number: ")), stop=int(input("enter stop number: ")))

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

stop = 10
a = 0
my_list = (123, "ABC", True)

for i in cycle(my_list):
    if stop > a:
        print(i)
        a += 1
    else:
        break
