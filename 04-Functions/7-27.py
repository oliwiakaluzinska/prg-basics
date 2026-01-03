def f(product_code):
    i = 0
    suma = 0
    while i < len(product_code) - 1:
            suma += int(product_code[i])
            i += 1

    if suma % 7 == int(product_code[-1]):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114") )
    print(f("7071"))