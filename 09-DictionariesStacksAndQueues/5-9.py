numbers = 'vehicle.txt'
polish = 'province.csv'
with open(numbers, 'r', encoding='utf-8') as file:
    all = [line.strip() for line in file]

with open(polish, 'r', encoding='utf-8') as files:
    poland = files.readlines()
result = {}
for number in all:
    for letter in poland:
          if number[0] == letter[0]:
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
print(result)