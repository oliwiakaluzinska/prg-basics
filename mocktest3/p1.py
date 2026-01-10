def f(word):
    arr = []
    for i in range(len(word)):
        tab = list(word)
        tab[i] = tab[i].upper()
        arr.append(''.join(tab))
    
    return '-'.join(arr)

print(f('water'))