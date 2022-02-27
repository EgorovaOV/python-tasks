#Найти НОК двух чисел
y = 36
x = 72
print('Y', y,'X', x)
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
print('prime factors of Y', f(y))
print('prime factors of X', f(x))
a = f(x)
b = f(y)
c = []
i =0
j = 0
for i in a:
    for j in b:
       if i == j:
           if i in c:
              continue
           else:
              c.append(i)
print(c)
p = 0
pr = 1
while p in range(len(c)):
    pr = pr*c[p]
    p += 1
print('NOD = ', pr)
print('NOK = ', (x * y)/pr)
















