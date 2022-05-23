# To print the matrix
def print_matrix(rows, columns, result):
    for i in range(rows):
        for j in range(columns):
            print(result[i][j], end=" ")

        print()


if __name__ == "__main__":
    n_rows = int(input("Number of rows:"))

    n_columns = int(input("Number of columns:"))

    # Define the matrix

    matrix = []

    print("Enter the entries row-wise:")

    # for user input

    for i in range(n_rows):  # A for loop for row entries

        a = []

        for j in range(n_columns):  # A for loop for column entries

            a.append(int(input()))

        matrix.append(a)

    print_matrix(n_rows, n_columns, matrix)
