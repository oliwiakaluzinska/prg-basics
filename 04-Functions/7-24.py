def f(expression):
    result = 0
    sign = 1
    for ch in expression:
        if ch == '+':
            sign = 1
        elif ch == '-':
            sign = -1
        else:  # cyfra
            result += sign * int(ch)
    return result
    
if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))