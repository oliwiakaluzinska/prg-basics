pin = '0805'
ilosc = 0
while ilosc < 4:
  user = input('Enter PIN: ')
  if user != pin:
    print("Incorrect...")
    ilosc += 1
  else:
    print('Correct!')
    break
  if ilosc == 3:
    print('Sorry, your payment card has been blocked.')
    break