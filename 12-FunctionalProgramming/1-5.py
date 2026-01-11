def avg_speed(distance,hours,minutes):
    minutes = minutes / 60
    avg = distance / (hours + minutes)
    return avg

dis = int(input('Enter distance in km: '))
ho = int(input('Enter number of travel hours: '))
minu = int(input('Enter number of travel minutes: '))
print(f'Avrige speed: {avg_speed(dis,ho,minu):.2f}')
