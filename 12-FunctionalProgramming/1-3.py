def ms_to_kmh(ms):
    kmh = 3.6 * int(ms)
    return kmh
ms1 = 10
ms2 = 5

kmh1 = ms_to_kmh(ms1)
kmh2 = ms_to_kmh(ms2)

print(f"Speed in meters per seconds: {ms1} and in kilometers per hour {kmh1}")
print(f"Speed in meters per seconds: {ms2} and in kilometers per hour {kmh2}")