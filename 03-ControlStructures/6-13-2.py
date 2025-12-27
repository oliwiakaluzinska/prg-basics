car_speed = int(input('Enter your car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed < speed_limit_min:
    print('Warning: invalid car speed!!')
elif car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Good for you')