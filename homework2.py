# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите натуральное число N: '))
# result = 1
# for i in range(1,n+1):
#     result *= i
#     print(result, end=' ')

# Вариант 2
def fib(count):
    result = 1
    for e in range(1, count +1):
        result *= e
    return result

n = int(input('Введите натуральное число N: '))
# in_list = [fib(i) for i in range(1,n+1)]
in_list = [i for i in range(1,n+1)]
print(list(map(fib, in_list)))


