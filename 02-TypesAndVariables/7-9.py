import random
dice_roll = random.randint(1,6)
special = dice_roll == 1 or dice_roll == 6
print(f'The number is {dice_roll} and is special: {special}')