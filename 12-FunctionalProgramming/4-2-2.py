recorded = [48,47,54,50,42,68,39,46]
too_high = list(filter(lambda x:x>50, recorded))

print(", ".join(str(x) for x in too_high))