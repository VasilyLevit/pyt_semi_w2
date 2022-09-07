# Для натурального n создать последовательность 3n+1

n = int(input('Введите число N: '))

for i in range(1,n+1):
    elem = 3 * i + 1
    print(elem, end=' ')    