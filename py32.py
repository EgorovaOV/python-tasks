#Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
a = [1, 2, 3, 4, 5, 5, 6, 6, 8, 2, 9, 7, 7, 8]
i = a[0]
c = []
for i in a:
    if i in c:
       continue
    else:
       c.append(i)
print(c)