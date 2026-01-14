class C:
    def __init__(self,co):
        self.co = co

    def m1(self):
        return self.co
    def m2(self):
        self.co += 1
    def m3(self):
        self.co -= 1
    def m4(self,n):
        self.n = n
        self.co += self.n
    def __str__(self):
        return str(self.co)
    
if __name__ == "__main__":
 def main():
    c=C(5)
    w1 = c.m1() #returns 5
    c.m2()
    w2 = c.m1() #returns 6
    c.m4(-8)
    w3 = c.m1() #returns -2
    c.m3()
    w4 = c.m1() #returns -3
    c.m4(10)
    w5 = c.m1() #returns 7
    w6 = c.__str__() #returns "7" 
    return w1,w2,w3,w4,w5,w6
 print(main())