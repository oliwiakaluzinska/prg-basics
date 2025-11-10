number1 = input ('Enter number 1: ')
number2 = input ('Enter number 2: ')
operator = input ('Enter operator (+, -, *, /): ')
result = 0

if operator == '+':
    result = int(number1) + int(number2)
elif operator == '-':
    result = int(number1) - int(number2)
elif operator == '*':
    result = int(number1) * int(number2)
elif operator == '/':
    result = int(number1) / int(number2)

print(f'{number1} {operator} {number2} = {result}')