# Python program for implementation of Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
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


if __name__ == '__main__':
    arr1 = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(arr1)

    print("Sorted array is:")
    for k in range(len(arr1)):
        print("% d" % arr1[k], end=" ")
