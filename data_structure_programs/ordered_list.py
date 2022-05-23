
# Node class
class Node:
    def __init__(self, data):
        """
        constructor to initialize data
        :param data: to get data
        """
        # Assign data
        self.data = data

        # Initialize next as null
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        """
        constructor to initialize head as none
        """
        self.head = None

    def push(self, new_data):
        """
        this function is used to insert node in beginning of a linkedlist
        :param new_data:to create a new node
        :return:new node inserted
        """
        # Create a new Node
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node

    def search(self, x):
        """
        function is used to search the given number present in the linked list or not
        :param x: search number
        :return: true or false
        """
        # Initialize current to head
        current = self.head

        # Loop till current not equal to None
        while current is not None:
            if current.data == x:
                # Data found
                return True

            current = current.next

        # Data Not found
        return False


if __name__ == '__main__':
    llist = LinkedList()

    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.push(50)

    search_word = int(input("please enter a search number to check: "))
    print(llist.search(search_word))
