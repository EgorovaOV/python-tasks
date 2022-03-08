#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
k = 2
import random
a = random.randint(1, 100)
print(a)
b = random.randint(0, 100)
print(b)
c = random.randint(0, 100)
print(c)
#pip install sympy
#from sympy import *
x = Symbol('x')
d = a * x **k + b * x + c
print(d)
with open('file.txt', 'w') as d:
     d.write('a * x **k + b * x + c')
