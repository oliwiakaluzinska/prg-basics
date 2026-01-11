from contact import Contact

class Contact_list:
    def __init__(self):
        self.arr = []

    def add(self):
        self.arr.append([Contact])

    def show(self):
        for i in self.arr:
            for j in i:
                print(j)
            print()