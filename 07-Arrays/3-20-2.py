arr = [7,9,2,4,5,6]
arr2 = []

for i in arr:
    if i % 2 == 0:
        arr2.append(i)
for i in arr:
    if i%2 != 0:
        arr2.append(i)

print(arr2)