def f(wartosc1, wartosc2):
    sum1 = 0
    sum2 = 0
    for i in wartosc1:
        if i in ("A","K","Q","J","T"):
            sum1 += 10
        else:
            sum1 += int(i)
    for j in wartosc2:
        if j in ("A","K","Q","J","T"):
            sum2 += 10
        else:
            sum2 += int(j)
    return sum1 >= sum2
if __name__ == "__main__": 
    print(f("9532","K8")) 