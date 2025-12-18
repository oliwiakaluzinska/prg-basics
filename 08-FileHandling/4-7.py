import re
text = input("Enter the text: ")
sum = 0
for i in text:
    number = r'[aeiouyąęó]'
    if re.findall(number, i):
        sum += 1
print(sum)