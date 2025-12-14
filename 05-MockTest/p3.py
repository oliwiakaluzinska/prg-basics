def f(nazwa):
   nazwa = str(nazwa)
   slowa = nazwa.split()
   akronim = ""

   for i in slowa:
      akronim = akronim + i[0]
   return akronim

if __name__ == '__main__':
 print(f("The Lord Of Rings"))