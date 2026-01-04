arr = [-15, 8, -31, 47, -2, 19]

maximum = 0
minimum = 0

for i in arr:
    if i > maximum:
        maximum = i
print('Maximum:',maximum)

for i in arr:
    if i < minimum:
        minimum = i
print('Minimum:', minimum)