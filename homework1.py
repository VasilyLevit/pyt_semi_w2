# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 0,56 -> 11

num = str(0.56)
summ = 0

for i in range(len(num)):
    if num[i].isdigit():
        summ += int(num[i])    

print(num, ' -> ', summ)