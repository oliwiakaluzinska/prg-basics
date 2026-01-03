def f(binary_number):
    sum = 0
    for i in binary_number:
        if i == '0' or i == '1':
            sum+=1
    
    if sum == len(binary_number):
        i = True
    else:
        i = False

    return i

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))