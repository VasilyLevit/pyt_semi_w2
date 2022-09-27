# Реализуйте алгоритм перемешивания списка. (свой рандомайз)

import random
n = 10

# list_in = list(range(n))
# list_out = []
# length_list = len(list_in)

# print('List input =', list_in)

# for i in range(length_list):
#     num_rand = random.choice(list_in)
#     list_out.append(num_rand)
#     list_in.remove(num_rand)
# print('List output =', list_out)

# Вариант 2 - с использованием фукции
def mix(list_in):
    for i in range(len(list_in)):
        num_rand = random.choice(list_in)
        list_out.append(num_rand)
        list_in.remove(num_rand)
    return list_out

list_in = list(range(n))
list_out = []

print('List input =', list_in)
print('List output =', mix(list_in))