def f(x, y):
    if x > 0 and y > 0:
        z = 1
        return z
    elif x < 0 and y > 0:
        z = 2
        return z
    elif x < 0 and y < 0:
        z = 3
        return z
    elif x > 0 and y < 0:
        z = 4
        return z 
if __name__ == "__main__":
    print(f(5,2))
    print(f(-5,2))
    print(f(-5,-2))
    print(f(5,-2))