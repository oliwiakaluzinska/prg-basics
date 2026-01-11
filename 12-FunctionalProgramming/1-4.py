def ms_to_kmh(ms):
    kmh = lambda x: x * 3.6
    result = kmh(ms)
    return result

print(ms_to_kmh(35))