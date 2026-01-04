arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == j:
            arr[i][j] = 1

for i in arr:
    print(i)