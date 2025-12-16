monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
categories = ["Food", "Transport", "Utilities"]
expenses_number = len(monthly_expenses)
categories_number = len(categories)
# Calculates expenses
# Use loop statements
category_totals = [0] * categories_number
for week in monthly_expenses:
    for i in range(categories_number):
        category_totals[i] += week[i]

weekly_totals = []
for week in monthly_expenses:
    weekly_totals.append(sum(week))

sum = 0
for row in monthly_expenses:
    for item in row:
        sum += item


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
for i in range(categories_number):
    print(f'{categories[i]}: {category_totals[i]}')

for i in range(expenses_number):
    print(f'Week {i+1}: {weekly_totals[i]}')

print('---------------')
print('TOTAL:',sum)