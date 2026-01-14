def f(d):
    total = 0
    for i in d:
        total += d[i]
    avr = total / len(d)
    
    result = 0
    for j in d:
        if d[j] > avr:
            result += 1
    return result

if __name__ == "__main__": 
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))