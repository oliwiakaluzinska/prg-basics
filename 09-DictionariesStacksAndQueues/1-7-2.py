products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for x,y in products.items():
    print(x, y)

suma = 0
for i in products.values():
    suma += i
print('Sum of products: ',suma)