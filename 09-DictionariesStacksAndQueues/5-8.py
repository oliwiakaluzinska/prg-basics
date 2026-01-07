prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total = 0
for i in cart:
    for j in prices:
        if i == j:
            total += cart[i] * prices[j]
print(total)