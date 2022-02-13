#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
#a = int(input())
#b = int(input())
#c = int(input())
#print((-(a or b or c)) == (-a and -b and -c))

x, y, z = [True, False], [True, False], [True, False]
i = 0

print((not(x[i] or y[i] or z[i])) == (not x[i] and not y[i] and not z[i])) 
print((not(x[i-1] or y[i] or z[i])) == (not x[i-1] and not y[i] and not z[i]))
print((not(x[i-1] or y[i-1] or z[i])) == (not x[i-1] and not y[i-1] and not z[i]))
print((not(x[i-1] or y[i-1] or z[i-1])) == (not x[i-1] and not y[i-1] and not z[i-1]))
print((not(x[i] or y[i-1] or z[i-1])) == (not x[i] and  not y[i-1] and not z[i-1]))
print((not(x[i] or y[i] or z[i-1])) == (not x[i] and not y[i] and not z[i-1]))
print((not(x[i] or y[i-1] or z[i])) == (not x[i] and not y[i-1] and not z[i]))
print((not(x[i] or y[i-1] or z[i-1])) == (not x[i] and not y[i-1] and not z[i-1]))
print((not(x[-1] or y[i] or z[i-1])) == (not x[i-1] and not y[i] and not z[i-1]))