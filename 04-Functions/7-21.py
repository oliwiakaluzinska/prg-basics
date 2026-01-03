def f(number1,number2,number3):
    max = 0
    min = 0
    if number1 > number2 and number1 > number3:
        max =  number1
    elif number2>number1 and number2>number3:
        max = number2
    elif number3>number1 and number3>number2:
        max = number3

    if number1 < number2 and number1 < number3:
        min =  number1
    elif number2<number1 and number2<number3:
        min = number2
    elif number3<number1 and number3<number2:
        min = number3

    return max - min

if __name__ == "__main__":
    print(f(7,4,9))
    print(f(2,12,8))