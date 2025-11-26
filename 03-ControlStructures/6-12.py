product_number = int(input("Enter the number of purchased products: "))
price = int(input("Enter the product price: "))
full_cost = 0
if product_number <=2:
    full_cost = price*product_number
elif product_number > 2:
    full_cost = price*2 + (product_number - 2)*price*0.75
print(f"The amount to pay: {full_cost}")   