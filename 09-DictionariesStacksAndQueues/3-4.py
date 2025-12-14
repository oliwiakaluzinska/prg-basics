person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(person['name'])
print(", ".join(person["hobby"]))
for key,value in person.items():
   print(f"{key} : {value}")

person["surname"] = "Nowak"

# 5. Change person's marriage status
person["married"] = False

# 6. Add gender: 'male'
person["gender"] = "male"

# 7. Add a new hobby: 'bicycle'
person["hobby"].append("bicycle")

# 8. Add work phone to existing phones
person["phone"]["work"] = "313131444"

# 9. Display the entire contents of the dictionary (after modifications)
print("\nUpdated dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")