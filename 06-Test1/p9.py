def f(size1,size2):
    x = "S"
    y = "M"
    z = "L"
    wielkosc = x < y < z
    if size1 == size2:
        n = 0
        return n
    elif size1  == z and size2 == y or size2 == x:
        n = 1
        return n
    elif size1 == x and size2 == y or size2 == z:
        n = 2
        return n
    
if __name__ == "__main__":
    print(f("L","S"))
    print(f("M","L"))
    print(f("S","S"))