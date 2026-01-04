arr = [2, 3, 2, 5, 8, 1, 9, 8]
arr2 = []
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    if count == 1:
        arr2.append(arr[i])
print(arr2)