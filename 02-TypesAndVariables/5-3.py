a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
cuboid_volume = a*b*c
cuboid_surface = (a*b)*2 + (b*c)*2 + (a*c)*2

print(f'The volume of a cuboid with sides {a},{b},{c} is {cuboid_volume}')
print(f'The surface of a cuboid with sides {a},{b},{c} is {cuboid_surface}')