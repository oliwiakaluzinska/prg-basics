x = int(input('Enter the x: '))
y = int(input('Enter the y: '))
quadrant = 0
if x > 0 and y >0:
    quadrant = 1
elif x < 0 and y > 0:
    quadrant = 2
elif x < 0 and y < 0:
    quadrant = 3
elif x > 0 and y < 0:
    quadrant = 4
print(f'Point P({x},{y}) is in the {quadrant} quadrant of the coordinate system')
if x == 0 and y == 0:
    print(f'Point P({x},{y}) is in the middle of the coordinate system')

