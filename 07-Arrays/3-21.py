arr1 = [1,5,3,7]
arr2 = [1,2,3,4,5,6,7]

x = True
for i in arr1:
    if i not in arr2:
        x = False
        break
if x:
    print("True")
else:
    print("False")