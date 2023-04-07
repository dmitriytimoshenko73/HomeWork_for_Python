import random 
n = random.randint (100, 999)  
print ('Случайное число =' , n)
a =  n//100
b =  n//10%10
c = n%10
print ('Сумма цифр числа =', a+b+c)