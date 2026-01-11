from contact import Contact

class Contact_list:
    def __init__(self):
        self.arr = []

    def add(self, name, email, telephone):
        contact = Contact(name, email, telephone)
        self.arr.append([contact])

    def show(self):
        for i in self.arr:
            for j in i:
                print(j)