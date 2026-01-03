def f(x,y,n):
    for i in range(x, y+1):
        if i == n:
            j = True
        else:
            j = False
    return j 

if __name__ == "__main__":
    print(f(2,15,1))