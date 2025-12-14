def f(a,b):
    sum = 0
    for x in range(a,b + 1):
        if x % 3 == 0:
            sum = sum + x
    return sum
if __name__ == "__main__":
    print(f(1,6))
    print(f(2,10))
