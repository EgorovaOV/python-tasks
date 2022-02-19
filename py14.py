#Подсчитать сумму цифр в вещественном числе
i = int(input())
if i < 0:
    i*=-1
sum = 0
while i % 10 > 0:
    sum = sum + i % 10
    i = i//10   
print(sum)
