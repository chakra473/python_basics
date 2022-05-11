
def print_array(m, n, array_inp):
    """

    :param m: no of rows
    :param n: no of columns
    :param array_inp: elements of array
    :return:
    """
    for i in range(0, m):
        for j in range(0, n):
            print(array_inp[i][j], end=" ")
        print()


if __name__ == "__main__":
    row = int(input("enter the number of rows: "))
    column = int(input("enter the number of columns: "))
    print("enter the elements of the array: ")
    array_input = []
    for k in range(0, row):
        a = []
        for p in range(0, column):
            a.append(int(input()))
        array_input.append(a)

    # calling print_array function to print the array elements
    print_array(row, column, array_input)
    print(len(array_input))
    print(array_input)
