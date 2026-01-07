price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for x,y in price_list.items():
    print(x, y)

totalb = 0
for i in price_list.values():
    totalb += i
print(f'Total before: {totalb:.2f}')

for i in price_list:
    price_list[i] = price_list[i]*0.9
    price_list[i] = round(price_list[i], 2)

for x,y in price_list.items():
    print(x, y)

totala = 0
for i in price_list.values():
    totala += i
print(f'Total after: {totala:.2f}')
