class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self,s,n):
        self.s = s
        self.n = n
        for i in self.sectors:
            if i == self.s:
                self.sectors[i] = self.n
        if not self.s in self.sectors:
            self.sectors[self.s] = self.n
    
    def m2(self, s):
        self.s = s
        total = 0
        for i in self.s:
            for j in self.sectors:
                if i == j:
                    total += self.sectors[j]
        return total
    
def main():
    x = C({"A":120,"D":150,"G":90,"K":110})
    x.m1("G",130)
    x.m1('E',50)
    print(x.m2("GD"))
    print(x.m2("KEJ"))
main()