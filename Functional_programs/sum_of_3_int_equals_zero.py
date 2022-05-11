# defining function to calculate the sum of three integers equals to zero
def sum_zero(n, arr_res):
    """

    :param n: N integers of triplets
    :param arr_res: collection of integers in the list
    :return:
    """
    a = 1
    i = 0
    j = 1
    k = 2
    count = 0
    while a <= n:
        if (arr_res[i] + arr_res[j] + arr_res[k]) == 0:
            print("the distinct triplets are :" + "(" + str(arr_res[i]) + "," + str(arr_res[j]) + "," + str(
                arr_res[k]) + ")")
            count += 1
        a += 1
        i += 3
        j += 3
        k += 3
    print("The number of distinct triplets :", count)


if __name__ == "__main__":
    num = int(input("enter the N integers "))
    arr = []
    for b in range(num):
        for c in range(3):
            arr.append(int(input()))
    # calling the sum_zero with num and arr arguments
    sum_zero(num, arr)
