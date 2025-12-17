arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

col1 = 0  
col2 = 4

for row in arr:
    row[col1], row[col2] = row[col2], row[col1]

# Wyświetlenie wyniku
for row in arr:
    print(row)

