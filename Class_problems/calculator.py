class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mult(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def operation(self, op):
        if op == "+":
            return self.x + self.y
        elif op == "-":
            return self.x - self.y
        elif op == "*":
            return self.x * self.y
        elif op == "/":
            return self.x / self.y
        else:
            a = "invalid input"
            return a


if __name__ == "__main__":
    cal = Calculator(5, 7)
    print(cal.add())
    print(cal.sub())
    print(cal.mult())
    print(cal.div())
    print(cal.operation("+"))

