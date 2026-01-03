def f(n):
    add = []
    while n > 1:
        add.append('*/')
        n -= 1
    if n == 1:
        add.append('*')

    return ''.join(add)

if __name__ == "__main__":
    print(f(4))
    print(f(1))