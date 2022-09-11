# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. (потребуется сплит)

n = 10
numbers = list(range(-n, n+1))
print('N =', numbers)

num_string = input('Введите числа от 0 до 10 через пробелы: ')
positions = num_string.split(' ')

mult = 1
for i in positions:
    mult *= numbers[int(i)]
   
print('Произведение: {}'.format(mult))