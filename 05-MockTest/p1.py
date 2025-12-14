def f(kwota):
    ilosc = 0

    while kwota >= 5:
        ilosc = kwota // 5
        kwota = kwota % 5

    while kwota >= 2:
        ilosc = ilosc + kwota // 2
        kwota = kwota % 2
    while kwota == 1:
        ilosc = ilosc + kwota // 1
        kwota = kwota % 1
    return ilosc 

if __name__ == '__main__':
    print(f(20))