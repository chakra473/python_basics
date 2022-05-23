# Python program to create Bank-account class
# with both a deposit() and a withdraw() function
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


# creating an object of class
if __name__ == '__main__':
    s = BankAccount()

    # Calling functions with that class object
    s.deposit()
    s.withdraw()
    s.display()
