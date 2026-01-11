class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def show(self):
        result = ''
        if self.age >= 18:
            result += self.surname.upper() + self.name[0].upper() + str(self.seniority)
        elif self.age < 18:
            result += self.surname.lower() + self.name[0].lower() + str(self.seniority)
        return result
    
def main():
    person1 = C("Anna","May",17,7)
    print(person1.show())
    person2 = C("George","Brown",21,4)
    print(person2.show())
main()
