file_name = 'reservations.json'

def f1(name):
    import json
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    result = []
    for i in data['reservations']:
        result.append(i['room_number'])
    return len(result), result

print(f1(file_name))

def f2(name):
    import json
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    number = 0
    for i in data['reservations']:
        if i['paid'] == True:
            number += 1
    return number

print(f2(file_name))

def f3(name):
    import json
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    number = 0
    for i in data['reservations']:
        if i['paid'] == False:
            number += 1
    return number
print(f3(file_name))

def f4(name):
    import json
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    result = 0
    for i in data['reservations']:
        if i['paid'] == True:
            result += i['nights'] * i["price_per_night"]
    return result
print(f4(file_name))

def f5(name):
    import json
    with open(name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    result = 0
    for i in data['reservations']:
        if i['paid'] == False:
            result += i['nights'] * i["price_per_night"]
    return result
print(f5(file_name))