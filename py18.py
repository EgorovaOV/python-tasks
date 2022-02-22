#Реализовать алгоритм перемешивания списка.
import random

array = [1, 'Iam', 'dollar', 14, '$']
print(array)
list = []
i = len(array)-1
while 0<= i <= len(array):
        list.append(array[i])
        i-=1
print(list)
random.shuffle(array)
print(array)
random.shuffle(list)
print(list)




