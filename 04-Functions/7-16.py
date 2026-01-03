def f(n):
    number1 = 0
    number2 = 1
    for number3 in range(n-2):
        number3 = number1 + number2
        number1 = number2
        number2 =  number3
    return number3

if __name__ == "__main__":
    print(f(5))
    print(f(9))