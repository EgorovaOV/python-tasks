#Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
import math
a = [2, 4, 6, 8, 10]
b = []
i = -1
j = 0
y = math.ceil(len(a)/2)

print(a)
while -len(a) <= i < y and 0 <=j < y:
    b.append(a[i]*a[j])
    i -= 1
    j += 1
print(b)



