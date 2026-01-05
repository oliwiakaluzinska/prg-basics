arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
]

arr[0],arr[-1] = arr[-1],arr[0]

for i in arr:
    for j in i:
        print(j, end=" ")
    print()