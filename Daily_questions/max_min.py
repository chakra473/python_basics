def max_min(num, max_or_min, arr):
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
    if max_or_min == "MAX":
        num_1 = -num
        return f"the {num} largest number is {arr[num_1]}"
    elif max_or_min == "MIN":
        num_1 = num - 1
        return f"the {num} smallest number is {arr[num_1]}"
    else:
        return arr


print(max_min(1, "MIN", [45, 12, 43, 123, 432, 100]))
