num1 = float(input('enter a number: '))
operator = input('enter operator: ')
num2 = float(input('enter another number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else: print('Invalid operator')