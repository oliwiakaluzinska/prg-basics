def f(palindrome):
    add = []
    for i in palindrome:
        add.append(i)
    
    while len(add)>1:
        if add[0] != add[-1]:
            return False
        del add[0]
        del add[-1]
    return True
        

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))