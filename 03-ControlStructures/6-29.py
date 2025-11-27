N = int(input("Enter the amount of prime numbers: "))
count = 0
number = 2
while count < N:
    # sprawdzamy czy 'number' jest pierwsza
    is_prime = True

    for i in range(2, number):
        if number % i == 0:   # jeśli dzieli się przez coś innego niż 1 i samą siebie
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        count += 1

    number += 1 