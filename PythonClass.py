class Account:
    def __init__(self, account_number, balance=0):
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)


titus_onabanjo_acct = Account("123456789")
titus_onabanjo_acct.deposit(100)
titus_onabanjo_acct.withdraw(10)


