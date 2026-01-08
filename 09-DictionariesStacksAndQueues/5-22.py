product = {}


product['name'] = str(input('Enter name: '))
product['price'] = float(input('Enter price: '))
product['paid'] = input('Did you paid?(yes/no): ')
if product['paid'] == 'yes':
    product['paid'] = True
else:
    product['paid'] = False
print(product)

import json
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)