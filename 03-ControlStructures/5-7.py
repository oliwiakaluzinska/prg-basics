number = int(input('Enter the number: '))
countdown = number
in_words = {5:'five',4:'four',3:'three',2:'two',1:'one'}
while countdown > 0:
    if countdown in in_words:
        print(in_words[countdown])
    else:
        print(countdown)
    countdown -= 1