#Вычислить число пи  c заданной точностью d
 #   Пример: при d = 0.001,  = 3.141. 10-1d10-10
import math
n = 6
print(' pi: {:.30f}'.format(math.pi))
a = math.pi
b = round(a,n+1)*10**n
c = math.modf(b)
a = c[1] / 10**n
print(a)








