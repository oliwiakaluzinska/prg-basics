def f(detector):
    room = 0
    for i in detector:
        if i == "+":
            room += 1
        elif i == "-":
            room -= 1
        
        if room >= 3:
            return True   

    return False

   
    
if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))
        