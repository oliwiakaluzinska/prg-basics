arr = [ [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0] 
        ]

for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][j] = (i+1) * (j+1)
print(arr)