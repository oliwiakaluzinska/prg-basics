def sum_digits(number):
    number = abs(number)
    number = str(number)
    
    sum = 0
    for i in number:
        i = int(i)
        sum += i
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')