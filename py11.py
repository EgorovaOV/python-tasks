#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81
print('enter N')

a = int(input())
n = [0]*a
print(n)
for i in range(len(n)):
    i = str(i + 1)
    print("Введите элемент массива " + i, end = " ")#С клавиатуры вводятся все элементы массива
    i = int(i)
    i = i - 1
    n[i] = int(input())
for i in range(len(n)):    
     print(n[i], end = " ") 
 #Чтобы элементы массива выводились в одну строку через пробел,
 #  используем параметр end =" " в операторе вывода на экран print(a[i], end = " ")       
