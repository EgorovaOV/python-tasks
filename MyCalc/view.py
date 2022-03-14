def calc_res(res):
    print('result is', res)
def get_value():
    return int(input('value = '))
def get_action():
    dictionary = {'+': 1, '-': 2, '*': 3, '/': 4}
    print('enter action +, -, /, *    ')
    ac = str(input())
    return (dictionary[ac])

