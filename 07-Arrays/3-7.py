arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

max = arr[0]
for i in arr:
    if len(i) > len(max):
        max = i
print(max)