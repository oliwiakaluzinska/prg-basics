def f(n):
    count = 0      
    number = 1    

    while count < n:
        number += 1
        is_prime = True

        if number < 2:
            is_prime = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

        if is_prime:
            count += 1

    return number

if __name__ == "__main__":
    print(f(1))
    print(f(5))