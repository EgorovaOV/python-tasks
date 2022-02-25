#Найти корни квадратного уравнения Ax² + Bx + C = 0
#Математикой
#Используя дополнительные библиотеки*

print('enter first multiplier', end = ' ')
a = int(input())
print('enter second multiplier', end = ' ')
b = int(input())
print('enter free term of the equation', end = ' ')
d = int(input())
print(b**2 - 4*a*d)
if b**2 - 4*a*d < 0:
    print('equation has no roots')
else:
    print((-b + (b**2 - (4*a)*d)**0.5) / 2*a)
    print((-b + (b ** 2 + (4 * a) * d) ** 0.5) / 2 * a)
import cmath

a = 8
b = 6
c = 14

# Вычисляем дискриминант
dd = (b**2) - (4*a*c)
print(cmath.sqrt(dd))

# Ищем корни
sol1 = (-b-cmath.sqrt(dd))/(2*a)
sol2 = (-b+cmath.sqrt(dd))/(2*a)

print('Корень 1 равен:', sol1,'Корень 2 равен: ',sol2)



