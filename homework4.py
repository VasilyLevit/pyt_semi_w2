# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. (потребуется сплит)

# Вариант 1
# n = 10
# numbers = list(range(-n, n+1))
# print('N =', numbers)
# num_string = input('Введите числа от 0 до 10 через пробелы: ')
# positions = num_string.split(' ')
# result = 1
# for i in positions:
#     result *= numbers[int(i)]
# print('Произведение: {}'.format(result))

# Вариант 2 - с использованием функций
# def mult_pos(numbers, pos):
#     result = 1
#     for i in pos:
#         result *= numbers[int(i)]
#     return result
# n = 10
# numbers = list(range(-n, n+1))
# print('N =', numbers)
# num_string = input('Введите числа от 0 до 10 через пробелы: ')
# positions = num_string.split(' ')

# print('Произведение: {}'.format(mult_pos(numbers, positions)))

# Вариант 3 - с использованием передачи функций в качестве аргумента
def mult_pos(fun_gen, pos, n):
    result = 1
    numbers = fun_gen(n)
    for i in pos:
        result *= numbers[int(i)]
    return result

def list_gen(n):
    numbers = list(range(-n, n+1))
    return numbers

n = 10
print('N =', list_gen(n))
positions = input('Введите числа от 0 до 10 через пробелы: ').split(' ')

print('Произведение: {}'.format(mult_pos(list_gen, positions, n)))