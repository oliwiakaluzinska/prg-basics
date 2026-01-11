def initials(name,surname):
    mean = lambda x,y: f'{x[0]}{y[0]}'
    result = mean(name,surname)
    return result

print(initials("Anna", "May"))