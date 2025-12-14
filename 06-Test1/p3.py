def f(product_code):
    product_code = str(product_code)
    n1 = int(product_code[0])
    n2 = int(product_code[1])
    n3 = int(product_code[2])
    n4 = int(product_code[3])
    if (n1+ n2 + n3) % 7 == n4:
        x = True
        return x
    else:
        x = False
        return x
if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))