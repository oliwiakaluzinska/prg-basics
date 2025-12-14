def f(n):
    suma = 0
    if n == 0:
        return 0
    elif n > 0:
        suma = (n-1) + (n-2)
    return suma
if __name__ == '__main__':
    print(f(5))