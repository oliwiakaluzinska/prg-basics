def f(number, tuple):
    c = 0
    for i in tuple:
        if i == number:
            c += 1
    return c
    
t = (50,20,40,50,30,50)
print(f(50,t))