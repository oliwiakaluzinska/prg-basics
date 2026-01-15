class Person:
    def __init__(self,first,last,score):
        self.first = first
        self.last = last
        self.score = score
        self.result = ''
        if self.score >=50:
            self.result = first[0].upper() + last[0].upper() + str(score)
        else:
            self.result = first[0].lower() + last[0].lower() + str(score)

    def __str__(self):
        return self.result
    
if __name__ == "__main__":
    print(Person("Tom","Lee",80))
    print(Person("Anna","Fox",40))
