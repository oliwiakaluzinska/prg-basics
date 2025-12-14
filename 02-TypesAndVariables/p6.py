def f(number,even):
    sum = 0
    
    if even == True:
        for i in number:
            i = int(i)
            if i % 2 == 0:
                sum += i

    if even == False:
        for i in number:
            i = int(i)
            if i % 2 != 0:
                sum += i
    
    return sum

if __name__ == '__main__':
    print(f('3124',True))
    print(f('3124',False))
    print(f('20576',False))