arr = [[-38, 19], [5,40],[-7,11],[29,16]]

max = arr[0][0]
min = arr[0][0]
max_row = max_col = 0
min_row = min_col = 0

for i in range(len(arr)):          # indeks wiersza
    for j in range(len(arr[i])):   # indeks kolumny
        if arr[i][j] > max:
            max = arr[i][j]
            max_row = i
            max_col = j
        elif arr[i][j] < min:
            min = arr[i][j]
            min_row = i
            min_col = j

print("Max:", max, "Row:", max_row, "Column:", max_col)
print("Min:", min, "Row:", min_row, "Column:", min_col)