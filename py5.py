#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
a = int(input())
print('statmet is')
print((((a % 10) == 0) or ((a % 15) == 0)) and ((a % 30) != 0))
        
        

