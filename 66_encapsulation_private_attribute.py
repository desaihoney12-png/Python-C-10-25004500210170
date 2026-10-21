class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def show_balance(self):
        print(self.owner, "has balance", self.__balance)

account = BankAccount("Asha", 1000)
account.deposit(500)
account.show_balance()
