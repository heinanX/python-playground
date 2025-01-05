is_female = True
is_comedian = True
is_fun = False

""" simple if else """
if is_female:
    print('she\'s female, folks!')
else:
    print('she\'s not female, folks!')

""" if x or x """
if is_female or is_comedian:
    print('it\'s true, folks!')
else:
    print('it\'s false, folks!')

""" if x and x """
if is_fun and is_comedian:
    print('they are a fun comedian, folks!')
else:
    print('they\'re neither, folks!')

""" if x and x, if else, else """
if is_fun and is_comedian:
    print('they are a fun comedian, folks!')
elif is_comedian and not(is_fun):
        print('they are a comedian but not fun, folks!')
else:
    print('they\'re neither, folks!')

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num1 >= num1 and num2 >= num3:
        return num1
    else:
        return num3
    
print(max_num(5,7,79))