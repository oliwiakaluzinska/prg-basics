hours = int(input('Enter the amount of hours: '))
if hours > 6:
    fee = 20
elif hours >= 3:
    fee = 15
else:
    fee = 5
print(f'The fee is {fee}zł')