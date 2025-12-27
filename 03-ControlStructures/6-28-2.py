number1 = 0
number2 = 1
i = 0
print(number1,number2, end=" ")
while i < 18:
    number3 = number1 + number2
    print(number3 , end=" ")
    number1 = number2
    number2 = number3
    i += 1