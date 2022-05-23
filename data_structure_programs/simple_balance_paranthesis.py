class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def balanced_paren(self, input_string):
        for c in input_string:
            if c == '(' or c == '{' or c == '[':
                self.push(c)
            elif (c == ')' and self.head.data == '(') or (c == '}' and self.head.data == '{') \
                    or (c == ']' and self.head.data == '['):

                empty = self.is_empty()
                if empty:
                    return f"expression is not balanced {input_string}"
                else:
                    self.pop()

        check = self.is_empty()
        if check:
            return f"expression is balanced {input_string}"
        else:
            return f"Expression is not balanced {input_string}"


if __name__ == "__main__":
    obj = Stack()
    str_in = "(5+6)*(3)"
    print(obj.balanced_paren(str_in))
