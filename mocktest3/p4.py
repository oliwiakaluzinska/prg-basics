def f(fnc,res):
    arr = []
    for i in res:
        if fnc(i):
            arr.append(i)
    maximum = max(arr)
    minimum = min(arr)

    return maximum-minimum

res = [95,90,20,50,70]
fnc1 = lambda x: x>50
print(f(fnc1,res))