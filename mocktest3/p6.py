class C: 
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.text = ''
    
    def __str__(self):
        if self.age >= 18:
            self.text = self.first_name[0] + self.last_name[0] + str(self.age)
        else:
           self.text = self.first_name[0].lower() + self.last_name[0].lower() + str(self.age) 
        return self.text
           
    
print(C("John","May",21))
print(C("Anna","Brown",17))
        