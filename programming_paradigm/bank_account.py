class BankAccount: 
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = float(account_balance)
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance += float(amount)
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= float(amount)
            return 1
        else:
            return 0
        
    def display_balance(self):
        balance = f"Current Balance: ${self.account_balance:.2f}"
        print(balance)
