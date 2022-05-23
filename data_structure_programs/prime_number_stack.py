class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    def push(self, data):
        """
        function for inserting element into stack
        :param data: get inserted data
        :return: insert data in respective position
        """
        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def primes(self, n):
        array = [i for i in range(2, n + 1)]
        p = 2

        while p <= n:
            i = 2 * p
            while i <= n:
                array[i - 2] = 0
                i += p
            p += 1

        for num in array:
            if num > 0:
                self.push(num)

    def display(self):
        """
        Function for Displaying stack elements
        :return: display stack elements
        """
        iter_node = self.head

        while (iter_node != None):
            print(iter_node.data,  end="\n")
            iter_node = iter_node.next
        return


if __name__ == '__main__':
    st = Stack()
    num_range = 1000
    st.primes(num_range)
    st.display()

