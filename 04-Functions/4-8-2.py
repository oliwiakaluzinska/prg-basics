def time_string(hours, minutes, time_format):
    if time_format == '24':
        return (f'{hours:02}:{minutes:02}')
    elif time_format == '12':
        if hours > 12:
            hours -= 12
            return (f'{hours:02}:{minutes:02}pm')
        elif hours == 0:
            hours += 12
            return (f'{hours:02}:{minutes:02}am')
        elif hours == 12:
            return (f'{hours:02}:{minutes:02}pm')
        else:
            return (f'{hours:02}:{minutes:02}am')
        
print(time_string(15, 38, '24'))
print(time_string(11, 15, '12'))
print(time_string(12, 46, '12'))
print(time_string(0, 7, '12'))