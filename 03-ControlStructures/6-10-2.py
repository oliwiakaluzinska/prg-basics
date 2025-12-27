age_in_human = int(input('Enter the dogs age in human years: '))
age_in_dog = 0
i = 0
while i <= age_in_human:
    if i == 1:
        age_in_dog += 10.5
    elif i == 2:
        age_in_dog += 10.5
    elif i > 2:
        age_in_dog += 4
    i += 1 

print(f'The dogs age in dogs years is {age_in_dog} years.')