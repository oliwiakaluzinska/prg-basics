arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

for i in arr1:
    x = False
    for j in arr2:
        if i == j:
            x = True
            break
    if not x:
        print(i, end=" ")