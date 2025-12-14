def f(n):
    x = 0
    for i in range(1, n + 1):
       x = i + "" + i
    return x
if __name__ == "__main__":
    print(f(11))
    print(f(1234))
        
