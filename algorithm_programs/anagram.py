def anagram(x, y):
    x = x.lower()
    y = y.lower()
    x1 = []
    y1 = []
    for i in x:
        x1.append(i)
    for j in y:
        y1.append(j)
    x1 = sort(x1)
    y1 = sort(y1)
    print(x1)
    print(y1)
    if x1 == y1:
        return "the two strings are anagram"
    else:
        return "the two strings are not anagram"


def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(anagram("EARTH", "HEART"))
