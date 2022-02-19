#Пользователь задаёт две строки. Определить количество вхождений одной строки в друго
from re import X

a = {1, 2, 3, 4}

print('first string ', a, end = "")
m = {8,5,4,2,3,6}
print()
print('second string ', m, end = "")
i = a.intersection(m)
print()
print('intersection of strings ',i)
