def time_string(hours, minutes, time_format):
    # Format 24-godzinny
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    
    # Format 12-godzinny
    elif time_format == '12':
        if hours == 0:          # północ
            period = "am"
            hours12 = 12
        elif 1 <= hours < 12:   # poranek
            period = "am"
            hours12 = hours
        elif hours == 12:       # południe
            period = "pm"
            hours12 = 12
        else:                   # godziny 13..23
            period = "pm"
            hours12 = hours - 12
        
        return f"{hours12}:{minutes:02d}{period}"

    else:
        return "Invalid format"

print(time_string(15, 38, '24'))  # wypisze: 15:38
print(time_string(11, 15, '12'))  # wypisze: 11:15am
print(time_string(0, 7, '12'))    # wypisze: 12:07am
print(time_string(19, 2, '12'))   # wypisze: 7:02pm