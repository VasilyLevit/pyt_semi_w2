# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. (потребуется сплит)

n = 5
for i in range(n):
    numbers = list(range(-n, n+1))

print(numbers)