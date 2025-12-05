import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

with open(email_file, "r", encoding="utf-8") as file:
    email = file.read()

pattern = r'€?\s?(\d+(\.\d{1,2})?)'  

# extract amounts from email
amounts = re.findall(pattern, email)

# calculate the total purchases
total_spent = 0
for amount in amounts:
    total_spent += int(amount[0])  # convert the string amount to a float and sum it up

# print result
print(f"Total money spent: €{total_spent:.2f}")
