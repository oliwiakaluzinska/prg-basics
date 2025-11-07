number1 = input ('Enter number 1: ')
number2 = input ('Enter number 2: ')
operator = input ('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2

print(f'{number1} {operator} {number2} = {result}')