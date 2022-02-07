#По двум заданным числам проверить является ли одно квадратом второг
from socket import if_indextoname


print("Enter a")
a = int (input())
print("Enter b ")
b = int (input())
if(a**2 == b):
    print('a is square of b')
elif(b**2==a):
     print('b is square of a')
else:
    print('none of numbers is square of other')

