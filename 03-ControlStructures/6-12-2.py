products = int(input('Enter the number of products purchased: '))
price = int(input('Enter the product price: '))
i = 0
amount = 0
while i < products:
    if i == 1:
        amount += price
    elif i == 2:
        amount += price
    else:
        amount += 0.75*price
    i += 1
print(amount)