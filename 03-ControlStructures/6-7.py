age = int(input("Enter your age: "))
if age < 13:
    print("You are a child")
elif age <= 19:
    print("You are a teen")
elif age <= 64:
    print("You are an adult")
elif age > 64:
    print("You are a senior")