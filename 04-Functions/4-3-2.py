def area(a,b,c):
    import math
    s = 0.5*(a + b + c)
    a = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return a

print(area(5,12,13))
