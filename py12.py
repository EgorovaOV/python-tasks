#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from audioop import add


print('enter n',end = " ")
n = int(input())
dictionary = {}
dictionary = \
   #{
   #(n - n + 1)  : (3 * n +1)
    #}
for i in range(n):
    i = (n-n+1) 
    dictionary[(i) : (3*i+1)]


print(dictionary)    