#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21
c = 15
def f(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
list1 = [f(c-k) for k in range(0, c+1)]
list = [-list1[j] for j in range(0, len(list1)-1)]
l = list + list1
l.sort()
print(l)


