t = ("Seven", [10, 20, 30], (5, 15, 25))

print(t[0])

for x in t:
    for y in x:
        if y == 30:
            print(y)