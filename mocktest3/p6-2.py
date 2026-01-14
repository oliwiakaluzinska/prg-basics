class C:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        self.result = ''
        if self.age >= 18:
            self.result = str(self.first[0]).upper() + str(self.last[0]).upper() + str(age)
        else:
            self.result = str(self.first[0]).lower() + str(self.last[0]).lower() + str(age)
    def __str__(self):
       return self.result
    
if __name__ == "__main__":
    print(C("John","May",21))
    print(C("Anna","Brown",17))