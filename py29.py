#Найти НОК двух чисел
y = 164
x = 14
print('num', x,'num2', y)
def f(a):
   b =[]
   i = 2
   while i in range(2, 10):
         while a % i == 0:
            b.append(i)
            a = a/i
         i += 1
   if a % i != 0:
       if a != 1:
            b.append(a)
   return(b)
print('prime factors of num1', f(y))
print('prime factors of num2', f(x))
a = f(x)
b = f(y)
c = []
if (all(n in a for n in b)):
    c = a
elif (all(n in b for n in a)):
    c = b
else:
    for i in a:
        if i in c:
            continue
        for j in b:
            if i == j:
                c.append(i)
                break
p = 0
pr = 1
while p in range(len(c)):
    pr = pr*c[p]
    p += 1
print('NOD = ', pr)
print('NOK = ', (x * y)/pr)
















