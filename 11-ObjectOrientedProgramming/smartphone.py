from contact_list import Contact_list

def main():
    person = Contact_list()
    person.add('John Brown', 'brown@onet.pl', 555234000)
    person.add('Anna May', 'am@o2.pl', 232000199)
    person.show()

main()