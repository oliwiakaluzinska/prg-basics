def f(name):
    name = str(name)
    add2 = []
    add1 = name.split(" ")
    for i in add1:
        add2.append(i[0])
    
    return ''.join(add2)


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
