#Составить список простых множителей натурального числа N
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
x = int(input())
print(f(x))