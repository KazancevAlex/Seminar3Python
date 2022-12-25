# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

list = [1, 2, 3, 4, 5, 6, 7, 8]
import math 
size = math.ceil(len(list)/2)
print(f"Начальный список: {list}")
list2 = []
for i in range(size):
    list2.append(list[i]*list[-i - 1])
print(f"Список с произведением пар чисел первого списка(первый элемент умножается на последний и т.д.): {list2}")