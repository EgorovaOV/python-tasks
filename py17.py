#Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число


from unicodedata import digit


parth = r'C:\Users\Ольга\Desktop\Документы Егорова О.В\ГИИКбрейнс\Знакомство с Python\for py17.txt'

n = int(input())
list = [n for n in range(-n,n+1)]
print(list)
f = open(parth, 'r')
x=[]
while True:
    index = int(f.readline())
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
f.close

m=0
while i in range(0, len.n+1):
    m= n[i]*n[i+1]



