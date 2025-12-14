def f(n):

    i = 0
    j = 1

    if n == 1:
        k = 0
        
        return k
    
    if n == 2:
        k = 1

        return k
    
    if n == 3:
        k = 1

        return k

    while n > 2:
        k = i + j
        i = j
        j = k
        
        n -= 1

    return k

if __name__ == '__main__':
    print(f(5))
    print(f(9))