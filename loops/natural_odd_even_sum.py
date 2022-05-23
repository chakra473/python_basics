def natural_num_for_loop(num):
    """
    this method returns n natural numbers using for loop
    :param num: num is the input upto which this method returns values
    :return: n natural number in a list
    """
    nat = []
    for i in range(1, num + 1):
        nat.append(i)
    return nat


def natural_num_while_loop(num):
    """
    this method returns n natural numbers using while loop
    :param num: num is the input upto which this method returns values
    :return: n natural number in a list
     """
    i = 1
    nat = []
    while i <= num:
        nat.append(i)
        i += 1
    return nat


def odd_even_range_n_nat_num_for_loop(lower, upper):
    """
    this method returns n natural odd and even numbers using for loop
    :param lower:lower limit from this number it starts iterating
    :param upper: upper limit upto this number it ends
    :return: all odd and even numbers which upper & lower limits
    """
    odd_range = []
    even_range = []
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            even_range.append(i)
        else:
            odd_range.append(i)
    return even_range, odd_range


def odd_even_range_n_nat_num_while_loop(lower, upper):
    """
    this method returns n natural odd and even numbers using while loop
    :param lower:lower limit from this number it starts iterating
    :param upper: upper limit upto this number it ends
    :return: all odd and even numbers which upper & lower limits
    """
    odd_range = []
    even_range = []
    i = lower
    while i <= upper:
        if i % 2 == 0:
            even_range.append(i)
        else:
            odd_range.append(i)
        i += 1
    return even_range, odd_range


def sum_n_natural_num_for_loop(num):
    """
    this method gives sum of n natural numbers using for loop
    :param num: input n value
    :return: sum of n natural numbers
    """
    res = 0
    for i in range(1, num + 1):
        res += i
    return res


def sum_n_natural_num_while_loop(num):
    """
    this method gives sum of n natural numbers using while loop
    :param num: input n value
    :return: sum of n natural numbers
    """
    res = 0
    i = 1
    while i <= num:
        res += i
        i += 1
    return res


def sum_odd_even_n_nat_num_for_loop(num):
    """
    this method gives sum of n natural odd and even numbers using for loop
    :param num: input n value
    :return: sum of n natural odd and even numbers in list
    """
    even_sum = 0
    odd_sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum


def sum_odd_even_n_nat_num_while_loop(num):
    """
    this method gives sum of n natural odd and even numbers using while loop
    :param num: input n value
    :return: sum of n natural odd and even numbers in list
    """
    even_sum = 0
    odd_sum = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i
        i += 1
    return even_sum, odd_sum


if __name__ == "__main__":
    n = 100
    print(natural_num_for_loop(n))
    print(natural_num_while_loop(n))
    print(sum_n_natural_num_for_loop(n))
    print(sum_n_natural_num_while_loop(n))
    print(sum_odd_even_n_nat_num_for_loop(n))
    print(sum_odd_even_n_nat_num_while_loop(n))
    print(odd_even_range_n_nat_num_for_loop(50, 100))
    print(odd_even_range_n_nat_num_while_loop(18, 45))
