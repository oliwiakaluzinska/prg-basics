hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
totalK = 0
quantityK = 0
for i in hotels_in_Krakow:
    totalK += i['price']
    quantityK += 1
avgK = totalK / quantityK
print(avgK)

totalS = 0
quantityS = 0
for i in hotels_in_Sopot:
    totalS += i['price']
    quantityS += 1
avgS = totalS / quantityS
print(avgS)

if avgS > avgK:
    print('Sopot is more expensive')
else:
    print('Krakow is more expensive')