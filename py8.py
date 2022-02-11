#Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
from math import e


print('enter x')
x = int(input())
print('enter y')
y = int(input())
if (x > 0 and y > 0):
    print('point is in first quater')
elif (x > 0 and y < 0):
    print('point is in second quater')
elif (x < 0 and y < 0):
    print('point is in third quater')    
else: 
    print('point is in fourth quater')   