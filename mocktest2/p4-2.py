def f(subjects):
    highest = 0
    result = ''
    for i in subjects:
        avr = sum(subjects[i])/len(subjects[i])
        if avr > highest:
            highest = avr
            result = i
    return result

if __name__ == "__main__":
    print(f({'math':[3,4,4], 'geo':[5,4,4,4], 'comp':[5,4]}))