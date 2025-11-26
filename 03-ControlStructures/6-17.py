time24 = input('Enter time (24-hour format): ')
hour24_1, minute_1 = time24.split(":")
hour24_2 = int(hour24_1)
minute_2 = int(minute_1)
hour12 = 0
if hour24_2 == 0:
   hour12 = 12
   print(f'Time in 12-hour format: {hour12}:{minute_2}AM')
else:
   hour24_2 >=1 and hour24_2 < 12
   hour12 = hour24_2
   print(f'Time in 12-hour format: {hour12}:{minute_2}AM')
if hour24_2 > 12:
   hour12 = hour24_2 - 12
   print(f'Time in 12-hour format: {hour12}:{minute_2}PM')