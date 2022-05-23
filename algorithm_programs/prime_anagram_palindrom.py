def primes(lower, upper):
    prime_list = []
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list


def anagram(a1):
    # initialize a list
    anagram_list = []
    for i in a1:
        for j in a1:
            if i != j and (sort(list(str(i))) == sort(list(str(j)))):
                anagram_list.append(i)
    return anagram_list


def palindrome(a2):
    palindrome_list = []
    for i in a2:
        temp = i
        rev = 0
        while i > 0:
            dig = i % 10
            rev = rev * 10 + dig
            i = i // 10
        if temp == rev:
            palindrome_list.append(rev)
    return palindrome_list


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


if __name__ == '__main__':
    print("The Prime Numbers are:\n", primes(100, 200), "\n")
    a = primes(1, 200)
    print("Prime Numbers between 100 to 200:")
    a3 = a[1:10]
    print(a3, "\n")
    print("The Anagram elements from 100 to 200 are listed :", anagram(a3), "\n")
    print("The palindrome elements from 100 to 200 are listed :", palindrome(a3), "\n")
    print("Prime Numbers between 201 to 300:")
    b = primes(200, 300)
    a4 = b[:]
    print(a4, "\n")
    print("The Anagram elements from 201 to 300 are listed :", anagram(a4), "\n")
    print("The Anagram elements from 201 to 300 are listed :", palindrome(a4), "\n")
