def f(fnc,res):
    result = []
    for i in res:
        if fnc(i):
            result.append(i)
    wynik = sum(result)
    return wynik

if __name__ == "__main__":
    res = [3,7,10,2]
    fnc = lambda x:x>5
    print(f(fnc,res))