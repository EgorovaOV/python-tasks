#Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
list = ['qwe', 'asd', 'zxc', 'poi', 'lkj', 'qwe', 'asd', 'zxc', 'poi', 'lkj', '1', '1']
print(list)
print(len(list))
i=0
print('enter pos to find ', end = ' ')
j = str(input())
list2 = [(i, list[i]) for i in range(len(list)) if list[i] ==j]
print(list2)
if len(list2) >= 2:
    print(list2[1])
else:
    print(-1)




