# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. (потребуется сплит)

n = 10

num_string = input('Введите 2а числа от 0 до 10 через пробел: ')
list_num = num_string.split(' ', 1)

for i in range(n):
    numbers = list(range(-n, n+1))
elem_1 = numbers[int(list_num[0])]
elem_2 = numbers[int(list_num[1])]
mult = elem_1 * elem_2
print('N =',numbers)
print('N[{}] * N[{}] = {}'.format(list_num[0], list_num[1], mult))