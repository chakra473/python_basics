class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.dequeSize = 0

    def is_empty(self):
        if self.dequeSize == 0:
            return True
        return False

    def deque_length(self):
        return self.dequeSize

    def insert_at_front(self, data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.dequeSize = self.dequeSize + 1
        else:
            temp.next = self.front
            self.front = temp
            self.dequeSize = self.dequeSize + 1

    def insert_at_rear(self, data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.dequeSize = self.dequeSize + 1
        else:
            curr = self.front
            while curr.next is not None:
                curr = curr.next
            curr.next = temp
            self.dequeSize = self.dequeSize + 1

    def del_from_front(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                temp = self.front
                self.front = self.front.next
                self.dequeSize = self.dequeSize - 1
                del temp
        except Exception as e:
            print(str(e))

    def delete_from_rear(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                prev = None
                while curr.next is not None:
                    prev = curr
                    curr = curr.next
                prev.next = curr.next
                self.dequeSize = self.dequeSize - 1
                del curr
        except Exception as e:
            print(str(e))

    def get_front(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                return self.front.data
        except Exception as e:
            print(str(e))

    def get_rear(self):
        try:
            if self.dequeSize == 0:
                raise Exception("Deque is Empty")
            else:
                curr = self.front
                while curr.next is not None:
                    curr = curr.next
                return curr.data
        except Exception as e:
            print(str(e))
