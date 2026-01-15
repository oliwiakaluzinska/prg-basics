def f(x,y,d):
    n = 0
    for i in range(x,y+1):
        if str(i) == d:
            n = 1
    if n == 1:
        return True
    else:
        return False
        
if __name__ == "__main__":
    print(f(10,15,"14")) 
    print(f(100,120,"11"))
    print(f(205,210,"04"))