in_human_years = int(input("Enter the dog's age in human years: "))
in_dog_years = 0
if in_human_years == 1 or in_human_years == 2:
   in_dog_years = in_human_years * 10.5
elif in_human_years > 2:
    in_dog_years = 21 + (in_human_years - 2) * 4
print(f"The dog's age in dog's years is {in_dog_years} years")
