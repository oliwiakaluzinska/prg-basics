def f(n):
    return lambda x:x-n

if __name__ == "__main__":
    minus = f(5)
    print(minus(12))