class Bank:
    def __init__(self, number):
        self.number = number
        self.account_balance = 0

    def deposit(self, added_value):
        self.account_balance += added_value

    def withdraw(self, taken_value):
        if self.account_balance - taken_value >= 0:
            self.account_balance -= taken_value
        else:
            print('Insufficient funds on the account')

    def show_status(self):
        print(self.number)
        print(self.account_balance)

def main():
    account1 = Bank('12 3456 5555 9090 1111 0000 7722')
    account1.show_status()
    account1.deposit(25.30)
    account1.show_status()
    account1.withdraw(31.60)
    account1.show_status()
    account1.withdraw(14)
    account1.show_status()
main()