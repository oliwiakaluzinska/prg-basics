arr = [2, 3, 2, 5, 8, 1, 9, 8]

for i in range(len(arr)):
    c = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            c += 1
    if c == 1:
        print(arr[i], end=" ")
