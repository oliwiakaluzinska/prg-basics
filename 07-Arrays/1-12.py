categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = expenses[0]
max_category = categories[0]
for i in range(len(expenses)):
    if expenses[i] > max_expense:
        max_expense = expenses[i]
        max_category = categories[i]

print("The most expensive category is:", max_category)
print("Amount spent:", max_expense)