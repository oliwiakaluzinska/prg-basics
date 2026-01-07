basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {}
for i in basic_data:
    person[i] = basic_data[i]
for j in advanced_data:
    person[j] = advanced_data[j]

for x,y in person.items():
    print(x,y)