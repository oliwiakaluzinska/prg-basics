arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

arr[0], arr[2] = arr[2], arr[0]

for i in arr:
    print(i)
