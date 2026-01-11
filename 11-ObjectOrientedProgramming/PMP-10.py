class C:
    def __init__(self, coo):
        self.coo = coo

    def m(self, n):
        self.n = n
        number = 0
        for i in self.coo:
            if i[0] > 0 and i[1] > 0:
                number += 1
        if number == self.n:
            return True
        else:
            return False
        
def main():
    x = C([[2,3],[1,8],[-6,4],[3,-7]])
    print(x.m(2))
    print(x.m(3))
main()