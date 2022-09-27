# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# k = int(input('Введите число k: '))
# result = 0
# summ = 0
# for i in range(1, k+1):
#     result = (1 + 1/i)**i
#     summ += result
#     print(round(result,2), end=' ')
# print('\n Cумма:', round(summ,2))

# Вариант 2 с использованием List Comperhension
k = int(input('Введите число k: '))
print('\n Cумма:', sum((1 + 1/i)**i for i in range(1, k+1)))