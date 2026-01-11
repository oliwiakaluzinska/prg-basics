from contact_list import Contact_list
from contact import Contact
def main():
    person1 = Contact('John Brown', 'brown@onet.pl', 555234000)
    person1 = Contact_list()
    person1.add()
    person2 = Contact('Anna May', 'am@o2.pl', 232000199)
    person2 = Contact_list()
    person2.add()
    person2.show()