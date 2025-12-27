N = int(input('Enter the amount of prime numbers: '))
number = 2
count = 0
while count < N:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number, end=" ")
        count += 1
    number += 1
    