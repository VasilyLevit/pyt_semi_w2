# Напишите программу, в которой пользователь будет задавть две строки, а программа - определять количество вхождений одной строки в другую.

main_string = 'Уж небо осенью дышало, Уж реже солнышко блистало, Короче становился день, Лесов таинственная сень'
find_string = 'нь'

# первый способ
print(main_string.count(find_string))

# второй способ
count = 0
len_fstring = len(find_string)
for i in range(len(main_string)-len_fstring+1):
    
    if (main_string[i:i+len_fstring]) == find_string:
        count += 1
        
print(count)