#Найти максимальное из пяти чисел
list = [10, 2, 3 ,4, 5]
print(list)
maxx = (list[0])
i = 0
while i<len(list):
        if list[i]>maxx:
           maxx=(list[i])
        else:
            i+=1

print(maxx)
    


