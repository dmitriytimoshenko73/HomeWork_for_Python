'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X.

*Пример:*

5
    7 -2 3 5 1
    
    -> 1 '''

import random 
n = int(input("Введите количество элементов в массиве: "))
a = [random.randint(1, 10) for i in range(n)]
print("Массив A:", a)

X = int(input('Введите число X, которое необходимо найти в списке: '))
count = 0
for i in a:
    if i == X:
       count += 1
print(f'Число {X} встречается в списке А {count} раз(а)') 