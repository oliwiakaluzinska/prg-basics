number = input('Enter the EAN-13 number: ')
if len(number) == 13:
    print('Article number is correct')
    if number[0:3] == '590':
        print('Article manufactured in Poland')
    else:
        print('Article manufactured not in Poland')
else:
    print('Article number is not correct')