class Account:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New Balance: {self.balance}")
        else:
            print("Balance cannot be negative.")

    def display_info(self):
        return f"Account Number: {self.account_number}, Holder Name: {self.holder_name}, Balance: {self.balance}"
    

class SavingsAccount(Account):

    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        print(f"Interest applied: {self.interest_rate}. New Balance: {self.balance}")

class CurrentAccount(Account):

    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn using overdraft. New Balance: {self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit.")

print("\n=== Saving Account ===") 
savings = SavingsAccount(1034, "Jahanzaib Khalid", 100000, 10)
print(savings.display_info())
savings.deposit(20000)
savings.withdraw(10000)
savings.apply_interest()
print(savings.display_info())

print("\n=== Current Account ===")
current = CurrentAccount(1035, "Jahanzaib Khalid", 80000, 20000)
print(current.display_info())
current.withdraw(80000)
current.withdraw(5000)
print(current.display_info())


