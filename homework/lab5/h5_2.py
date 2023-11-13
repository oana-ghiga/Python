class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.name} , {self.balance}"

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.savings_accounts = []

    def add_savings_account(self, savings_account):
        self.savings_accounts.append(savings_account)

    def __str__(self):
        checking_info = f"Checking , {self.name} , {self.balance}\n"
        savings_info = "\n".join(str(savings) for savings in self.savings_accounts)
        return checking_info + savings_info


savings1 = SavingsAccount("Savings1", 1000, 0.05)
savings2 = SavingsAccount("Savings2", 1500, 0.03)

checking = CheckingAccount("Main account", 5000)
checking.add_savings_account(savings1)
checking.add_savings_account(savings2)

print(checking)
print ("Interest:", savings2.interest())

savings2.deposit(1000)
savings1.withdraw(500)

print(checking)