current = 190
previous = 200
decrease = int((1 - current / previous)*100)
if decrease >= 10:
    print(f'Buy the product!! Product price reduced by {decrease}%')
else:
    print('Whait for bigger decrease')