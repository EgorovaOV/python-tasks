#Определить, присутствует ли в заданном списке строк, некоторое число
list1 = '1 2 3 4 5 6'.split()
list2 = [5, 'u', 44, '$$']

print(list1)
print(list2)
a = str(input())
print(a)
if a in list1:
    print('ok')
elif a in list2:
    print('ok')
else:
    print('not ok')

