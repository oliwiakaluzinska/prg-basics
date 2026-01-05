number = int(input('Enter the number: '))

count = 0
arr = [7,9,2,4,5,6]

for i in arr:
    if i > number:
        count += 1
print(count)