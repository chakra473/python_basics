# Python code to implement binary search
# on Singly Linked List

# Link list node
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def new_node(x):
    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp


# function to find out middle element
def middle(start, last):
    if start is None:
        return None

    slow = start
    fast = start.next

    while fast != last:

        fast = fast.next
        if fast != last:
            slow = slow.next
            fast = fast.next

    return slow


def binary_search(head, value):
    """
     Function for implementing the Binary
     Search on linked list
    :param head:
    :param value:
    :return:
    """
    start = head
    last = None

    while True:

        # Find middle
        mid = middle(start, last)

        # If middle is empty
        if mid is None:
            return None

        # If value is present at middle
        if mid.data == value:
            return mid

        # If value is more than mid
        elif mid.data < value:
            start = mid.next

        # If the value is less than mid.
        else:
            last = mid

        if not (last is None or last != start):
            break

    # value not present
    return None
