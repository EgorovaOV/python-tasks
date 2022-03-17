#В файле находится N натуральных чисел, записанных через пробел.
#Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его
file = 'file_35.txt'
f = open(file, 'r')
data = f.read()
f.close()
print(data)
i = 0
num = []
while i < data.index('\n'):
    num.append(int(data[i]))
    i += 2
print(num)
j = 0
while j <= (len(num)-1):
    if num[j+1] - num[j] != 1:
        print('we find', num[j] + 1)
    j += 1





