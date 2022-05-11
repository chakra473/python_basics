# Python3 program to accept an amount
# and count number of notes

# Function to count and print
# currency notes
def count_currency(amount):
    notes = [2000, 500, 200, 100,
             50, 20, 10, 5, 1]

    noteCounter = [0, 0, 0, 0, 0,
                   0, 0, 0, 0]

    print("Currency Count -> ")
    min_notes = 0
    total_notes = 0

    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print(i, " : ", j)
            total_notes += j
            min_notes += 1
    return min_notes, total_notes


class TestClass:

    def test_one(self):
        # Driver code
        amount = 1000
        a, b = (count_currency(amount))  # a is number of minimum Note needed to give the change
        assert a <= b  # b is number of notes that would have given in the Change
