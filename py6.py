#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным
print('input number day of week')
a = int(input())
if ((a<0) or a>7):
    print('wrong number')
elif (a == 6):
    print('saturday is weekend')
elif (a ==7):
    print('sunday is weekend')
else:
    print('sorry')







