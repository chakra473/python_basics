# find sum of negative numbers
def neg_sum(list1):
    """
    this method is finds the sum of negative numbers
    in the list that we are passing
    :param list1: input the list
    :return: sum of all negative numbers inside list1
    """
    # counter for sum of
    # negative numbers
    neg_sum1 = 0

    for num in list1:

        # converting number
        # to integer explicitly
        num = int(num)

        # if negative number
        if num < 0:
            # simply add to the
            # negative sum
            neg_sum1 += num
    return neg_sum1


# find sum of positive numbers
# according to categorize
def pos_sum(list1):
    """
    this method is finds the sum of positive numbers
    in the list that we are passing
    :param list1: input the list
    :return: sum of all positive numbers inside list1
    """
    # counter for sum of
    # positive  numbers
    pos_sum1 = 0
    for num in list1:

        # converting number
        # to integer explicitly
        num = int(num)

        # if negative number
        if num >= 0:
            pos_sum1 += num

    return pos_sum1


if __name__ == '__main__':
    # input a list of numbers
    list_num = [-7, 5, 60, -34, 1]

    # creating an object of class

    # calling method for sum
    # of all negative numbers
    print(neg_sum(list_num))

    # calling method for
    # sum of all positive numbers
    print(pos_sum(list_num))
