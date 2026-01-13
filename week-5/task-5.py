class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner  # Private attribute 
        self.__balance = balance  # Private attribute 

    def deposit(self, amount):
        if amount > 0:  # Validation: Deposit must be positive 
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Error: Deposit must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:  # Validation: Must not exceed balance 
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Withdrawal must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    account = BankAccount("Alexandru", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Current Balance: {account.get_balance()}")