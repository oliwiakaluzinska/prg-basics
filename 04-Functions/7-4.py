def f(text):
    sum = 0
    for i in text:
        if i == 'e':
            sum += 1
    return sum

if __name__ == "__main__":
    print(f('You never get a second chance to make a first impression'))