arr1 = [5,4,36]
arr2 = [4,36,12,28,9,44,5]
count = 0

for i in arr1:
    for j in arr2:
        if i == j:
            count += 1
if count < len(arr1):
    print(False)
else:
    print(True)
