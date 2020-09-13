from functools import reduce
from common import prod

list1 = list(range(100, 1001))
list2 = [el for el in list1 if el % 2 == 0]
print(f'Исходный список: {list2}')

product = reduce(prod, [el for el in list1 if el % 2 == 0])
print(f'Произведение: {product}')
