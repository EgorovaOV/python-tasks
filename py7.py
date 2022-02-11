#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
a = int(input())
b = int(input())
c = int(input())
print((-(a or b or c)) == (-a and -b and -c))
