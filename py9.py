#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
print('enter a number of quater')
a = int(input())
if (1 <= a <= 4):
    if a == 1:
          print('number of quater is first')
    elif a == 2:
          print('number of quater is second')
    elif a == 3:
          print('number of quater is third')
    elif a == 4:
          print('number of quater is fourth')     
else:
    print('number of quater is wrong')
