# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. (потребуется сплит)

n = 5

num_string = input('Введите 2а числа через пробел: ')
list_num = num_string.split(' ', 1)

for i in range(n):
    numbers = list(range(-n, n+1))
arg_1 = numbers[int(list_num[0])]
arg_2 = numbers[int(list_num[1])]
print(numbers)
print(arg_1*arg_2)