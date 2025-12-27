amount = int(input('Enter the amount in PLN: '))
ilosc5 = 0
ilosc2 = 0
ilosc1 = 0

ilosc5 = amount // 5
amount = amount % 5
ilosc2 = amount // 2
amount = amount % 2
ilosc1 = amount

print(f'5 PLN coins: {ilosc5}')
print(f'2 PLN coins: {ilosc2}')
print(f'1 PLN coins: {ilosc1}')