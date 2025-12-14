def f(speed1,speed2):
    speed1 = (speed1 *1000)/ 3600
    if speed1 == speed2:
        x = True
        return x
    else:
        x = False 
        return x
if __name__ == "__main__":
    print(f(36,10))
    print(f(20,20))