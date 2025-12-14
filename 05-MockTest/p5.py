def f(liczba):

    for i in liczba:
        if i == '0' or i == '1':
            return True
        else:
            return False
        
if __name__ == '__main__':
    print(f('10011'))