class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.quadrantxy = 0
        self.quadrantab = 0

    def m1(self):
        if self.x > 0 and self.y > 0:
            self.quadrantxy = 1
        elif self.x < 0 and self.y > 0:
            self.quadrantxy = 2
        elif self.x < 0 and self.y < 0:
            self.quadrantxy = 3
        elif self.x > 0 and self.y < 0:
            self.quadrantxy = 4
        else:
            self.quadrantxy = 0
        return self.quadrantxy
    
    def m2(self,a,b):
        self.a = a
        self.b = b
        if self.a > 0 and self.b > 0:
            self.quadrantab = 1
        elif self.a < 0 and self.b > 0:
            self.quadrantab = 2
        elif self.a < 0 and self.b < 0:
            self.quadrantab = 3
        elif self.a > 0 and self.b < 0:
            self.quadrantab = 4
        else:
            self.quadrantab = 0

        if self.quadrantxy == self.quadrantab:
            return True
        else:
            return False
        
    def m3(self,a,b):
        import math
        self.a = a
        self.b = b
        if math.sqrt((self.x - self.a)**2 + (self.y - self.b)**2) > 5:
            return True
        else:
            return False
        
def main():
    p = C(2,3)
    w = p.m1() 
    w1 = p.m2(7,4) 
    w2 = p.m2(-3,1) 
    w3 = p.m3(8,5) 
    w4 = p.m3(4,7) 
    p1 = C(0,5)
    w5 = p1.m1() 
    w6 = p1.m2(4,7) 
    w7 = p1.m2(-7,0)
    return w,w1,w2,w3,w4,w5,w6,w7

if __name__ == "__main__": 
    print(main())