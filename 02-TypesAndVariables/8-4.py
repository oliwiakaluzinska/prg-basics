cm = 180
inches = cm / 2.54
feet = int(inches // 12)
remainder = inches % 12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {remainder:.2f} inches')