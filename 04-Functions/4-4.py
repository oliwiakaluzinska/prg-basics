import math


def sum_digits(number):
    if number < 0:
       number = abs(number)
    number = str(number)
    sum_number = 0
    for i in number:
        digit = int(i)
        sum_number += digit
    return sum_number

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')