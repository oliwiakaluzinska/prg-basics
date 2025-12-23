speed_limit = 140
speed = int(input("Enter the speed limit: "))

if speed < speed_limit:
    print(f'Your speed is {speed}km/h')
else:
    print('Warning: speed limit exceeded!!')