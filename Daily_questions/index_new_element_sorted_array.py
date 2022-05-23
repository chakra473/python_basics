# Python program for the above approach

# Function to find insert position of K
def find_index(arr, n, k):
    arr = sorted(arr)
    for i in range(n):

        # If k is found
        if arr[i] == k:
            return i

        # If arr[i] exceeds K
        elif arr[i] > k:
            return i

    # If all array elements are smaller
    return n


# Driver Code
arr1 = [1, 31, 5, 3]
n1 = len(arr1)
k1 = 25
print(find_index(arr1, n1, k1))
