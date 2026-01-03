# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food = 0
transport = 0 
utilities = 0
# Calculates expenses
# Use loop statements
for i in monthly_expenses:
    food += i[0]
for i in monthly_expenses:
    transport += i[1]
for i in monthly_expenses:
    utilities += i[2]

week1 = 0
week2 = 0
week3 = 0
week4 = 0
for i in monthly_expenses[0]:
    week1 += i
for i in monthly_expenses[1]:
    week2 += i
for i in monthly_expenses[2]:
    week3 += i
for i in monthly_expenses[3]:
    week4 += i

total = week1 + week2 + week3 + week4
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',total)