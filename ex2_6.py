class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Początkowe saldo nie może być ujemne.")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być dodatnia.")
        if amount > self.balance:
            raise ValueError("Niewystarczające środki.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
