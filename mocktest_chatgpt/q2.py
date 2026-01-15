class P:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.q = ""
    def m1(self):
        if self.x > 0 and self.y > 0:
            self.q = "I"
        elif self.x < 0 and self.y >0:
            self.q = "II"
        elif self.x < 0 and self.y < 0:
            self.q = "III"
        elif self.x > 0 and self.y < 0:
            self.q = "IV"
        else:
            self.q = 'AXIS'
        
    def m2(self,a,b):
        self.a = a
        self.b = b
        self.q2 = ""
        if self.a > 0 and self.b > 0:
            self.q2 = "I"
        elif self.a < 0 and self.b >0:
            self.q2 = "II"
        elif self.a < 0 and self.b < 0:
            self.q = "III"
        elif self.a > 0 and self.b < 0:
            self.q2 = "IV"
        else:
            self.q2 = 'AXIS'
        
        if self.q == self.q2:
            return True
        else:
            return False
        
    def m3(self,a,b):
        import math
        self.a = a
        self.b = b
        result = math.sqrt((self.x-self.a)**2+(self.y-self.b)**2)
        if result < 10:
            return True
        else:
            return False

if __name__ == "__main__":
    def main():
        p = P(5,3)
        p.m1()
        print(p.m2(8,-2))
        print(p.m3(5,0))
    main()