'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
list = [random.randint(0, 15) for _ in range(int(input("Введите размер массива: ")))]
print (list)
min = int(input("Введите минимальное число диапазона:  "))
max = int(input("Введите максимальное число диапазона: "))
for i in range(len(list)):
    if min <= list[i] <= max:
       print (i, end = " ")

