product_price = float(input('Enter the product price: '))
discount_percent = float(input('Enter the discount(%): '))
discount = 0.01 * discount_percent
price_with_disc = product_price - product_price * discount
reduction = product_price * discount

print (f'The product price is: {product_price}')
print (f'The discount is: {discount_percent}')
print (f'The price with discount is: {price_with_disc:.2f}')
print (f'And the reduction is: {reduction:.2f}')