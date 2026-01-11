def avg_speed(distance,hours,minutes):
    mean = lambda x,y,z: x/(y+z/60)
    avg = mean(distance,hours,minutes)
    return f'{avg:.2f}'

print(avg_speed(70,1,23))