#В файле находится N натуральных чисел, записанных через пробел.
#Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его
file = 'file_35.txt'
f = open(file, 'r')
data = f.read()
f.close()
num = []
while data != ' ':
    position = data.index(' ')
    num.append(int(data[:position]))
    data = data[position+1:]
print(num)


