def f(n):
    add = []
    for i in range(1, n+1):
        add.append(str(i))

    return ''.join(add)

if __name__ == "__main__":
    print(f(11))
    print(f(4))