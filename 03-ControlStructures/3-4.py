x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if not x < 0 or not y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
elif not x > 0 and not y > 0:
    print('Both of the numbers are negative')
elif x == 0 and y == 0 :
    print('Both numbers are zero')