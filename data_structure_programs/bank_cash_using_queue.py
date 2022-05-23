class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.balance = 0
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def deposit(self, amount):
        """
        function for deposit money to bank account
        :param amount: money from user
        :return: deposit money and add to queue
        """
        temp = Node(amount)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

        self.balance += amount
        print("Amount added to you bank account")

    def withdraw(self, amount):
        """
        function for withdraw money from account
        :param amount: withdraw amount
        :return: remove money from queue
        """
        if self.balance >= amount:
            self.balance -= amount
            if self.is_empty():
                return
            temp = self.front
            self.front = temp.next

            if self.front is None:
                self.rear = None
            return f"you withdraw an amount of {amount} "

    def display_transaction(self):
        """
        function for checking account balance and transaction
        :return: main account balance
        """
        iter_node = self.front
        if self.is_empty():
            print("Stack Underflow")

        else:
            while iter_node is not None:
                print(iter_node.data, "->", end=" ")
                iter_node = iter_node.next

    def display_balance(self):
        """
        function for calculating main account balance
        :return: total account balance
        """
        print("Net available balance is: ", self.balance)


if __name__ == "__main__":
    bank = Queue()
    print(" 1. for adding Balance "
          "\n 2. for Withdraw amount "
          "\n 3. for check main balance"
          "\n 4. For checking transaction")

    while True:
        input_ = int(input("Enter Selection"))
        if input_ == 1:
            deposit_money = float(input("Enter deposit amount"))
            bank.deposit(deposit_money)

        elif input_ == 2:
            withdraw_money = float(input("enter withdraw amount"))
            bank.withdraw(withdraw_money)

        elif input_ == 3:
            bank.display_balance()

        elif input_ == 4:
            bank.display_transaction()

