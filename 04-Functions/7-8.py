def f(amount_to_pay):
    suma = amount_to_pay // 5
    reszta = amount_to_pay % 5
    suma += reszta // 2
    reszta = reszta % 2
    suma += reszta
    return suma

if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(0))
