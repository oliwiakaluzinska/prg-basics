hours = int(input("Enter the number of hours: "))
fee = 0
if hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
print(f"Your fee is {fee} PLN")