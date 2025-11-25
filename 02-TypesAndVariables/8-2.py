import math
r = int(input('Enter the radius of a circle: '))
a = float(math.pi * r**2)
c = float(math.pi * 2 * r)
print(f'The circle with radius {r} has area {a:.2f} and circumference {c:.2f}')