import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for i in data:
    for j,age in i.items():
        if j == 'age':
            if age < 5:
                print(i)

