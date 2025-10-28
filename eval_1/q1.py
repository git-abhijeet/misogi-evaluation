# Q: 1
# Write code that simulates a mini banking app:
# A user tries to withdraw more money than available.

# It raises a ValueError but wraps it inside a custom exception InsufficientFundsError.

# Demonstrate raise ... from ... exception chaining.

# Submit the GitHub repository link to the code file



class InsufficientFundsError():
    pass

class BankAcc():
    def __init__(self, amount):
        self.balance = amount
        
    def withdraw(self, amt):
        if(amt > self.balance):
            raise ValueError("Insufficient balance")


acc = BankAcc(5000)
acc.withdraw(6000)