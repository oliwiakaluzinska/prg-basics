amount = int(input('Enter the amount: '))
coin1 = 0 
coin2 = 0
coin3 = 0
remainder = ""
if amount == 0:
    print("You need to enter the amount")
else:
    coin5 = amount // 5
    remainder = amount % 5
    coin2 = remainder // 2
    remainder = remainder % 2
    coin1 = remainder // 1

print(f'5PLN: {coin5}, 2PLN: {coin2}, 1PLN{coin1}')
