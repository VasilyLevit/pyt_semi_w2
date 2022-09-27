# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

num = str(1.56)
# summ = 0

# for i in range(len(num)):
#     if num[i].isdigit():
#         summ += int(num[i])    
# print(num, ' -> ', summ)

# Вариант 2 - с использованием List Comperhansion
print(num, ' -> ', sum(int(num[i]) for i in range(len(num)) if num[i].isdigit()))