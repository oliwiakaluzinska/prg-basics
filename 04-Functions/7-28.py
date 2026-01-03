def f(dice):
    number = 0
    for i in range(len(dice)):
        for j in range(len(dice)):
            if i == j+1 and dice[i]==dice[j]:
                number = dice[i]

    return number

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))