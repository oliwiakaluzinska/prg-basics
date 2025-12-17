def transpose_matrix(m):
    t = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        t.append(row)
    return t


arr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
]
print(transpose_matrix(arr1))