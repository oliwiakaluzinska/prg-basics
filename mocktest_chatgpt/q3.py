def f(d):
    total = 0
    for i in d:
        total += d[i]
    avr = total / len(d)
    result = 0
    for i in d:
        if d[i] < avr:
            result += 1
    return result

if __name__ == "__main__":
    print(f({'milk':4, "bread":6, "butter":10}))