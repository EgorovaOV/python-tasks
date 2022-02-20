#Задать список из n чисел последовательности (1+1/n)в степени n и вывести на экран их сумму
print('enter n ', end = ' ')
n = int(input())
def f(x):
    return round((1+1/x)**x, 2)
list = [f(n) for n in range(1,n+1)]  
print(list)  
sum = 0
for n in range(n):
    sum = sum + list[n]
print(sum)