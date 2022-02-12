#Найти расстояние между двумя точками пространства

print('enter coordinates of a')
xa = int(input())
ya = int(input())
za = int(input())
print('enter coordinates of b')
xb = int(input())
yb = int(input())
zb = int(input())
import math
print('distance between  a and b is ',math.sqrt(((xb-xa) **2 + (yb-ya)**2 + (zb-za)**2)))