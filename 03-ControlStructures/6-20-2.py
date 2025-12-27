decimal = int(input('Enter the decimal number: '))
remainder = []
while decimal != 0:
    remainder.append(decimal % 2)
    decimal = decimal // 2
remainder.reverse()
for i in remainder:
    print(i, end='')