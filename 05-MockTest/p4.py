def f(numer):
    if not len(numer) == 16:
        return 0
    elif len(numer) == 16:
        poczatek = numer[0:2]
        ukryty = 10 * "*"
        koniec = numer[12:16]
        numerkarty = poczatek + ukryty + koniec
        return numerkarty
if __name__ == '__main__':
    print(f('8765432109800000'))
