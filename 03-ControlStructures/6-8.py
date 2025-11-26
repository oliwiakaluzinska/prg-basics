person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
elif person1_age >= 18 and person2_age < 18:
    print(f"Only {person1_name} is an adult")
elif person2_age >= 18 and person1_age <18:
    print(f"Only {person2_name} is an adult")
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')