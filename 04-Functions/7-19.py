def f(number):
    suma = 0
    for i in range(len(str(number))):
       x = False
       for j in range(len(str(number))):
           if i != j and str(number)[i] == str(number)[j] :
               x = True
       if x:
           suma += int(str(number)[i])
    
            
    return suma

if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))