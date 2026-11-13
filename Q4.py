class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Rs/={amount} has been deposited successfully.....\n")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"Rs/={amount} withdrew successfully.....\n")
        else:
            print("Insufficient balance.........\n")
    def display_balance(self):
        print(f"Hellow {self.account_holder}, Your current balance is {self.balance}\n")

account1 = BankAccount("Narenar kor",50000)
account1.deposit(5020)
account1.withdraw(400)
account1.display_balance()