def f(player1, player2):
    sum1 = 0
    sum2 = 0
    special = {'A',"K",'Q',"J",'T'}
    for i in player1:
        if i in special:
            sum1 += 10
        else:
            sum1 += int(i)
    for j in player2:
        if j in special:
            sum2 += 10
        else:
            sum2 += int(j)
    
    if sum1 > sum2:
        return True
    else:
        return False
    
if __name__ == "__main__": 
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
    
    