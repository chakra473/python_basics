from dequeue import Deque


def palindrom_checker(str_in):
    """
    function for check palindrome string using deque
    :param str_in: string input from user
    :return: palindrome string
    """
    char_deque = Deque()

    for ch in str_in:
        char_deque.insert_at_front(ch)

    still_equal = True

    while char_deque.deque_length() > 1 and still_equal:
        first = char_deque.del_from_front()
        last = char_deque.delete_from_rear()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == "__main__":
    str_input = input("enter a string: ")
    print(palindrom_checker(str_input))
