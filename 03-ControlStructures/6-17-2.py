time24 = input('Enter time in 24-hour format (hh:mm): ')
hours, minutes = time24.split(':')
hours = int(hours)
minutes = int(minutes)
if hours <= 12:
    print(f'The time in 12-hour format is {hours}:{minutes}')
elif hours > 12:
    hours -= 12
    print(f'The time in 12-hour format is {hours}:{minutes}')
