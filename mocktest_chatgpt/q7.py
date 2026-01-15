class Counter:
    def __init__(self,x):
        self.x = x

    def add(self):
        self.x += 1

    def sub(self):
        self.x -= 1

    def change(self,n):
        self.n = n
        self.x += self.n

    def __str__(self):
        return str(self.x)
    
if __name__ == "__main__":
    p = Counter(5)
    p.add()
    p.sub()
    p.change(6)
    print(p)