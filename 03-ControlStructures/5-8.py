print('1. Deposit')
print('2. Withdraw')
print('3. Check the balance')
print('4. Check PIN')
print('5. Change PIN')
user = input('Enter what you want to do(1,2,3,4,5): ')
balance = 0
if user == '1':
    balance += user
    print(f'You deposit{user}zł')
elif user == '2':
    balance -= user