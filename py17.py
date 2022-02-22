#Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число

parth = r'C:\Users\Ольга\Desktop\Документы Егорова О.В\ГИИКбрейнс\Знакомство с Python\for py17.txt'

n = int(input())
list = [n for n in range(-n,n+1)]
print(list)
f = open(parth, 'r')
list1 = f.read()
x=[]
while True:
    line = line.rstrip('\n')
    index = f.readline()
    #line = line.rstrip('\n')
    index = int(index)
    x.append(list[index])
    if not index:
        break
print(x)
m=0
i=0
while i in range(0, len.x+1):
          m= x[i]*x[i+1]
          print(m)    




