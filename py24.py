#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным
# значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
a = [1.25, 10.255, 1.964, 3.47, 5.18]
import math
res = []
b = math.modf(a[0])
print(a)
i = 0
while i <= len(a)-1:
        res.append(math.modf(a[i]))
        i += 1
print(res)
j = 0
max = res[0][0]
min = res[0][0]
while j <= len(res)-1:
        if res[j][0] > max:
            max = (res[j][0])
        elif res[j][0] < min:
            min = (res[j][0])
        j += 1
print(max - min)











