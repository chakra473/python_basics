def sum_two_array(arr1, arr2):
    """
    this method finds the sum of elemnets of two arrays
    of same index
    :param arr1: input array1
    :param arr2: input array2
    :return: sum of two array in single arr
    """
    sum_arr = []
    for i in range(0, len(arr2)):
        # add_arr = 0
        add_arr = arr1[i] + arr2[i]
        sum_arr.append(add_arr)
    return sum_arr


if __name__ == '__main__':
    a1 = [1, 4, 2, 4, 5]
    a2 = [4, 12, 43, 5, 4]
    print(sum_two_array(a1, a2))
