dictionary = {'+' : 1,'-' : 2,'*' : 3,'/' :4}
print(dictionary)
print('+')

print('enter action +, -, /, *    ')
ac = str(input())
print(ac)
print(dictionary[ac])
print(type(dictionary[ac]))
