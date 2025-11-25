import random
computer = random.randint(1,6)
you = int(input('Guess the number: '))
result = you == computer
print(f'You won: {result}')