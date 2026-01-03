categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most = 0
for j in expenses:
    if j > most:
      most = j
print(categories[expenses.index(most)])