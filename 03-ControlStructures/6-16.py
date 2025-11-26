program = input("Select washing program: (j)acket, (u)nderwear, (s)hoes: ")
extra_rinse = input("Extra rinse? (y/n) ")
extra_spin = input("Extra spin? (y/n) ")
total_washing_time = 0
if program == "s":
    total_washing_time = 20
elif program == "u":
    total_washing_time = 70
elif program == "j":
    total_washing_time = 40
else:
    print("Invalid program selected")
if extra_rinse == "y":
    total_washing_time = total_washing_time + 15
else:
    total_washing_time = total_washing_time
if extra_spin == "y":
    total_washing_time = total_washing_time + 9
else:
    total_washing_time = total_washing_time
print(f"Total washing time: {total_washing_time} minutes")