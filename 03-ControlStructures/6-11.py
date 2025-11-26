current = int(input("Enter the current price of a product: "))
previous = int(input("Enter the previous price of a product: "))
reduce = 100 - (current * 100) / previous
if reduce >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduce}%")
else:
    print("Wait for a bigger discount")